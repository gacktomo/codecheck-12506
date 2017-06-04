#!/usr/bin/env python3
import struct
import sys

symbolList = ["+","-","*","/","(",")"]
numList = []
calcList = []

def main(argv):
    
    anser = 0
    if argv[0] == "":
        sys.stderr.write('you need arg')
        sys.exit(1)
    if argv[0].count("(") != argv[0].count(")"):
        sys.stderr.write('invalid arg')
        sys.exit(3)
    for c in argv[0]:
        if c != " ":
            if c.isdigit():
                numList.append(c)
            elif c in symbolList:
                calcList.append(c)
            else:
                sys.stderr.write('invalid symbol')
                sys.exit(2)
    try:
        anser = eval(argv[0])
    except:
        sys.stderr.write('invalid calc')
        sys.exit(4)
    
    print(" ".join(numList)," ".join(calcList),"=",anser)
    sys.exit(0)
    
    
    
