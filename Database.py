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
cur.execute("""
CREATE TABLE Test
(
ID INT PRIMARY KEY NOT NULL,
SENSOR_1 INT NOT NULL,
SENSOR_2 INT NOT NULL,
SENSOR_3 INT NOT NULL,
SENSOR_4 INT NOT NULL,
SENSOR_5 INT NOT NULL,
SENSOR_6 INT NOT NULL,
SENSOR_7 INT NOT NULL,
SENSOR_8 INT NOT NULL,
SENSOR_9 INT NOT NULL,
SENSOR_10 INT NOT NULL,
SENSOR_11 INT NOT NULL,
SENSOR_12 INT NOT NULL,
SENSOR_13 INT NOT NULL,
SENSOR_14 INT NOT NULL,
SENSOR_15 INT NOT NULL,
SENSOR_16 INT NOT NULL,
OUT INT NOT NULL

)
""")
conn.commit()
print("Table Created")