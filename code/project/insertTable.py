import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)

cursor = db.cursor()
sql="insert into film (title, year, budget, director) values (%s,%s,%s,%s)"
#values = ("Toy Story",1995,50000000,"John Lasseter")
#values = ("Casino",1995,60000000, "Martin Scorsese")
values = ("The Hangover",2010, 40000000,"Todd Phillips")
#values = ("Due Date",2015, 40000000,"Todd Phillips")


cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)