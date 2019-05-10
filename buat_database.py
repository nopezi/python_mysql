import mysql.connector
import database

# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     passwd = ""
# )

cursor = database.db.cursor()
cursor.execute("CREATE DATABASE python")

print("DATABASE BERHASIL DI BUAT")