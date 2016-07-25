#!/usr/bin/env bash
# author : Chengyu Liu

echo `which python`

# Absolute path to this script, e.g. /home/user/bin/foo.sh
FPATH=$(readlink -f "$0")
DIR=$(dirname "$FPATH") # only print a dot (.)
echo "$DIR"

# virtual environment directory
VirtEnv="$DIR"/virtEnv

virtualenv "$VirtEnv"

source "$VirtEnv"/bin/activate
echo `which python`

pip install -r config/pypa-requirement

#pip freeze
./lib/config.py

#deactivate
