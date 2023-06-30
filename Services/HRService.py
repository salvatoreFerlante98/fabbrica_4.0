from tkinter import Tk, Label, Button, END, Entry, StringVar, Toplevel
from controllers.userController import UserController


class UserService:
    user_cont = UserController()

    def delete_user(self):
        username_info = username.get()

        try:
            self.user_cont.del_user(username_info)
            Label(delete_screen, text="Eliminazione effettuata con successo", fg="green", font=("calibri", 11)).pack()
        except KeyError:
            Label(delete_screen, text="Utente non trovato", fg="red", font=("calibri", 11)).pack()

        username_entry.delete(0, END)


    def register_user(self):
        username_info = username.get()
        password_info = password.get()
        role_info = ruolo.get()

        self.user_cont.add_user(username_info, password_info, role_info)

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(register_screen, text="Registrazione effettuata con successo", fg="green", font=("calibri", 11)).pack()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Registra nuovo utente")
    register_screen.geometry("300x250")

    global username
    global password
    global ruolo
    global username_entry
    global password_entry
    global role_entry
    username = StringVar()
    password = StringVar()
    ruolo = StringVar()

    Label(register_screen, text="Compilare i seguenti campi", bg="gray").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    role_lable = Label(register_screen, text="Ruolo * ")
    role_lable.pack()
    role_entry = Entry(register_screen, textvariable=ruolo)
    role_entry.pack()
    Label(register_screen, text="").pack()

    # Modifica: crea un'istanza di UserService e chiama il metodo register_user su di essa
    user_service = UserService()
    Button(register_screen, text="Registra Utente", width=10, height=1, bg="green",
           command=user_service.register_user).pack()

    register_screen.mainloop()


def delete():
    global delete_screen
    delete_screen = Toplevel(main_screen)
    delete_screen.title("Elimina utente")
    delete_screen.geometry("300x250")

    global username
    global username_entry
    username = StringVar()

    Label(delete_screen, text="Compilare i seguenti campi", bg="gray").pack()
    Label(delete_screen, text="").pack()
    username_lable = Label(delete_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(delete_screen, textvariable=username)
    username_entry.pack()

    # Modifica: crea un'istanza di UserService e chiama il metodo register_user su di essa
    user_service = UserService()
    Button(delete_screen, text="Elimina Utente", width=10, height=1, bg="green",
           command=user_service.delete_user).pack()

    delete_screen.mainloop()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Risorse Umane")
    Label(text="scegli un opzione", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Crea Utente", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Elimina Utente", height="2", width="30", command=delete).pack()

    main_screen.mainloop()


main_account_screen()
