import hashlib


class User:
    def __init__(self, name, role, password):
        self.__name = name
        self.__password = hashlib.sha256(password.encode()).hexdigest()
        self.__role = role

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def check_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, password):
        self.__password = hashlib.sha256(password.encode()).hexdigest()
