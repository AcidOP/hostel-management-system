from mysql.connector import connect

USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
DATABASE = 'hostel'

# Connect to the database
db = connect(
    host=HOST,
    user=USERNAME,
    password=PASSWORD,
    database=DATABASE,
    auth_plugin='mysql_native_password'
  )

cursor = db.cursor()
