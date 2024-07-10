#!/usr/bin/python3

# SPDX-FileCopyrightText: 2021 Jeff Epler
#
# SPDX-License-Identifier: GPL-3.0-only

"""Update the DUT1 and LS data based on online sources"""

from __future__ import annotations

import csv
import datetime
import io
import itertools
import pathlib
from typing import Callable

import bs4
import click
import platformdirs
import requests

DIST_PATH = pathlib.Path(__file__).parent / "iersdata_dist.py"

OLD_TABLE_START: datetime.date | None = None
OLD_TABLE_END: datetime.date | None = None
if DIST_PATH.exists():
    import wwvb.iersdata_dist

    OLD_TABLE_START = wwvb.iersdata_dist.DUT1_DATA_START
    OLD_TABLE_END = OLD_TABLE_START + datetime.timedelta(days=len(wwvb.iersdata_dist.DUT1_OFFSETS) - 1)

IERS_URL = "https://datacenter.iers.org/data/csv/finals2000A.all.csv"
IERS_PATH = pathlib.Path("finals2000A.all.csv")
if IERS_PATH.exists():
    IERS_URL = str(IERS_PATH)
    print("using local", IERS_URL)
NIST_URL = "https://www.nist.gov/pml/time-and-frequency-division/atomic-standards/leap-second-and-ut1-utc-information"


def _get_text(url: str) -> str:
    """Get a local file or a http/https URL"""
    if url.startswith("http"):
        with requests.get(url, timeout=30) as response:
            return response.text
    else:
        return pathlib.Path(url).read_text(encoding="utf-8")


