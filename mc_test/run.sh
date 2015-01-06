#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$DIR:$PYTHONPATH
export ENV=$1
source /usr/local/bin/virtualenvwrapper.sh
workon mc_test 
if [ "x$1" != "x" ];then
    pybot -d src/report -i $1 src/suites/
else
    pybot -d src/report src/suites/ 
fi
