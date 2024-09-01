import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Deadly245!',
    database = 'Fitapp'
)

if db.is_connected():
    print("Successfully connected to the database")