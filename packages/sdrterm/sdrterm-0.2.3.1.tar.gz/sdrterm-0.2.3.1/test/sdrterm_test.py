from os import getpid

import pytest
import sdrterm
from multiprocessing import Value

def test_main():
    FILE_NAME = "/mnt/d/SDRSharp_20160101_231914Z_12kHz_IQ.wav"
    sdrterm.__setStartMethod()
    sdrterm.isDead =  Value('b', 0)
    sdrterm.__deletePidFile = sdrterm.__generatePidFile(getpid())
    sdrterm.main(inFile=FILE_NAME,
                 outFile="/dev/null",
                 # outFile=/tmp/out.bin,
                 omegaOut=5000, verbose=1)
    sdrterm.main(inFile=FILE_NAME,
                 outFile="/dev/null",
                 omegaOut=5000, verbose=2)
    sdrterm.main(inFile=FILE_NAME,
                 outFile="/dev/null",
                 omegaOut=5000,
                 tuned=155685000,
                 center=-350000,
                 vfos="15000,-60000",
                 plot="ps,water,vfo")