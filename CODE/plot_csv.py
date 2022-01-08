#!/usr/bin/python3

from os import linesep
import sys
import matplotlib.pyplot as plt

outData = []

dsp2_xram = []
dsp2_yram = []

with open(sys.argv[1]) as file:
    data = file.readlines()

    for line in data:
        lineSplit = line.strip().split(",")
        
        # Get writes to xram or whyram
        if(lineSplit[0] == "Write"):
            # Extract address
            addrHigh = int(lineSplit[2],16)
            addrLow = int(lineSplit[3],16)
            address = (addrHigh<<8) + addrLow

            print(address)

            # Check address range
            if(address >= 0x1000 and address <= 0x127F):
                # We are in XRAM (DSP2)
                settingValue = ((int(lineSplit[4],16)<<16) + (int(lineSplit[5],16)<<8) + int(lineSplit[6],16)) & 0b111111111111111111111111
                dsp2_xram.append((address,settingValue))

            elif(address >=0x2000 and address <= 0x21FF):
                # We ar ein YRAM (DSP2)
                settingValue = ((int(lineSplit[4],16)<<8) + int(lineSplit[5],16)) & 0b111111111111
                dsp2_yram.append((address,settingValue))

#plt.plot([x[0] for x in dsp2_xram],[x[1] for x in dsp2_xram])
plt.plot([x[0] for x in dsp2_yram],[x[1] for x in dsp2_yram])
#plt.plot([x[1] for x in dsp2_xram],[x[1] for x in dsp2_yram])
plt.show()


