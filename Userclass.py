"""
This module contains the class definition for a user
"""
from dataclasses import dataclass


def create_user(user_name, user_id):
    user = User(user_name, user_id)
    return user


@dataclass
class User:
    __user_name:str = ""
    __user_id:int = 0

    def __init__(self, username, userid):
        self.__user_name = username
        self.__user_id = userid

    def get_user_name(self):
        return self.__user_name

    def get_user_id(self):
        return self.__user_id

    def set_user_name(self, user_name):
            self.__user_name = user_name

    def set_user_id(self, user_id):
        self.__user_id = user_id