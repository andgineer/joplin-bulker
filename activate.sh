#!/usr/bin/env bash
#
# "Set-ups or/and activates development environment"
#

VENV_FOLDER=".venv"
PYTHON="python3.11"  # sync with python-version: '3.11' in .github/workflows/static.yml

RED='\033[1;31m'
GREEN='\033[1;32m'
CYAN='\033[1;36m'
NC='\033[0m' # No Color

if ! (return 0 2>/dev/null) ; then
    # If return is used in the top-level scope of a non-sourced script,
    # an error message is emitted, and the exit code is set to 1
    echo
    echo -e $RED"This script should be sourced like"$NC
    echo "    . ./activate.sh"
    echo
    exit 1
fi

# virtual env
if [[ ! -d ${VENV_FOLDER} ]] ; then
    echo -e $CYAN"Creating virtual environment for python in ${VENV_FOLDER}"$NC
    $PYTHON -m venv ${VENV_FOLDER}
    . ${VENV_FOLDER}/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.dev.txt
    pip install -e .
else
    echo -e $CYAN"Activating virtual environment ..."$NC
    . ${VENV_FOLDER}/bin/activate
fi
