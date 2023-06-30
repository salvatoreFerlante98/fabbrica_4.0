from tkinter import Tk, Label, Button
from controllers.islands_controller import IslandsController
from Services import IslandsService
from controllers.storage_controller import Storage
from Services import StorageService


class AdminService:
    def ___init___(self):
        self.storage = Storage()
