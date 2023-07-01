from controllers.daos.user import User
from dataStructures.probe_hash_map import ProbeHashMap
from controllers.daos.permissions import Permissions


class UserController:

    def __init__(self):
        self._users = ProbeHashMap()
        self.__permission = Permissions()

    def add_user(self, name, password, role):
        self._users[name] = User(name, self.__permission.get_permission(role), password)

    def del_user(self, name):
        del self._users[name]

    def __str__(self):
        return str(self._users)

    def login(self, name, password):
        if self._users[name].check_password(password):
            return self._users[name]
        else:
            return None

    def __getitem__(self, item):
        return self._users[item]

    def __iter__(self):
        for user in self._users:
            yield user
