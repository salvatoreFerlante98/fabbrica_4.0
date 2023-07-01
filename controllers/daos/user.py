import hashlib


class User:
    def __init__(self, name, role, password):
        """
        Inizializza un oggetto User con un nome, un ruolo e una password specificati.
        La password viene criptata utilizzando l'algoritmo SHA-256.
        """
        self.__name = name
        self.__password = hashlib.sha256(password.encode()).hexdigest()
        self.__role = role

    def get_name(self):
        """
        Restituisce il nome dell'utente.
        """
        return self.__name

    def set_name(self, name):
        """
        Imposta il nome dell'utente.
        """
        self.__name = name

    def get_role(self):
        """
        Restituisce il ruolo dell'utente.
        """
        return self.__role

    def set_role(self, role):
        """
        Imposta il ruolo dell'utente.
        """
        self.__role = role

    def check_password(self, password):
        """
        Verifica se la password specificata corrisponde alla password dell'utente.
        Restituisce True se le password corrispondono, altrimenti False.
        """
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, password):
        """
        Imposta la password dell'utente.
        La nuova password viene criptata utilizzando l'algoritmo SHA-256.
        """
        self.__password = hashlib.sha256(password.encode()).hexdigest()
