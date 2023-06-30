from tkinter import Tk, Label, Button, END, Entry, StringVar, Toplevel
from Services.AdminService import AdminService
from Services.HRService import HRService
from Services.IslandsService import IslandService
from Services.StorageService import StorageService
from controllers.userController import UserController


class UserService:
    def __init__(self):
        self.user_cont = UserController()

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        try:
            user = self.user_cont[username1]
            if self.user_cont.login(username1, password1):
                self.login_success()
                role = str(user.get_role())
                if role == 'admin':
                    AdminService()
                elif role == 'responsabile tecnico':
                    IslandService()
                elif 'centro logistico' in role:
                    if role.split()[1] == 'ufficio':
                        HRService()
                    else:
                        StorageService()
            else:
                self.password_not_recognised()
        except KeyError:
            self.user_not_found()

    def login(self):
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

        Button(login_screen, text="Login", width=10, height=1, command=self.login_verify).pack()

    def main_account_screen(self):
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Fabbrica FePa")
        Button(text="Login", height="2", width="30", command=self.login).pack()
        Label(text="").pack()

        main_screen.mainloop()

    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()

    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()

    def delete_login_success(self):
        login_success_screen.destroy()

    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Fail")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="Utente non trovato").pack()
        Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()

    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Fail")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()

    def login_success(self):
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=self.delete_login_success).pack()


user_service = UserService()
user_service.main_account_screen()
