from random import randint
from controllers.daos.richiesta import Richiesta
from dataStructures.heap_priority_queue import HeapPriorityQueue
from dataStructures.lista_posizionale import PositionalList
from daos.isola import Isola


class IslandsController:

    def __init__(self, penne):
        self._penne = penne
        self._id = 0
        self._richieste = HeapPriorityQueue()
        self.isole = PositionalList()
        isole_tipi = ['punte', 'astucci', 'tappi']
        position = self.isole.add_first(Isola('penne', 1))
        for nome in isole_tipi:
            position = self.isole.add_after(position, Isola(nome, randint(1, 5)))

    def crea_richiesta(self, tipo, data, quantita, penne_prod, quantita_tipo):
        priorita = round((quantita_tipo / (self._penne - penne_prod)) * 4)
        self._id += 1
        self._richieste.add(priorita, Richiesta(self._id, tipo, data, quantita))

    def esegui_richieste(self):
        num_richieste = len(self._richieste)
        while num_richieste != 0:
            richiesta = self._richieste.remove_max()
            isola = self.isole[richiesta[1].get_nome()]
            isola.gestione_macchinari(richiesta[0])
            num_richieste -= 1