import PySimpleGUI
from controllers.StorageController import StorageController

class StorageService:
    storage_cont = StorageController()

    def __init__(self, storage_controller: StorageController):
        """
        Inizializza il servizio di gestione del magazzino utilizzando il controller di storage specificato.
        """
        self.storage_controller = storage_controller
        self.plastica = self.storage_controller['plastica'].value
        self.metallo = self.storage_controller['metallo'].value
        self.cartucce = self.storage_controller['cartucce'].value
        self.punte = self.storage_controller['punte'].value
        self.tappi = self.storage_controller['tappi'].value
        self.astucci = self.storage_controller['astucci'].value
        self.penne = self.storage_controller['penne'].value

    def aggiorna_liste(self):
        """
        Aggiorna i valori delle quantità di materiali nel magazzino.
        """
        self.plastica = self.storage_controller['plastica'].value
        self.metallo = self.storage_controller['metallo'].value
        self.cartucce = self.storage_controller['cartucce'].value
        self.punte = self.storage_controller['punte'].value
        self.tappi = self.storage_controller['tappi'].value
        self.astucci = self.storage_controller['astucci'].value
        self.penne = self.storage_controller['penne'].value

    def create_storage_interface(self):
        """
        Crea un'interfaccia grafica per visualizzare lo stato del magazzino.
        """
        self.aggiorna_liste()
        layout = [
            [PySimpleGUI.Text('Plastica: ' + str(self.plastica), background_color="gray", size=(30, 1))],
            [PySimpleGUI.Text('Metallo: ' + str(self.metallo), background_color="gray", size=(30, 1))],
            [PySimpleGUI.Text('Cartucce: ' + str(self.cartucce), background_color="gray", size=(30, 1))],
            [PySimpleGUI.Text('Punte: ' + str(self.punte), background_color="gray", size=(30, 1))],
            [PySimpleGUI.Text('Tappi: ' + str(self.tappi), background_color="gray", size=(30, 1))],
            [PySimpleGUI.Text('Astucci: ' + str(self.astucci), background_color="gray", size=(30, 1))],
            [PySimpleGUI.Text('Penne: ' + str(self.penne), background_color="gray", size=(30, 1))],
        ]

        window = PySimpleGUI.Window("Magazzino", layout)
        event, _ = window.read()
        window.close()

    def run(self):
        """
        Esegue il servizio di gestione del magazzino.
        Mostra un'interfaccia grafica per scegliere le opzioni disponibili.
        """
        layout = [
            [PySimpleGUI.Text("Scegli un'opzione", background_color="gray", size=(30, 1))],
            [PySimpleGUI.Button("Visualizza Magazzino", size=(30, 2))],
            [PySimpleGUI.Button("Rifornisci", size=(30, 2))]
        ]

        window = PySimpleGUI.Window("Centro Logistico", layout)
        while True:
            event, _ = window.read()
            if event == PySimpleGUI.WINDOW_CLOSED:
                break
            elif event == "Visualizza Magazzino":
                self.create_storage_interface()
            elif event == "Rifornisci":
                self.rifornimento_result_screen()

        window.close()

    def rifornimento_result_screen(self):
        """
        Mostra una finestra popup con il risultato del rifornimento del magazzino.
        """
        result = self.storage_controller.esegui_richiesta()
        if result is True:
            PySimpleGUI.popup("Rifornimento effettuato con successo", title="Successo")
        else:
            PySimpleGUI.popup("Rifornimento non effettuato", title="Errore")
