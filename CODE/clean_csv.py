#!/usr/bin/python3

import sys

outData = []

with open(sys.argv[1]) as file:
    data = file.readlines()

    
    lSplit = data[0].strip().split(",")
    
    addr = lSplit[2]
    id = int(lSplit[1])
    dat = lSplit[3]
    wrType = lSplit[4]

    packetID = id
    currentBuildingLine = str(wrType) + "," + str(addr) + "," + str(dat)

    for line in data[1:]:
        lSplit = line.strip().split(",")
        addr = lSplit[2]
        id = int(lSplit[1])
        dat = lSplit[3]
        wrType = lSplit[4]

        if(id != packetID):
            outData.append(currentBuildingLine)
            currentBuildingLine = str(wrType) + "," + str(addr) + "," + str(dat)
            packetID = id
        else:
            currentBuildingLine += "," + str(dat)

fileOut = sys.argv[1].replace(".csv","_cleaned.csv")
with open(fileOut,"w") as out:
    for i in outData:
        out.write(i + "\n")
