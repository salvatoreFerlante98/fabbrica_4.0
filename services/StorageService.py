import PySimpleGUI as sg
from controllers.StorageController import StorageController


class StorageService:
    storage_cont = StorageController()

    def __init__(self, storage_controller: StorageController):
        self.storage_controller = storage_controller
        self.plastica = self.storage_controller['plastica'].value
        self.metallo = self.storage_controller['metallo'].value
        self.cartucce = self.storage_controller['cartucce'].value
        self.punte = self.storage_controller['punte'].value
        self.tappi = self.storage_controller['tappi'].value
        self.astucci = self.storage_controller['astucci'].value
        self.penne = self.storage_controller['penne'].value

    def aggiorna_liste(self):
        self.plastica = self.storage_controller['plastica'].value
        self.metallo = self.storage_controller['metallo'].value
        self.cartucce = self.storage_controller['cartucce'].value
        self.punte = self.storage_controller['punte'].value
        self.tappi = self.storage_controller['tappi'].value
        self.astucci = self.storage_controller['astucci'].value
        self.penne = self.storage_controller['penne'].value

    def create_storage_interface(self):
        self.aggiorna_liste()
        layout = [
            [sg.Text('Plastica: ' + str(self.plastica), background_color="gray", size=(30, 1))],
            [sg.Text('Metallo: ' + str(self.metallo), background_color="gray", size=(30, 1))],
            [sg.Text('Cartucce: ' + str(self.cartucce), background_color="gray", size=(30, 1))],
            [sg.Text('Punte: ' + str(self.punte), background_color="gray", size=(30, 1))],
            [sg.Text('Tappi: ' + str(self.tappi), background_color="gray", size=(30, 1))],
            [sg.Text('Astucci: ' + str(self.astucci), background_color="gray", size=(30, 1))],
            [sg.Text('Penne: ' + str(self.penne), background_color="gray", size=(30, 1))],
        ]

        window = sg.Window("Magazzino", layout)
        event, _ = window.read()
        window.close()

    def run(self):
        layout = [
            [sg.Text("Scegli un'opzione", background_color="gray", size=(30, 1))],
            [sg.Button("Visualizza Magazzino", size=(30, 2))],
            [sg.Button("Rifornisci", size=(30, 2))]
        ]

        window = sg.Window("Centro Logistico", layout)
        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Visualizza Magazzino":
                self.create_storage_interface()
            elif event == "Rifornisci":
                self.rifornimento_result_screen()

        window.close()

    def rifornimento_result_screen(self):
        result = self.storage_controller.esegui_richiesta()
        if result is True:
            sg.popup("Rifornimento effettuato con successo", title="Successo")
        else:
            sg.popup("Rifornimento non effettuato", title="Errore")
