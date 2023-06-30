import PySimpleGUI as sg
from controllers.storage_controller import Storage


class StorageService:
    storage_cont = Storage()


def create_storage_interface():
    storage_serv = StorageService()
    plastica = storage_serv.storage_cont.get_magazzino('plastica')
    metallo = storage_serv.storage_cont.get_magazzino('metallo')
    cartucce = storage_serv.storage_cont.get_magazzino('cartucce')
    punte = storage_serv.storage_cont.get_magazzino('punte')
    tappi = storage_serv.storage_cont.get_magazzino('tappi')
    astucci = storage_serv.storage_cont.get_magazzino('astucci')
    penne = storage_serv.storage_cont.get_magazzino('penne')

    layout = [
        [sg.Text('Plastica: ' + str(plastica), background_color="gray", size=(30, 1))],
        [sg.Text('Metallo: ' + str(metallo), background_color="gray", size=(30, 1))],
        [sg.Text('Cartucce: ' + str(cartucce), background_color="gray", size=(30, 1))],
        [sg.Text('Punte: ' + str(punte), background_color="gray", size=(30, 1))],
        [sg.Text('Tappi: ' + str(tappi), background_color="gray", size=(30, 1))],
        [sg.Text('Astucci: ' + str(astucci), background_color="gray", size=(30, 1))],
        [sg.Text('Penne: ' + str(penne), background_color="gray", size=(30, 1))],
    ]

    window = sg.Window("Magazzino", layout)
    event, _ = window.read()
    window.close()


def main_logistic_screen():
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
            create_storage_interface()
        elif event == "Rifornisci":
            rifornimento_result_screen()

    window.close()


def rifornimento_result_screen():
    storage_serv = StorageService()
    result = storage_serv.storage_cont.esegui_richiesta()
    if result is True:
        sg.popup("Rifornimento effettuato con successo", title="Successo")
    else:
        sg.popup("Rifornimento non effettuato", title="Errore")


main_logistic_screen()
