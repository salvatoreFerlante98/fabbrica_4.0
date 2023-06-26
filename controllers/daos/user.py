import hashlib


class User:
    def __init__(self, name, age, email, role, password):
        self.__name = name
        self.__age = age
        self.__password = hashlib.sha256(password.encode()).hexdigest()
        self.__email = email
        self.__role = role

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def check_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, password):
        self.__password = hashlib.sha256(password.encode()).hexdigest()
