import PySimpleGUI as sg
from Services.HRService import HRService
from Services.IslandsService import IslandService
from Services.AdminService import AdminService
from Services.StorageService import StorageService
from controllers.userController import UserController
from controllers.IslandsController import IslandsController
from controllers.StorageController import StorageController
from CronJob import Cronjob


class UserService:
    def __init__(self, island_controller: IslandsController, storage_controller: StorageController, user_controller: UserController):
        self.island_controller = island_controller
        self.storage_controller = storage_controller
        self.user_controller = user_controller
        self.isola_punte_service = IslandService(self.island_controller.isole['punte'],
                                                 self.storage_controller['metallo'])
        self.isola_tappi_service = IslandService(self.island_controller.isole['tappi'],
                                                 self.storage_controller['plastica'])
        self.isola_astucci_service = IslandService(self.island_controller.isole['astucci'],
                                                   self.storage_controller['plastica'])
        self.admin_service = AdminService(self.user_controller, self.island_controller)
        self.user_controller.add_user('admin', 'nimda', 'admin')

    def login_verify(self, username, password):
        username1 = username
        password1 = password
        try:
            user = self.user_controller[username1]
            if self.user_controller.login(username1, password1):
                self.login_success()
                role = str(user.get_role())
                if role == 'admin':
                    self.admin_service.run()  # Call 'run' method on 'admin_service' instance
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
                        HRService().run()  # Call 'run' method on 'HRService' instance
                    else:
                        StorageService().run()  # Call 'run' method on 'StorageService' instance
            else:
                self.password_not_recognized()
        except KeyError:
            self.user_not_found()

    @staticmethod
    def password_not_recognized():
        layout = [
            [sg.Text("Invalid Password")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    @staticmethod
    def user_not_found():
        layout = [
            [sg.Text("Utente non trovato")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    @staticmethod
    def login_success():
        layout = [
            [sg.Text("Login Success")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Success", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    def run(self):
        layout = [
            [sg.Text("Fabbrica FePa")],
            [sg.Button("Login", size=(10, 1))]
        ]
        window = sg.Window("Main Account Screen", layout)
        event, _ = window.read()
        window.close()
        if event == "Login":
            self.login_screen()

    def login_screen(self):
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
            self.login_verify(username, password)
