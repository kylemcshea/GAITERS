import serial
import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime
import psycopg2 as psy

dbName = "zdwkvtfh"
dbUser = "zdwkvtfh"
dbPass = "Jc3rLhG14M9TR2U77iz8PX8Lgb-UyHZl"
dbHost = "queenie.db.elephantsql.com"
dbPort = "5432"

try:
    conn = psy.connect(database = dbName, user = dbUser, password = dbPass, host= dbHost, port= dbPort)

    print("DB connect")
except:
    print("failed connect")
cur = conn.cursor()

ser = serial.Serial("/dev/cu.usbmodem14201",9600)
time.sleep(1)
b=ser.readline()
data = []
for i in range(10):
    b=ser.readline()
    string_n = b.decode()
    s = string_n.rstrip()
    s = s.split("|")
    s=s[:-1]
    lineOfTable = [int(s[0])]
    for a in range(1,len(s)-1):
        lineOfTable.append(int(s[a][11:]))
    lineOfTable.append(int(s[-1][-1]))
    lintOfTable = np.array(lineOfTable)
    data.append(lineOfTable)
    cur.execute(
        "INSERT INTO Test(ID, SENSOR_1, SENSOR_2, SENSOR_3, SENSOR_4, SENSOR_5, SENSOR_6, SENSOR_7, SENSOR_8, SENSOR_9, SENSOR_10, SENSOR_11, SENSOR_12, SENSOR_13, SENSOR_14, SENSOR_15, SENSOR_16, OUT) VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (i, int(s[1][11:]), int(s[2][11:]), int(s[3][11:]), int(s[4][11:]), int(s[5][11:]), int(s[6][11:]), int(s[7][11:]), int(s[8][11:]), int(s[9][11:]), int(s[10][11:]), int(s[11][11:]), int(s[12][11:]), int(s[13][11:]), int(s[14][11:]), int(s[15][11:]), int(s[16][11:]), int(s[17][-1])))
conn.commit()
conn.close()
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
