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
    user = User()

    while True:
        command = input("Command: ").lower()
        if command == "show users":
            show_users(users)
        elif command == "add":
            add_user(user)
        elif command == "del":
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
      print()
    else:
        print ("No Users\r\n")

def add_user(user):
    print()

def del_user(user):
    print()

if __name__ == "__main__":
    main()