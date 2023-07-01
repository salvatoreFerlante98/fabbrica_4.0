import PySimpleGUI as sg
from controllers.userController import UserController
from controllers.IslandsController import IslandsController
from services.IslandsService import IslandService
from controllers.StorageController import StorageController


class AdminService:

    def __init__(self, user_controller: UserController, island_controller: IslandsController,
                 storage_controller: StorageController):
        self.user_controller = user_controller
        self.island_controller = island_controller
        self.storage_controller = storage_controller
        self.isola_punte_service = IslandService(self.island_controller.isole['punte'],
                                                 self.storage_controller['metallo'])
        self.isola_tappi_service = IslandService(self.island_controller.isole['tappi'],
                                                 self.storage_controller['plastica'])
        self.isola_astucci_service = IslandService(self.island_controller.isole['astucci'],
                                                   self.storage_controller['plastica'])
        self.isola_penne_service = IslandService(self.island_controller.isole['penne'],
                                                 [self.storage_controller['punte'], self.storage_controller['tappi'],
                                                  self.storage_controller['astucci']])
        self._isole = []
        self._macchinari = []
        for isola in self.island_controller.isole:
            self._isole.append(isola.get_nome())
            self._macchinari.append(isola.get_status_macchinari())

    def get_user_list(self):
        user_list = []
        for user in self.user_controller:
            user_list.append(user)
        return user_list

    def view_user_list(self):
        user_list = self.get_user_list()

        layout = [
            [sg.Text("Lista Utenti", background_color="gray", font=("Calibri", 13))],
            [sg.Listbox(user_list, size=(30, 6))],
            [sg.Button("Indietro")]
        ]

        window = sg.Window("Admin - Lista Utenti", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Indietro":
                break

        window.close()

    def view_machines_in_progress(self):

        layout = [
            [sg.Text("Macchinari in Lavorazione", background_color="gray", font=("Calibri", 13))],

            [sg.Text(self._isole[0])],
            [sg.Listbox(self._macchinari[0], size=(30, 6))],
            [sg.Button("isola_" + self._isole[0])],

            [sg.Text(self._isole[1])],
            [sg.Listbox(self._macchinari[1], size=(30, 6))],
            [sg.Button("isola_" + self._isole[1])],

            [sg.Text(self._isole[2])],
            [sg.Listbox(self._macchinari[2], size=(30, 6))],
            [sg.Button("isola_" + self._isole[2])],

            [sg.Text(self._isole[3])],
            [sg.Listbox(self._macchinari[3], size=(30, 6))],
            [sg.Button("isola_" + self._isole[3])],

            [sg.Button("Indietro")]
        ]

        window = sg.Window("Admin - Macchinari in Lavorazione", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Indietro":
                break

            if "isola_" in event:
                isola = event.split("_")[1]
                if isola == "punte":
                    self.isola_punte_service.run()
                if isola == "tappi":
                    self.isola_tappi_service.run()
                if isola == "astucci":
                    self.isola_astucci_service.run()
                if isola == "penne":
                    self.isola_penne_service.run()


        window.close()

    def run(self):
        layout = [
            [sg.Text("Scegli un'opzione", background_color="gray", size=(30, 2), font=("Calibri", 13))],
            [sg.Button("Visualizza Lista Utenti", size=(30, 2))],
            [sg.Button("Visualizza Macchinari in Lavorazione", size=(30, 2))],
            [sg.Button("Esci")]
        ]

        window = sg.Window("Admin", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Esci":
                break

            if event == "Visualizza Lista Utenti":
                self.view_user_list()

            if event == "Visualizza Macchinari in Lavorazione":
                self.view_machines_in_progress()

        window.close()
