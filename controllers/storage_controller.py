from controllers.daos.richiesta import Richiesta
from dataStructures.UnsortedTableMap import UnsortedTableMap
from dataStructures.heap_priority_queue import HeapPriorityQueue


class Storage:

    def __init__(self):
        self.richieste = HeapPriorityQueue()
        self.storage_map = UnsortedTableMap()
        self.storage_map['plastica'] = 0
        self.storage_map['metallo'] = 0
        self.storage_map['cartucce'] = 0
        self.storage_map['punte'] = 0
        self.storage_map['tappi'] = 0
        self.storage_map['astucci'] = 0
        self.storage_map['penne'] = 0
        self.id = 0

    def map_is_empty(self):
        return len(self.richieste) == 0

    def crea_richiesta(self, tipo):
        priorita = self.storage_map[tipo]
        self.id += 1
        self.richieste.add(priorita, Richiesta(self.id, tipo, 100))

    def esegui_richiesta(self):
        if self.richieste.is_empty():
            return False
        else:
            richiesta = self.richieste.remove_min()
            quantita = self.storage_map[richiesta.get_tipo()] + richiesta.get_quantita()
            self.storage_map[richiesta.get_tipo()] = quantita
            return True

    def usa_pezzo(self, tipo, quantita):
        if self.storage_map[tipo] - quantita < 0:
            return False
        else:
            self.storage_map[tipo](tipo, self.storage_map[tipo] - quantita)
            return True

    def get_magazzino(self, nome):
        return self.storage_map[nome]
