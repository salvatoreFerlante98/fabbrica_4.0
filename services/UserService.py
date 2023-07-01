import PySimpleGUI as sg
from services.HRService import HRService
from services.IslandsService import IslandService
from services.AdminService import AdminService
from services.StorageService import StorageService
from controllers.userController import UserController
from controllers.IslandsController import IslandsController
from controllers.StorageController import StorageController

class UserService:
    def __init__(self, island_controller: IslandsController,
                 storage_controller: StorageController,
                 user_controller: UserController):

        self.island_controller = island_controller
        self.storage_controller = storage_controller
        self.user_controller = user_controller

        self.isola_punte_service = IslandService(self.island_controller.isole['punte'],
                                                 self.storage_controller['metallo'],
                                                 self.storage_controller['punte'], self)

        self.isola_tappi_service = IslandService(self.island_controller.isole['tappi'],
                                                 self.storage_controller['plastica'],
                                                 self.storage_controller['tappi'])

        self.isola_astucci_service = IslandService(self.island_controller.isole['astucci'],
                                                   self.storage_controller['plastica'],
                                                   self.storage_controller['astucci'], self)

        self.isola_penne_service = IslandService(self.island_controller.isole['penne'],
                                                 [self.storage_controller['punte'],
                                                  self.storage_controller['tappi'],
                                                  self.storage_controller['astucci'],
                                                  self.storage_controller['cartucce']],
                                                 self.storage_controller['penne'], self)
        self.admin_service = AdminService(self.user_controller, self.island_controller, self.storage_controller, self)
        self.user_controller.add_user('admin', 'nimda', 'admin')

    def login_verify(self, username, password):
        """
        Verifica le credenziali dell'utente durante il login.
        In base al ruolo dell'utente, esegue il servizio corrispondente.
        """
        username1 = username
        password1 = password
        try:
            user = self.user_controller[username1]
            if self.user_controller.login(username1, password1):
                self.login_success()
                role = str(user.get_role())
                if role == 'admin':
                    self.admin_service.run()
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
                elif role == 'penne':
                    self.isola_penne_service.run()
                elif 'risorse_umane' in role:
                    HRService(self.user_controller, self).run()
                elif 'responsabile_logistica' == role:
                    StorageService(self.storage_controller, self).run()
                else:
                    self.user_without_permission()
            else:
                self.password_not_recognized()
        except KeyError:
            self.user_not_found()

    @staticmethod
    def password_not_recognized():
        """
        Mostra una finestra popup con un messaggio di password non riconosciuta.
        """
        layout = [
            [sg.Text("Invalid Password")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    @staticmethod
    def user_not_found():
        """
        Mostra una finestra popup con un messaggio di utente non trovato.
        """
        layout = [
            [sg.Text("Utente non trovato")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    @staticmethod
    def user_without_permission():
        """
        Mostra una finestra popup con un messaggio di utente senza permessi.
        """
        layout = [
            [sg.Text("Questo utente non ha i permessi per operare")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Fail", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    @staticmethod
    def login_success():
        """
        Mostra una finestra popup con un messaggio di login avvenuto con successo.
        """
        layout = [
            [sg.Text("Login Success")],
            [sg.Button("OK", size=(10, 1))]
        ]
        window = sg.Window("Success", layout, size=(150, 100))
        event, _ = window.read()
        window.close()

    def run(self):
        """
        Esegue il programma principale.
        Mostra una finestra con il pulsante di login.
        """
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
        """
        Mostra la finestra di login per inserire nome utente e password.
        """
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
