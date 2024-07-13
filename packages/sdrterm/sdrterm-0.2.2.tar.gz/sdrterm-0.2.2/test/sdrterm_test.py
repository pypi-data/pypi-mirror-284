from os import getpid

import pytest
import sdrterm
from multiprocessing import Value

def test_main():
    sdrterm.__setStartMethod()
    sdrterm.isDead =  Value('b', 0)
    sdrterm.isDead.value = 0
    sdrterm.__deletePidFile = sdrterm.__generatePidFile(getpid())
    sdrterm.main(inFile="/mnt/d/uint8.wav",
                 outFile="/mnt/d/testing/out.bin",
                 omegaOut=5000, verbose=1)
    sdrterm.main(inFile="/mnt/d/uint8.wav",
                 outFile="/dev/null",
                 omegaOut=5000, verbose=2)
    sdrterm.main(inFile="/mnt/d/uint8.wav",
                 outFile="/dev/null",
                 omegaOut=5000,
                 tuned=155685000,
                 center=-350000,
                 vfos="15000,-60000",
                 plot="ps,water,vfo")