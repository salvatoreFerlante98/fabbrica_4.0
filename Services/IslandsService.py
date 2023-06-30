from tkinter import *
from controllers.islands_controller import IslandsController


class IslandsService:

    island_cont = IslandsController()


def create_island_interface():
    global main_screen
    island_serv = IslandsService
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Isola")
    Label(main_screen, text="scegli un opzione", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(main_screen, text="Attiva Macchine", height="2", width="30",
           command=island_serv.island_cont.esegui_richieste()).pack()
    Label(text="").pack()
    main_screen.mainloop()


create_island_interface()
