from controllers.daos.richiesta import Richiesta
from dataStructures.UnsortedTableMap import UnsortedTableMap
from dataStructures.heap_priority_queue import HeapPriorityQueue


class Storage:

    def __init__(self):
        self._richieste = HeapPriorityQueue()
        self._storage_map = UnsortedTableMap()
        self._storage_map['plastica'] = 100
        self._storage_map['metallo'] = 100
        self._storage_map['cartucce'] = 100
        self._storage_map['punte'] = 100
        self._storage_map['tappi'] = 100
        self._storage_map['astucci'] = 100
        self._storage_map['penne'] = 100
        self.id = 0

    def map_is_empty(self):
        return len(self._richieste) == 0

    def crea_richiesta(self, tipo):
        priorita = self._storage_map[tipo]
        self.id += 1
        self._richieste.add(priorita, Richiesta(self.id, tipo, 100))

    def esegui_richiesta(self):
        if self._richieste.is_empty():
            return False
        else:
            richiesta = self._richieste.remove_min()
            quantita = self._storage_map[richiesta.get_tipo()] + richiesta.get_quantita()
            self._storage_map[richiesta.get_tipo()] = quantita
            return True

    def usa_pezzo(self, tipo, quantita):
        if self._storage_map[tipo] - quantita < 0:
            return False
        else:
            self._storage_map[tipo](tipo, self._storage_map[tipo] - quantita)
            return True

    def get_magazzino(self, nome):
        return self._storage_map[nome]
