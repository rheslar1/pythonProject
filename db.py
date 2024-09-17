import csv
import os
from Userclass import User

FILENAME = "users.csv"

def get_users():
    users = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # convert row to Product object
                user = User(str(row[0]), int(row[1]))
            users.append(user)
        return users
    else:
        return None

