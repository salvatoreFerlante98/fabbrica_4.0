import PySimpleGUI as sg
from controllers.userController import UserController

class HRService:
    def __init__(self, user_controller: UserController, user_service):
        """
        Inizializza il servizio HR con il controller degli utenti.
        """
        self.user_service = user_service
        self.user_controller = user_controller

    def delete_user(self, username):
        """
        Elimina un utente dal sistema.
        Restituisce True se l'eliminazione è avvenuta con successo, altrimenti False.
        """
        try:
            self.user_controller.del_user(username)
            return True
        except KeyError:
            return False

    def register_user(self, username, password, role):
        """
        Registra un nuovo utente nel sistema.
        Restituisce True se la registrazione è avvenuta con successo.
        """
        self.user_controller.add_user(username, password, role)
        return True

    def register(self):
        """
        Mostra una finestra per registrare un nuovo utente.
        """
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
        """
        Mostra una finestra per eliminare un utente dal sistema.
        """
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
        """
        Esegue il servizio HR.
        Mostra un'interfaccia grafica con diverse opzioni per la gestione degli utenti.
        """
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
                self.user_service.run()
                break

            if event == "Crea Utente":
                self.register()

            if event == "Elimina Utente":
                self.delete()

        window.close()
