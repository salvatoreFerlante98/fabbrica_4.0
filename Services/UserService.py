import PySimpleGUI as sg
import schedule
import time
from Services.HRService import HRService
from Services.IslandsService import IslandService
from Services.StorageService import StorageService
from controllers.userController import UserController
from controllers.islands_controller import IslandsController
from controllers.storage_controller import StorageController
from CronJob import Cronjob


class UserService:
    def __init__(self):
        self.island_controller = IslandsController()
        self.storage_controller = StorageController()
        self.user_cont = UserController()
        self.isola_punte_service = IslandService(self.island_controller.isole['punte'],
                                                 self.storage_controller['metallo'])
        self.isola_tappi_service = IslandService(self.island_controller.isole['tappi'],
                                                 self.storage_controller['plastica'])
        self.isola_astucci_service = IslandService(self.island_controller.isole['astucci'],
                                                   self.storage_controller['plastica'])
        self.user_cont.add_user('admin', 'nimda', 'punte')
        cronjob = Cronjob(self.island_controller, self.storage_controller)
        schedule.every(1).seconds.do(cronjob.my_task)


    def login_verify(self, username, password):
        username1 = username
        password1 = password
        try:
            user = self.user_cont[username1]
            if self.user_cont.login(username1, password1):
                self.login_success()
                role = str(user.get_role())
                if role == 'admin':
                    cipolla = 0
                    # AdminService()
                elif role == 'responsabile_macchinari':
                    self.isola_punte_service.run()
                    self.isola_tappi_service.run()
                    self.isola_astucci_service.run()
                elif role == 'punte':
                    self.isola_punte_service.run()
                elif role == 'tappi':
                    self.isola_tappi_service.run()
                elif role == 'astucci':
                    self.isola_astucci_service.run()
                elif 'centro logistico' in role:
                    if role.split()[1] == 'ufficio':
                        HRService()
                    else:
                        StorageService()
            else:
                self.password_not_recognized()
        except KeyError:
            self.user_not_found()

    def password_not_recognized(self):
        layout = [
            [sg.Text("Invalid Password")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    def user_not_found(self):
        layout = [
            [sg.Text("Utente non trovato")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    def login_success(self):
        layout = [
            [sg.Text("Login Success")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Success", layout, size=(150, 100))
        event, _ = window.read()
        window.close()


def main_account_screen():
    layout = [
        [sg.Text("Fabbrica FePa")],
        [sg.Button("Login", size=(10, 1))]
    ]
    window = sg.Window("Main Account Screen", layout)
    event, _ = window.read()
    window.close()
    if event == "Login":
        login_screen()


def login_screen():
    layout = [
        [sg.Text("Inserisci nome e password")],
        [sg.Input(key='-USERNAME-')],
        [sg.Input(key='-PASSWORD-', password_char='*')],
        [sg.Button("Login", size=(10, 1))]
    ]
    window = sg.Window("Login", layout)
    event, values = window.read()
    window.close()
    if event == "Login":
        username = values['-USERNAME-']
        password = values['-PASSWORD-']
        user_service = UserService()
        user_service.login_verify(username, password)


if __name__ == '__main__':
    main_account_screen()
