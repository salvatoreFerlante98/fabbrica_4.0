from controllers.daos.user import User
from dataStructures.probe_hash_map import ProbeHashMap
from controllers.daos.permissions import Permissions


class UserController:

    def __init__(self):
        self.__users = ProbeHashMap()
        self.__permission = Permissions()

    def add_user(self, name, password, role):
        self.__users[name] = User(name, self.__permission.get_permission(role), password)

    def del_user(self, name):
        del self.__users[name]

    def login(self, name, password):
        if self.__users[name].check_password(password):
            return self.__users[name]
        else:
            return None

    def __getitem__(self, item):
        return self.__users[item]
