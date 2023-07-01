import PySimpleGUI as sg
from controllers.userController import UserController
from controllers.IslandsController import IslandsController


class AdminService:
    user_cont = UserController()
    machine_cont = IslandsController()

    def get_user_list(self):
        return str(self.user_cont)

    def get_machines_in_progress(self):
        for isola in self.machine_cont.isole:
            return isola.get_status_macchinari()


def view_user_list():
    admin_service = AdminService()
    user_list = admin_service.get_user_list()

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


def view_machines_in_progress():
    admin_service = AdminService()
    machines_in_progress = admin_service.get_machines_in_progress()

    layout = [
        [sg.Text("Macchinari in Lavorazione", background_color="gray", font=("Calibri", 13))],
        [sg.Listbox(machines_in_progress, size=(30, 6))],
        [sg.Button("Indietro")]
    ]

    window = sg.Window("Admin - Macchinari in Lavorazione", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Indietro":
            break

    window.close()


def main_admin_screen():
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
            view_user_list()

        if event == "Visualizza Macchinari in Lavorazione":
            view_machines_in_progress()

    window.close()


main_admin_screen()
