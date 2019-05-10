import mysql.connector 
import database

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd=""
# )

if database.db.is_connected():
  print("Berhasil terhubung ke database")