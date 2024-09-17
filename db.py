import csv
import os
from typing import TextIO

from Userclass import User

FILENAME = "users.csv"
users = []

def get_users():
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, newline="") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    # convert row to Product object
                    user = User(str(row[0]), int(row[1]))
                    users.append(user)
            return users
        else:
            return None
    except:
        print (f"error opening {FILENAME}")
        return None

def add_user(user):
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow([user.get_user_name(), user.get_user_id()])


    except:
        print(f"error opening {FILENAME}")
