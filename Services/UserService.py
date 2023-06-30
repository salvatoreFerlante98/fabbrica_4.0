from tkinter import *
from Services.IslandsService import IslandsService
from controllers.userController import UserController


class UserService:
    user_cont = UserController()

    def register_user(self):
        username_info = username.get()
        password_info = password.get()
        role_info = ruolo.get()

        self.user_cont.add_user(username_info, password_info, role_info)

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(register_screen, text="Registrazione effettuata con successo", fg="green", font=("calibri", 11)).pack()

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        try:
            user = self.user_cont[username1]
            if self.user_cont.login(username1, password1):
                login_sucess()
                role = str(user.get_role())
                if role == 'admin':
                    AdminService()
                elif role == 'responsabile tecnico':
                    IslandsService()
                elif 'centro logistico' in role:
                    if role.split()[1] == 'ufficio':
                        OfficeService()
                    else:
                        StorageService()
            else:
                password_not_recognised()
        except KeyError:
            user_not_found()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Inserisci nome e password").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()

    # Modifica: crea un'istanza di UserService e chiama il metodo login_verify su di essa
    user_service = UserService()
    Button(login_screen, text="Login", width=10, height=1, command=user_service.login_verify).pack()


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


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Fabbrica FePa")
    Label(text="scegli un opzione", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_login_success():
    login_success_screen.destroy()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Fail")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Utente non trovato").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Fail")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


main_account_screen()
