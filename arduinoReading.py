import serial
import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime

ser = serial.Serial('COM5',9600)
time.sleep(2)
b=ser.readline()
data = []
for i in range(50):
    b=ser.readline()
    string_n = b.decode()
    s = string_n.rstrip()
    s = s.split("|")
    s=s[:-1]
    lineOfTable = [float(s[0])]
    print(s)
    for a in range(1,len(s)):
        lineOfTable.append(float(s[a][11:]))
    lineOfTable = np.array(lineOfTable)
    data.append(lineOfTable)

#data = [np.array([0, 242.0, 234.0, 242.0,240.0,239.0]), np.array([1, 240.0, 233.0, 240.0,242.0,241.0]), np.array([2, 232.0, 134.0, 240.0,237.0,235.0]), np.array([3, 245.0, 240.0, 242.0,241.0,220.0]), np.array([4, 244.0, 244.0, 243.0,241.0,240.0]), np.array([5, 239.0, 140.0, 240.0,241.0,229.0])]
column = ["Count"]
for col in range(1, len(data[0])):
    column.append("Sensor " + str(col - 1))

data = np.array(data)
df = pd.DataFrame(data, columns = column)
dfnotefic = df.drop("Count", axis=1)
now = datetime.datetime.now()
csv_file = str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute) + ".csv"
dfnotefic.to_csv(csv_file)
sns.scatterplot(data= dfnotefic)
plt.show()
