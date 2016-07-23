#!/usr/bin/env bash
#########################################################################
## create virtual environment using virtualenv package
#sudo pip install virtualenv
echo `which python`

# Absolute path to this script, e.g. /home/user/bin/foo.sh
FPATH=$(readlink -f "$0")
DIR=$(dirname "$FPATH") # only print a dot (.)
echo "$DIR"

# virtual environment directory
VirtEnv="$DIR"/virtEnv

#####
### 1. create virtual environment folder where python executable files, a copy of the pip library which you can use to install other packages are contained.
virtualenv "$VirtEnv"
#
## option: use a python interpreter of your choice.
#virtualenv -p /usr/bin/python2.7 "$VirtEnv"

#####
### 2. To begin using the virtual environment, it needs to be activated:
source "$VirtEnv"/bin/activate
## test virtual environment 
#echo `which python`

#####
### 3. From now on, any package that you install using pip will be placed in the venv folder, isolated from the global Python installation. 
## Install pakcages
pip install requests
# or
#pip install -r requirement.txt # requirement.txt saves package name and version. It is recommanded. Since exact package version can be controled. 


## this shows what libraries have been installed. In this case only requests is installed.
pip freeze

# 4. If you are done working in the virtual environment for the moment, you can deactivate it:
#deactivate
