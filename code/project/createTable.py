
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

  database="datarepresentation"
)

cursor = db.cursor()
sql="CREATE TABLE films (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), year INT, budget INT, director VARCHAR(255))"

cursor.execute(sql)