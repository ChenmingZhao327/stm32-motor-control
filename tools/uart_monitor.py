import serial
ser = serial.Serial("COM5", 115200, timeout=1)
while 1:
    data = ser.readline()
    if data:
        print(data.decode('utf-8').rstrip())