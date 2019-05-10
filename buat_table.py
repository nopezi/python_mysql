import mysql.connector
import database

# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "",
#     database = "python"
# )

cursor = database.db.cursor()

sql = """ CREATE TABLE customers (
          customer_id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(255),
          address VARCHAR(255)
) """

cursor.execute(sql)


print("Table berhasil di buat")