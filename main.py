"""
This module contains functions entering creating users, viewing existing users,
creating user tasks list, viewing user task list
"""
import db
from Userclass import User


def main(user=None):
    show_title()
    show_menu()
    users = db.get_users()
    users_set = set(users)
    user = User("", 1)

    while True:
        command = input("Command: ").lower()
        if command == "show users":
            show_users(users)
        elif command == "add user":
            add_user(user, users_set)
        elif command == "del user":
            del_user(user)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

def show_title():
    print("The User Task List Program\r\n")

def show_menu():
    print("COMMAND MENU")
    print("show users - Show the users")
    print("add user  - Add a user")
    print("del user  - Delete an user")
    print("exit - Exit program")
    print()

def show_users(users):
    """
    Displays the current users, if any
    otherwise displays 'No Users'
    """
    print("Users\r\n")
    if users is not None:
      print ("User Name\tUser ID")
      for i, user in enumerate(users, start=1):
          print(f"{user.get_user_name():s}\t\t\t"
                f"{user.get_user_id():>4d}")
          print()
    else:
        print ("No Users\r\n")

def add_user(user, users_set):
    user_name = str(input("User Name: "))

    user_id = int(input("User ID:"))

    user = User(user_name, user_id)

    if user in users_set:
        print (f"User Found: {user.get_user_name()}\n")
    else:
        users_set.add(user)
        db.add_user(user)

def del_user(user):
    print()

if __name__ == "__main__":
    main()