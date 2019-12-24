import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)

cursor = db.cursor()
sql="update film set title= %s, year=%s, budget=%s, director=%s  where id = %s"
values = ("The Irishman",2019,140000000,"Martin Scorsese", 1)

cursor.execute(sql, values)

db.commit()
print("update done")