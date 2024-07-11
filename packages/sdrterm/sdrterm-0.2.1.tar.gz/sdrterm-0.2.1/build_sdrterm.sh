#!/bin/bash
WD=$(pwd)
#cd ~/sdrterm && python -m pip install build twine && python -m build && twine check dist/* && twine upload dist/*

cd /tmp && rm -rf .venv/ && python -m venv .venv && . .venv/bin/activate && pip install sdrterm[gui] && cd /tmp
cp ~/sdrterm/*.sh .
./test.sh
deactivate
cd $WD
