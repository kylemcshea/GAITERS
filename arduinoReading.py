import serial
import time
import numpy as np
import pandas as pd
ser = serial.Serial('COM5',9600)
time.sleep(2)
b=ser.readline()
data = []
for i in range(5):
    b=ser.readline()
    string_n = b.decode()
    s = string_n.rstrip()
    s = s.split("|")
    s=s[:-1]
    lineOfTable = [float(s[0])]
    for a in range(1,len(s)):
        lineOfTable.append(float(s[a][11:]))
    lintOfTable = np.array(lineOfTable)
    data.append(lineOfTable)
column = ["Count"]
for col in range(1, len(data[0])):
    column.append("Sensor " + str(col - 1))

data = np.array(data)
df = pd.DataFrame(data, columns = column)
print(df)
