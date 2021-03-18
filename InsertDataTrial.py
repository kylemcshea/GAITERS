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
i = 0

sen1 = 123
sen2 = 124
sen3 = 945
sen4 = 423
sen5 = 324
sen6 = 157
sen7 = 123
sen8 = 124
sen9 = 945
sen10 = 423
sen11 = 324
sen12 = 157
sen13 = 423
sen14 = 324
sen15 = 157
sen16 = 189

cur.execute("INSERT INTO Trial(ID, SENSOR_1, SENSOR_2, SENSOR_3, SENSOR_4, SENSOR_5, SENSOR_6, SENSOR_7, SENSOR_8, SENSOR_9, SENSOR_10, SENSOR_11, SENSOR_12, SENSOR_13, SENSOR_14, SENSOR_15, SENSOR_16) VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i, sen1, sen2, sen3, sen4, sen5, sen6, sen7, sen8, sen9, sen10,sen11,sen12,sen13,sen14,sen15,sen16))
conn.commit()
conn.close()
print("Working")