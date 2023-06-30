from tkinter import Tk, Label, Button
from controllers.islands_controller import IslandsController
from Services import IslandsService
from controllers.storage_controller import Storage
from Services import StorageService



class AdminService:

    island_cont = IslandsController()
    storage_cont = Storage()

def create_admin_interface():
    global main_screen
    admin_serv = AdminService
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Admin")
    Label(main_screen, text="scegli un opzione", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(main_screen, text="Attiva Macchine", height="2", width="30",
           command=admin_serv.island_cont.esegui_richieste()).pack()
    Label(text="").pack()
    tipo = StringVar
    tipo_info = tipo.get()
    tipo_info = Entry(main_screen, textvariable=tipo)
    tipo_info.pack()
    Button(main_screen, text="Visualizza Magazzino", height="2", width="30",
           command=admin_serv.storage_cont.get_magazzino()).pack()
    Label(text="").pack()
    main_screen.mainloop()


create_island_interface()