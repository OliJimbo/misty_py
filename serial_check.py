import serial
import time
import numpy as np
try:
    sr=serial.Serial("COM8", 115200, timeout=1)
    print("Serial Connected")
except serial.serialutil.SerialException:
    print("Serial Not Connected")

evntlg = 'sr' in locals() or 'sr' in globals()
for i in np.arange(1, 256):
    thisbyte=str(hex(i).split('x')[-1]).encode()
    if evntlg: sr.write(thisbyte)
    else: print(thisbyte)
    time.sleep(0.1)
    if evntlg: sr.write('00'.encode())
    else: print('00'.encode())
    time.sleep(0.1)