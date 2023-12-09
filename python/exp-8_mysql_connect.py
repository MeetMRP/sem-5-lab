import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="db"
)

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM table")

for row in cursor.fetchall():
    print(row)

cursor.close()
db_connection.close()
