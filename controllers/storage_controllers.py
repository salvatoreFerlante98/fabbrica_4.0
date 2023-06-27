from controllers.daos.richiesta import Richiesta
from dataStructures.UnsortedTableMap import UnsortedTableMap
from dataStructures.codaFIFO import ArrayQueue


class Storage:

    def __init__(self):
        self.richieste = ArrayQueue()
        self.storage_map = UnsortedTableMap()
        self.id = 0

    def map_is_empty(self):
        return len(self.richieste) == 0

    def crea_richiesta(self, tipo, data, quantita):
        self.id += 1
        richiesta = Richiesta(self.id, tipo, data, quantita)
        self.richieste.enqueue(richiesta)
        return richiesta

    def esegui_richiesta(self):
        if self.richieste.is_empty():
            return False
        else:
            richiesta = self.richieste.first()
            quantita = self.storage_map[richiesta.get_tipo()] + richiesta.get_quantita()
            self.storage_map[richiesta.get_tipo()] = quantita
            self.richieste.dequeue()
            return True

    def usa_pezzo(self, tipo, quantita):
        if self.storage_map[tipo] - quantita < 0:
            return False
        else:
            self.storage_map[tipo](tipo, self.storage_map[tipo] - quantita)
            return True

    def get_magazzino(self, nome):
        return self.storage_map[nome]
