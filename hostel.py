from connection import db, cursor
from authentication import login, register

LOGIN = False

# Method to only accept a number as input
def input_digit():
  answer = input(">>> ")
  # Check if answer is a number
  try:
    answer = int(answer)
    return answer
  except ValueError:
    print("[+] Invalid input. Please enter a number.")
    return input_digit()

# First check if user is a valid user
def authenticate():
  welcome_msg = """
  [+] Welcome to the hostel management system.
  [+] Please select an option:

  (1) Register
  (2) Login
  (3) Exit
  """

  print(welcome_msg)
  answer = input_digit()
  global LOGIN
  if answer == 1:
    register()
    LOGIN = True
  elif answer == 2:
    if login():
      LOGIN = True
    else:
      # Clear the screen
      print("\033c")
      print("[+] Invalid username or password.")
  elif answer == 3:
    print("[+] Exiting...")
    exit()
  else:
    print("[+] Invalid input. Please enter a number from 1 to 3.")
    authenticate()

def all_records():
  cursor.execute("SELECT * FROM students")
  result = cursor.fetchall()

  if not result:
    print("[+] No records found.")
    return

  for row in result:
    print(row)

# Adding a new entry to the database
def add_record(name, room_number, phone_number, father_name):
  query = "INSERT INTO students (name, room_number, phone_number, father_name) VALUES (%s, %s, %s, %s)"
  values = (name, room_number, phone_number, father_name)
  cursor.execute(query, values)
  db.commit()

# Deleting an entry from the database
def delete_record(roll_no):
  cursor.execute(f"DELETE FROM students WHERE roll_number = {roll_no}")
  db.commit()

# Change the contents of an entry
def update_record(name, room_number, phone_number, father_name):
  query = "UPDATE students SET (name, room_number, phone_number, father_name) VALUES (%s, %s, %s, %s)"
  values = (name, room_number, phone_number, father_name)
  cursor.execute(query, values)
  db.commit()

# View the contents of an entry
def view_record(roll_no):
  cursor.execute(f"SELECT * FROM students WHERE roll_number = {roll_no}")
  result = cursor.fetchall()

  if not result:
    print("[+] No such record found.")
    return

  for row in result:
    print(row)
  
def main():
  if LOGIN:
    # print("\033c")
    print("\n[+] Logged in successfully.")
    print("[+] Please select an option:")
    print("(1) View all records")
    print("(2) Add a new record")
    print("(3) Delete a record")
    print("(4) Update a record")
    print("(5) View a record")
    print("(6) Exit\n")
    
    is_exit = False

    while not is_exit:
      answer = input_digit()
      if answer == 1:
        all_records()
      elif answer == 2:
        name = input("Enter name: ")
        room_number = input("Enter room number: ")
        phone_number = input("Enter phone number: ")
        father_name = input("Enter father's name: ")
        add_record(name, room_number, phone_number, father_name)
      elif answer == 3:
        roll_no = input("Enter roll number: ")
        delete_record(roll_no)
      elif answer == 4:
        roll_no = input("Enter roll number: ")
        name = input("Enter name: ")
        room_number = input("Enter room number: ")
        phone_number = input("Enter phone number: ")
        father_name = input("Enter father's name: ")
        update_record(name, room_number, phone_number, father_name)
      elif answer == 5:
        roll_no = input("Enter roll number: ")
        view_record(roll_no)
      elif answer == 6:
        print("[+] Exiting...")
        is_exit = True

    else:
      print("[+] Invalid input. Please enter a number from 1 to 6.")
      main()
  else:
    print("[+] Please login first.")
    authenticate()

if __name__ == "__main__":
  authenticate()
  main()
