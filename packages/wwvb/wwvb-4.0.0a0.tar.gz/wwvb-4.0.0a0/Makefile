ifeq ("$(origin V)", "command line")
BUILD_VERBOSE=$(V)
endif
ifndef BUILD_VERBOSE
$(info Use make V=1, make V=2 or set BUILD_VERBOSE similarly in your environment to increase build verbosity.)
BUILD_VERBOSE = 0
endif
ifeq ($(BUILD_VERBOSE),0)
Q = @
STEPECHO = @:
else ifeq ($(BUILD_VERBOSE),1)
Q = @
STEPECHO = @echo
else
Q =
STEPECHO = @echo
endif

PYTHON ?= python3

.PHONY: default
default: coverage mypy

COVERAGE_INCLUDE=--include "src/**/*.py"
.PHONY: coverage
coverage:
	$(Q)$(PYTHON) -mcoverage erase
	$(Q)env PYTHONPATH=src $(PYTHON) -mcoverage run --branch -p -m unittest discover -s src
	$(Q)$(PYTHON) -mcoverage combine -q
	$(Q)$(PYTHON) -mcoverage html $(COVERAGE_INCLUDE)
	$(Q)$(PYTHON) -mcoverage xml $(COVERAGE_INCLUDE)
	$(Q)$(PYTHON) -mcoverage report --fail-under=100 $(COVERAGE_INCLUDE)

.PHONY: mypy
mypy:
	$(Q)mypy --strict --no-warn-unused-ignores src

.PHONY: update
update:
	$(Q)env PYTHONPATH=src $(PYTHON) -mwwvb.updateiers --dist

# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -a -E -j auto
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Route particular targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.PHONY: html
html:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Pass the desired coverage tracer name to subprocesses
export COVERAGE_CORE

# Copyright (C) 2021 Jeff Epler <jepler@gmail.com>
# SPDX-FileCopyrightText: 2021 Jeff Epler
#
# SPDX-License-Identifier: GPL-3.0-only
