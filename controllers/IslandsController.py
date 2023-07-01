from random import randint
from controllers.daos.richiesta import Richiesta
from data_structures.PositionalList import PositionalList
from controllers.daos.isola import Isola
from data_structures.UnsortedPriorityQueue import UnsortedPriorityQueue


class IslandsController:

    def __init__(self):
        """
        Inizializza un oggetto IslandsController.
        Viene inizializzato un contatore per gli ID delle richieste,
        una coda prioritaria per le richieste e una lista posizionale per le isole.
        Vengono create alcune isole di tipo predefinito.
        """
        self._id = 0
        self._richieste = UnsortedPriorityQueue()
        self.isole = PositionalList()
        isole_tipi = ['punte', 'astucci', 'tappi']
        position = self.isole.add_first(Isola('penne', 1))
        for nome in isole_tipi:
            position = self.isole.add_after(position, Isola(nome, randint(1, 5)))

    def crea_richiesta(self, tipo, quantita):
        """
        Crea una nuova richiesta con il tipo e la quantità specificati,
        assegnandole un ID incrementale.
        """
        self._id += 1
        self._richieste.add(Richiesta(self._id, tipo, quantita), quantita)

    def esegui_richieste(self):
        """
        Esegue le richieste presenti nella coda delle richieste.
        Per ogni richiesta, trova l'isola corrispondente al tipo e gestisce i macchinari.
        """
        num_richieste = len(self._richieste)
        while num_richieste != 0:
            richiesta = self._richieste.remove_max()
            isola = self.isole[richiesta.tipo]
            isola.gestione_macchinari(richiesta.quantita)
            num_richieste -= 1

    def get_consume(self, tipo):
        """
        Restituisce il consumo dell'isola corrispondente al tipo specificato.
        """
        isola = self.isole[tipo]
        return isola.get_consumo()
