import mysql.connector
import database

cursor = database.db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val = ("nama", "alamat")

cursor.execute(sql, val)

database.db.commit()

print("{} data ditambahkan".format(cursor.rowcount))