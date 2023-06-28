from controllers.daos.richiesta import Richiesta
from dataStructures.UnsortedTableMap import UnsortedTableMap
from dataStructures.codaFIFO import ArrayQueue


class Storage:

    def __init__(self):
        self._richieste = ArrayQueue()
        self._storage_map = UnsortedTableMap()
        self._storage_map['plastica'] = 0
        self._storage_map['metallo'] = 0
        self._storage_map['cartucce'] = 0
        self._storage_map['punte'] = 0
        self._storage_map['tappi'] = 0
        self._storage_map['astucci'] = 0
        self._storage_map['penne'] = 0
        self.id = 0

    def map_is_empty(self):
        return len(self._richieste) == 0

    def crea_richiesta(self, tipo, data, quantita):
        self.id += 1
        richiesta = Richiesta(self.id, tipo, data, quantita)
        self._richieste.enqueue(richiesta)
        return richiesta

    def esegui_richiesta(self):
        if self._richieste.is_empty():
            return False
        else:
            richiesta = self._richieste.first()
            quantita = self._storage_map[richiesta.get_tipo()] + richiesta.get_quantita()
            self._storage_map[richiesta.get_tipo()] = quantita
            self._richieste.dequeue()
            return True

    def usa_pezzo(self, tipo, quantita):
        if self._storage_map[tipo] - quantita < 0:
            return False
        else:
            self._storage_map[tipo](tipo, self._storage_map[tipo] - quantita)
            return True

    def get_magazzino(self, nome):
        return self._storage_map[nome]
