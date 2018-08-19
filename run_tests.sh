#!/usr/bin/env bash

: "${VIRTUAL_ENV?Make sure that the tests are run within a virtual environment!}"

export DB_URL=sqlite:///fatlama.sqlite3
export SPATIALITE_LIBRARY_PATH=/usr/local/lib/mod_spatialite.dylib

pip install -q -r requirements.txt
pip install -q -r requirements_test.txt

PYTHONPATH=./ python -m pytest
