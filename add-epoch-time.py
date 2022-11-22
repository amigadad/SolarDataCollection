import sqlite3
import datetime
from datetime import datetime
import time

file = 'SolarDataCollection.db'
conn = sqlite3.connect(file)
c = conn.cursor()
c2 = conn.cursor()


def read_from_db():
    unix_time_start = int(time.time()*1000)
    print("Start Time ", unix_time_start)
    c.execute("SELECT * FROM 'Raw Solar Data'")
    count = 0

    for row in c.fetchall():
        count = count + 1
        epoch_time = int((datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S").timestamp())*1000)
        c2.execute("UPDATE 'Raw Solar Data' SET Epoch = (?) WHERE ID = (?)", (epoch_time, count))
        conn.commit()


read_from_db()
unix_time_end = int(time.time()*1000)
print("End Time ", unix_time_end)
print("Finished!")
c.close()
c2.close()
conn.close()
