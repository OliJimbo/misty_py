#!/usr/bin/env python3
## From https://blackboxtoolkit.com/usbttl.html

import serial
ser = serial.Serial("COM1", 115200, timeout=1)
ser.write("RR".encode())
core.wait(0.025) #wait 25 mS after resetting
ser.write("01".encode()) #line 1 high
<My Stimulus Image Shown Here>
<My Stimulus Image Removed>
ser.write("00".encode()) #turn all lines off
core.wait(0.025)
ser.flush()
ser.close()
