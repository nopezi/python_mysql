import mysql.connector
import database

cursor = database.db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

result = cursor.fetchall()

for data in result:
    # gambar = data[1]
    print(data)
