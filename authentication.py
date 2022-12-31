import hashlib
import getpass
from connection import db, cursor

# Add new user with their username and hashed password
def register():
  name = input("Enter your name: ")
  password = getpass.getpass("Enter your password: ")
  phone_no = input("Enter your phone number: ")
  email = input("Enter your email: ")
  hash = hash_password(password)
  query = "INSERT INTO management (name, password, phone_number, email) VALUES (%s, %s, %s, %s)"
  values = (name, hash, phone_no, email)

  cursor.execute(query, values)
  db.commit()
  print("[+] Successfully registered.")

# Returns true if successfully authenticated
def login():
  name = input("Enter your name: ")
  password = getpass.getpass("Enter your password: ")
  cursor.execute("SELECT password FROM management WHERE name = %s", (name,))
  hash = cursor.fetchone()
  if hash is None:
    return False
  else:
    return hash[0] == hash_password(password)


def hash_password(text):
  encoded_pw = text.encode()
  hash_object = hashlib.sha1(encoded_pw)
  return hash_object.hexdigest()
