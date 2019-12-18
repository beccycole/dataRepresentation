import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

  database="datarepresentation"
)

cursor = db.cursor()
sql="insert into films (title, year, budget, director) values (%s,%s,%s,%s)"
values = ('Sabrina',2004, 58000000, 'Lee Toland Krieger')

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)