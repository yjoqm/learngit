#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
echo $DIR
export PYTHONPATH=$DIR:$PYTHONPATH
export ENV=$1
echo $1
source /usr/local/bin/virtualenvwrapper.sh
workon sona
