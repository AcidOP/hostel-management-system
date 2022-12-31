from mysql.connector import connect
from connection import USERNAME, PASSWORD, HOST, DATABASE

# Connect to the database
db = connect(
    host=HOST,
    user=USERNAME,
    password=PASSWORD,
    auth_plugin='mysql_native_password',
)

cursor = db.cursor()

# Create the database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
cursor.execute(f"USE {DATABASE}")

# Add a table for the student
cursor.execute('CREATE TABLE students (name VARCHAR(60), roll_number smallint UNSIGNED PRIMARY KEY AUTO_INCREMENT, room_number smallint UNSIGNED, phone_number VARCHAR(10), father_name VARCHAR(60));')

# Add a table for management staff
cursor.execute('CREATE TABLE management (name VARCHAR(60), id smallint UNSIGNED PRIMARY KEY AUTO_INCREMENT, password VARCHAR(60), phone_number VARCHAR(10), email VARCHAR(60));')
