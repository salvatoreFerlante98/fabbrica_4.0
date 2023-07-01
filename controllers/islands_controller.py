from random import randint
from controllers.daos.richiesta import Richiesta
from dataStructures.lista_posizionale import PositionalList
from dataStructures.coda_conc import LinkedQueue
from controllers.daos.isola import Isola


class IslandsController:

    def __init__(self):
        self._id = 0
        self._richieste = LinkedQueue()
        self.isole = PositionalList()
        isole_tipi = ['punte', 'astucci', 'tappi']
        position = self.isole.add_first(Isola('penne', 1))
        for nome in isole_tipi:
            position = self.isole.add_after(position, Isola(nome, randint(1, 5)))

    def crea_richiesta(self, tipo, quantita):
        self._id += 1
        self._richieste.enqueue(Richiesta(self._id, tipo, quantita))

    def esegui_richieste(self):
        num_richieste = len(self._richieste)
        while num_richieste != 0:
            richiesta = self._richieste.dequeue()
            isola = self.isole[richiesta.tipo]
            isola.gestione_macchinari(richiesta.quantita)
            num_richieste -= 1

    def get_consume(self, tipo):
        isola = self.isole[tipo]
        return isola.get_consumo()
