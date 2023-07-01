from controllers.daos.user import User
from data_structures.ProbeHashMap import ProbeHashMap
from controllers.daos.permissions import Permissions


class UserController:

    def __init__(self):
        """
        Inizializza un oggetto UserController.
        Viene inizializzata una hashmap per gli utenti e viene istanziato l'oggetto Permissions per gestire i permessi.
        """
        self._users = ProbeHashMap()
        self.__permission = Permissions()

    def add_user(self, name, password, role):
        """
        Aggiunge un nuovo utente con il nome, la password e il ruolo specificati.
        Il ruolo viene ottenuto dai permessi corrispondenti attraverso l'oggetto Permissions.
        """
        self._users[name] = User(name, self.__permission.get_permission(role), password)

    def del_user(self, name):
        """
        Rimuove l'utente con il nome specificato dalla mappa degli utenti.
        """
        del self._users[name]

    def __str__(self):
        """
        Restituisce una rappresentazione in formato stringa degli utenti presenti nella mappa.
        """
        return str(self._users)

    def login(self, name, password):
        """
        Effettua il login per l'utente con il nome e la password specificati.
        Verifica se la password corrisponde alla password memorizzata per l'utente.
        Restituisce l'oggetto User se il login ha successo, altrimenti restituisce None.
        """
        if self._users[name].check_password(password):
            return self._users[name]
        else:
            return None

    def __getitem__(self, item):
        """
        Restituisce l'oggetto User corrispondente al nome specificato.
        """
        return self._users[item]

    def __iter__(self):
        for user in self._users:
            yield user
