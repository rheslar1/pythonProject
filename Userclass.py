"""
This module contains the class definition for a user
"""
from dataclasses import dataclass


def create_user(user_name, user_id):
    user = User(user_name, user_id)
    return user


@dataclass
class User:
    _user_name:str = ""
    _user_id:int = 0
    _internal_dict = []
    def __init__(self, username, userid):
        self._user_name = username
        self._user_id = userid
        self._internal_dict.append(self)

    def __iter__(self):  # iterate over all keys
        return self._internal_dict

    def __hash__(self):
        return hash(self._internal_dict.__hash__)

    def __eq__(self, other):
        return self._user_name.lower() == other.get_user_name().lower()

    def __ne__(self, other):
        return not self._user_name.lower() == other.get_user_name().lower()

    def get_user_name(self):
        return self._user_name

    def get_user_id(self):
        return self._user_id

    def set_user_name(self, user_name):
            self._user_name = user_name

    def set_user_id(self, user_id):
        self._user_id = user_id