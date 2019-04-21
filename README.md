CSIS-250-4704 Final Project
Project to automate a test on a UUT with a power supply with programmable capbility.
Requirements:
In order to use this application the user must have a BK power supply model 1697.  In addition, the BK drivers mustbe installed before using this application.

Installaton:
import serial(pySerial module) is required in order to communicate with the PC serial ports.
Other modules may be added as the project is completed.
To install the drivers, open the 169x SW folder and click the setup icon, follow instructions as prompted.

Operating instructions:
Once the requirment above have been done, connect the power supply to a serial com port that is not being used by another peripheral in the PC, use a RS232 serial cable to conect between the RS232 connectors in the powers supply to the PC serial com port.
Connec the device under test, and run the executable programm.

List of Files:
for now include files:
BK.py to enter the required configuration settings for the test to be performed with the power supply. This file needs more code.
PSRampUp.py The file where the user enteres the desired inputs to be performed by the power supply.
Another file, an executable file, must be created after the main code is finished. the file will ask the user to enter desired information to configure the testig of a UUT.

troubleshooting:
Based on the project requirements, classes need to be incorporated to the code in order to accomplish the requirements.  Updates will be documented here...

Changelog:
List of changes are listed her in chronological order.  updates will be documented here...






