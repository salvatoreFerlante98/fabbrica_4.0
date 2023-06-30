from tkinter import Tk, Label, Button, Toplevel

from controllers.storage_controller import Storage


class StorageService:
    storage_cont = Storage()


def create_storage_interface():
    global storage_screen
    storage_serv = StorageService()
    storage_screen = Toplevel(logistic_screen)
    storage_screen.geometry("300x250")
    storage_screen.title("Magazzino")
    Label(storage_screen, text='Plastica: ' + str(storage_serv.storage_cont.get_magazzino('plastica')), bg="gray",
          width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(storage_screen, text='Metallo: ' + str(storage_serv.storage_cont.get_magazzino('metallo')), bg="gray",
          width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(storage_screen, text='Cartucce: ' + str(storage_serv.storage_cont.get_magazzino('cartucce')), bg="gray",
          width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(storage_screen, text='Punte: ' + str(storage_serv.storage_cont.get_magazzino('punte')), bg="gray", width="300",
          height="2",
          font=("Calibri", 13)).pack()
    Label(storage_screen, text='Tappi: ' + str(storage_serv.storage_cont.get_magazzino('tappi')), bg="gray", width="300",
          height="2",
          font=("Calibri", 13)).pack()
    Label(storage_screen, text='Astucci: ' + str(storage_serv.storage_cont.get_magazzino('astucci')), bg="gray",
          width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(storage_screen, text='Penne: ' + str(storage_serv.storage_cont.get_magazzino('penne')), bg="gray", width="300",
          height="2",
          font=("Calibri", 13)).pack()
    Label(text="").pack()
    storage_screen.mainloop()


def main_logistic_screen():
    global logistic_screen
    logistic_screen = Tk()
    logistic_screen.geometry("300x250")
    logistic_screen.title("Centro Logistico")
    Label(text="scegli un opzione", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Visualizza Magazzino", height="2", width="30", command=create_storage_interface).pack()
    Label(text="").pack()
    Button(text="Rifornisci", height="2", width="30", command=rifornimento_result_screen).pack()
    Button(text="Crea richista penne", height="2", width="30", command=richiesta_penne_screen).pack()
    logistic_screen.mainloop()


def rifornimento_result_screen():
    storage_serv = StorageService()
    if storage_serv.storage_cont.esegui_richiesta() is True:
        Label(logistic_screen, text="Rifornimento effettuato con successo", fg="green", font=("calibri", 11)).pack()
    else:
        Label(logistic_screen, text="Rifornimento non effettuata", fg="green", font=("calibri", 11)).pack()


main_logistic_screen()