def update_iersdata(  # noqa: PLR0915, PLR0912
    target_path: pathlib.Path,
) -> None:
    """Update iersdata.py"""
    offsets: list[int] = []
    iersdata_text = _get_text(IERS_URL)
    for r in csv.DictReader(io.StringIO(iersdata_text), delimiter=";"):
        jd = float(r["MJD"])
        offs_str = r["UT1-UTC"]
        if not offs_str:
            break
        offs = int(round(float(offs_str) * 10))
        if not offsets:
            table_start = datetime.date(1858, 11, 17) + datetime.timedelta(jd)

            when = min(datetime.date(1972, 1, 1), table_start)
            # iers bulletin A doesn't cover 1972, so fake data for those
            # leap seconds
            while when < datetime.date(1972, 7, 1):
                offsets.append(-2)
                when = when + datetime.timedelta(days=1)
            while when < datetime.date(1972, 11, 1):
                offsets.append(8)
                when = when + datetime.timedelta(days=1)
            while when < datetime.date(1972, 12, 1):
                offsets.append(0)
                when = when + datetime.timedelta(days=1)
            while when < datetime.date(1973, 1, 1):
                offsets.append(-2)
                when = when + datetime.timedelta(days=1)
            while when < table_start:
                offsets.append(8)
                when = when + datetime.timedelta(days=1)

            table_start = min(datetime.date(1972, 1, 1), table_start)

        offsets.append(offs)

    wwvb_text = _get_text(NIST_URL)
    wwvb_data = bs4.BeautifulSoup(wwvb_text, features="html.parser")
    wwvb_dut1_table = wwvb_data.findAll("table")[2]
    assert wwvb_dut1_table
    meta = wwvb_data.find("meta", property="article:modified_time")
    assert isinstance(meta, bs4.Tag)
    wwvb_data_stamp = datetime.datetime.fromisoformat(meta.attrs["content"]).replace(tzinfo=None).date()

    def patch(patch_start: datetime.date, patch_end: datetime.date, val: int) -> None:
        off_start = (patch_start - table_start).days
        off_end = (patch_end - table_start).days
        offsets[off_start:off_end] = [val] * (off_end - off_start)

    wwvb_dut1: int | None = None
    wwvb_start: datetime.date | None = None
    for row in wwvb_dut1_table.findAll("tr")[1:][::-1]:
        cells = row.findAll("td")
        when = datetime.datetime.strptime(cells[0].text + "+0000", "%Y-%m-%d%z").date()
        dut1 = cells[2].text.replace("s", "").replace(" ", "")
        dut1 = int(round(float(dut1) * 10))
        if wwvb_dut1 is not None:
            assert wwvb_start is not None
            patch(wwvb_start, when, wwvb_dut1)
        wwvb_dut1 = dut1
        wwvb_start = when

    # As of 2021-06-14, NIST website incorrectly indicates the offset of -600ms
    # persisted through 2009-03-12, causing an incorrect leap second inference.
    # Assume instead that NIST started broadcasting +400ms on January 1, 2009,
    # causing the leap second to occur on 2008-12-31.
    patch(datetime.date(2009, 1, 1), datetime.date(2009, 3, 12), 4)

    # this is the final (most recent) wwvb DUT1 value broadcast.  We want to
    # extend it some distance into the future, but how far?  We will use the
    # modified timestamp of the NIST data.
    assert wwvb_dut1 is not None
    assert wwvb_start is not None
    patch(wwvb_start, wwvb_data_stamp + datetime.timedelta(days=1), wwvb_dut1)

    with target_path.open("w", encoding="utf-8") as output:

        def code(*args: str) -> None:
            """Print to the output file"""
            print(*args, file=output)

        code("# -*- python3 -*-")
        code("# fmt: off")
        code('"""File generated from public data - not subject to copyright"""')
        code("# SPDX" + "-FileCopyrightText: Public domain")
        code("# SPDX" + "-License-Identifier: CC0-1.0")
        code("# isort: skip_file")
        code("import datetime")

        code("__all__ = ['DUT1_DATA_START', 'DUT1_OFFSETS']")
        code(f"DUT1_DATA_START = {table_start!r}")
        c = sorted(chr(ord("a") + ch + 10) for ch in set(offsets))
        code(f"{','.join(c)} = tuple({''.join(c)!r})")
        code(f"DUT1_OFFSETS = str( # {table_start.year:04d}{table_start.month:02d}{table_start.day:02d}")
        line = ""
        j = 0

        for val, it in itertools.groupby(offsets):
            part = ""
            ch = chr(ord("a") + val + 10)
            sz = len(list(it))
            if j:
                part = part + "+"
            part = part + ch if sz < 2 else part + f"{ch}*{sz}"
            j += sz
            if len(line + part) > 60:
                d = table_start + datetime.timedelta(j - 1)
                code(f"    {line:<60s} # {d.year:04d}{d.month:02d}{d.day:02d}")
                line = part
            else:
                line = line + part
        d = table_start + datetime.timedelta(j - 1)
        code(f"    {line:<60s} # {d.year:04d}{d.month:02d}{d.day:02d}")
        code(")")
    table_end = table_start + datetime.timedelta(len(offsets) - 1)
    if OLD_TABLE_START:
        print(f"old iersdata covered {OLD_TABLE_START} .. {OLD_TABLE_END}")
    print(f"iersdata covers {table_start} .. {table_end}")


def iersdata_path(callback: Callable[[str, str], pathlib.Path]) -> pathlib.Path:
    """Find out the path for this directory"""
    print("iersdata_path", callback)
    r = callback("wwvbpy", "unpythonic.net") / "wwvb_iersdata.py"
    print(f"iersdata_path {r=!r}")
    return r


@click.command()
@click.option(
    "--user",
    "location",
    flag_value=iersdata_path(platformdirs.user_data_path),
    default=iersdata_path(platformdirs.user_data_path),
    type=pathlib.Path,
)
@click.option("--dist", "location", flag_value=DIST_PATH)
@click.option("--site", "location", flag_value=iersdata_path(platformdirs.site_data_path))
def main(location: str) -> None:
    """Update DUT1 data"""
    path = pathlib.Path(location)
    print(f"will write to {location!r}")
    path.parent.mkdir(parents=True, exist_ok=True)
    update_iersdata(path)


if __name__ == "__main__":
    main()
