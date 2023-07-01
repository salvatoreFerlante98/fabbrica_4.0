import PySimpleGUI as sg
from controllers.userController import UserController
from controllers.islands_controller import IslandsController


class AdminService:

    def __init__(self, user_controller: UserController, island_controller: IslandsController):
        self.user_controller = user_controller
        self.island_controller = island_controller

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
        isole = []
        macchinari = []
        for isola in self.island_controller.isole:
            isole.append(isola.get_nome())
            macchinari.append(isola.get_status_macchinari())

        layout = [
            [sg.Text("Macchinari in Lavorazione", background_color="gray", font=("Calibri", 13))],
            [sg.Text(isole[0], size=(30, 6))],
            [sg.Listbox(macchinari[0], size=(30, 6))],
            [sg.Text(isole[1], size=(30, 6))],
            [sg.Listbox(macchinari[1], size=(30, 6))],
            [sg.Text(isole[2], size=(30, 6))],
            [sg.Listbox(macchinari[2], size=(30, 6))],
            [sg.Text(isole[3], size=(30, 6))],
            [sg.Listbox(macchinari[3], size=(30, 6))],
            [sg.Button("Indietro")]
        ]

        window = sg.Window("Admin - Macchinari in Lavorazione", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Indietro":
                break

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
