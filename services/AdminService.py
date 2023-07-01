import PySimpleGUI as sg
from controllers.userController import UserController
from controllers.IslandsController import IslandsController
from services.IslandsService import IslandService
from controllers.StorageController import StorageController
from services.HRService import HRService
from services.StorageService import StorageService

class AdminService:
    def __init__(self, user_controller: UserController,
                 island_controller: IslandsController,
                 storage_controller: StorageController,
                 user_service):
        """
        Inizializza il servizio Admin con i controller e i servizi necessari.
        """
        self.user_controller = user_controller
        self.island_controller = island_controller
        self.storage_controller = storage_controller
        self.user_service = user_service

        self.isola_punte_service = IslandService(self.island_controller.isole['punte'],
                                                 self.storage_controller['metallo'],
                                                 self.storage_controller['punte'], self)

        self.isola_tappi_service = IslandService(self.island_controller.isole['tappi'],
                                                 self.storage_controller['plastica'],
                                                 self.storage_controller['tappi'], self)

        self.isola_astucci_service = IslandService(self.island_controller.isole['astucci'],
                                                   self.storage_controller['plastica'],
                                                   self.storage_controller['astucci'], self)

        self.isola_penne_service = IslandService(self.island_controller.isole['penne'],
                                                 [self.storage_controller['punte'],
                                                  self.storage_controller['tappi'],
                                                  self.storage_controller['astucci'],
                                                  self.storage_controller['cartucce']],
                                                 self.storage_controller['penne'], self)
        self._isole = []
        self._macchinari = []
        self.aggiorna_liste()

    def aggiorna_liste(self):
        """
        Aggiorna le liste delle isole e dei macchinari.
        """
        self._isole = []
        self._macchinari = []
        for isola in self.island_controller.isole:
            self._isole.append(isola.get_nome())
            self._macchinari.append(isola.get_status_macchinari())

    def get_user_list(self):
        """
        Restituisce la lista degli utenti.
        """
        user_list = []
        for user in self.user_controller:
            user_list.append(user)
        return user_list

    def view_user_list(self):
        """
        Visualizza la lista degli utenti in una finestra.
        """
        user_list = self.get_user_list()

        layout = [
            [sg.Text("Lista Utenti", background_color="gray", font=("Calibri", 13))],
            [sg.Listbox(user_list, size=(30, 6))],
            [sg.Button("Edit_Users")],
            [sg.Button("Indietro")]
        ]

        window = sg.Window("Admin - Lista Utenti", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Indietro":
                break

            if event == "Edit_Users":
                HRService(self.user_controller, self).run()

            window.refresh()

        window.close()

    def view_machines_in_progress(self):
        """
        Visualizza lo stato dei macchinari in lavorazione per ogni isola in una finestra.
        """
        self.aggiorna_liste()
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
            self.aggiorna_liste()

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
            window.refresh()

        window.close()

    def run(self):
        """
        Esegue il servizio Admin.
        Mostra un'interfaccia grafica con diverse opzioni per l'amministratore.
        """
        layout = [
            [sg.Text("Scegli un'opzione", background_color="gray", size=(30, 2), font=("Calibri", 13))],
            [sg.Button("Visualizza Lista Utenti", size=(30, 2))],
            [sg.Button("Visualizza Macchinari in Lavorazione", size=(30, 2))],
            [sg.Button("Visualizza stato magazzino", size=(30, 2))],
            [sg.Button("Esci")]
        ]

        window = sg.Window("Admin", layout)

        while True:
            event, values = window.read()
            self.aggiorna_liste()

            if event == sg.WINDOW_CLOSED or event == "Esci":
                self.user_service.run()
                break

            if event == "Visualizza Lista Utenti":
                self.view_user_list()

            if event == "Visualizza Macchinari in Lavorazione":
                self.view_machines_in_progress()

            if event == "Visualizza stato magazzino":
                StorageService(self.storage_controller, self).run()

            window.refresh()
        window.close()
