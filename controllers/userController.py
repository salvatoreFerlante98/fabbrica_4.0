from daos.user import User
from dataStructures.probe_hash_map import ProbeHashMap
from daos.permissions import Permissions


class UserController:

    def __init__(self):
        self.__users = ProbeHashMap()
        self.__permission = Permissions()

    def add_user(self, name, age, email, password, role):
        self.__users[name] = User(name, age, email, self.__permission.get_permission(role), password)

    def del_user(self, name):
        del self.__users[name]

    def login(self, name, password):
        if self.__users[name].check_password(password):
            return self.__users[name]
        else:
            return None
        