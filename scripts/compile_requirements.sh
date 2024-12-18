#!/usr/bin/env bash
#
# Pin current dependencies versions.
#

uv pip compile requirements.in --output-file=requirements.txt --upgrade
uv pip compile requirements.dev.in --output-file=requirements.dev.txt --upgrade
