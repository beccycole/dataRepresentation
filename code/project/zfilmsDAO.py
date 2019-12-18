import mysql.connector
class FilmDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",

        database="datarepresentation"
        )
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into films (title, year, budget, director) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from films"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from films where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
    def update(self, values):
        cursor = self.db.cursor()
        sql="update films set title= %s, year=%s, budget=%s, director=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from films where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

filmDAO = FilmDAO()
