import PySimpleGUI as sg
from controllers.userController import UserController


class HRService:

    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller

    def delete_user(self, username):
        try:
            self.user_controller.del_user(username)
            return True
        except KeyError:
            return False

    def register_user(self, username, password, role):
        self.user_controller.add_user(username, password, role)
        return True

    def register(self):
        layout = [
            [sg.Text("Compilare i seguenti campi", background_color="gray")],
            [sg.Text("Username * "), sg.Input(key="-USERNAME-")],
            [sg.Text("Password * "), sg.Input(key="-PASSWORD-", password_char="*")],
            [sg.Text("Ruolo * "), sg.Input(key="-ROLE-")],
            [sg.Button("Registra Utente", button_color="green"), sg.Button("Indietro")]
        ]

        window = sg.Window("Registra nuovo utente", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Indietro":
                break

            if event == "Registra Utente":
                username = values["-USERNAME-"]
                password = values["-PASSWORD-"]
                role = values["-ROLE-"]
                success = self.register_user(username, password, role)
                if success:
                    sg.popup("Registrazione effettuata con successo")
                else:
                    sg.popup("Errore durante la registrazione")

                break

        window.close()

    def delete(self):
        layout = [
            [sg.Text("Compilare i seguenti campi", background_color="gray")],
            [sg.Text("Username * "), sg.Input(key="-USERNAME-")],
            [sg.Button("Elimina Utente", button_color="green"), sg.Button("Indietro")]
        ]

        window = sg.Window("Elimina utente", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Indietro":
                break

            if event == "Elimina Utente":
                username = values["-USERNAME-"]
                success = self.delete_user(username)
                if success:
                    sg.popup("Eliminazione effettuata con successo")
                else:
                    sg.popup("Utente non trovato")

                break

        window.close()

    def run(self):
        layout = [
            [sg.Text("Scegli un'opzione", background_color="gray", size=(30, 2), font=("Calibri", 13))],
            [sg.Button("Crea Utente", size=(30, 2))],
            [sg.Button("Elimina Utente", size=(30, 2))],
            [sg.Button("Esci")]
        ]

        window = sg.Window("Risorse Umane", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Esci":
                break

            if event == "Crea Utente":
                self.register()

            if event == "Elimina Utente":
                self.delete()

        window.close()
