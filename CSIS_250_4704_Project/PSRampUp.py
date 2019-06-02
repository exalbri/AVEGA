'''
Program: PSRAmpUp.py
Author: Vega
This version prompts the user to enter desired inputs to test a UUT at
different ranges to help validate its functionality.
'''
import BK
import time

if __name__ == "__main__":
    PowerSupply = raw_input("Enter Power Supply serial port of the Modem: ")
    startV = float(raw_input("Enter Start Voltage(V): "))
    StepV = float(raw_input("Enter Step Voltage(V): "))
    Numloops = float(raw_input("Enter Number of loops: "))
    sleepBetweenLoops = float(raw_input("Enter Number of loops: "))
    sleepTime = float(raw_input("Enter time between Steps(seconds): "))
    maxV = float(raw_input("Enter Max Voltage(V): "))
    sup = BK.Supply(ident=PowerSupply)
    sup.enable()
    sup.voltage(startV)
    readV = 0;
    current = 0    
    for i in range(0,Numloops):
        newVolt = startV;
        time.sleep(sleepBetweenLoops)
        while readV < maxV:
            readV, current = sup.reading()
            print("Read Voltage ,%s Current %s"%(str(readV),str(current)))
            time.sleep(sleepTime)
            newVolt = newVolt + StepV;
            sup.voltage(newVolt)
    print("Done")
#===============================================================================
# End
#===============================================================================