#!/bin/bash
WD=$PWD;
#cd ~/sdrterm && python -m pip install build twine && python -m build && twine check dist/* && twine upload dist/*
#export DSD_CMD="/home/peads/dsd/build/dsd -q -i - -o /dev/null -n";

cd /tmp && rm -rf .venv/ && python -m venv .venv && . .venv/bin/activate && pip install sdrterm[gui] --upgrade && cd /tmp \
  && cp ~/sdrterm/*.sh . && ./test.sh && deactivate;
cd $WD;
