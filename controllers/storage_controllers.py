from controllers.daos.richiesta import Richiesta
from dataStructures.UnsortedTableMap import UnsortedTableMap
from dataStructures.codaFIFO import ArrayQueue


class Storage:

    def __init__(self):
        self.richieste = ArrayQueue()
        self.storage_map = UnsortedTableMap()
        self.id = 0

    def mapIsEmpty(self):
        return len(self.richieste) == 0

    def creaRichiesta(self, tipo, data, quantita):
        self.id += 1
        richiesta = Richiesta(self.id, tipo, data, quantita)
        self.richieste.enqueue(richiesta)
        return richiesta

    def eseguiRichiesta(self):
        if self.richieste.is_empty():
            return False
        else:
            richiesta = self.richieste.first()
            quantita = self.storage_map[richiesta.getTipo()] + richiesta.getQuantita()
            self.storage_map[richiesta.getTipo()] = quantita
            self.richieste.dequeue()
            return True

    def usaPezzo(self, tipo, quantita):
        if self.storage_map[tipo] - quantita < 0:
            return False
        else:
            self.storage_map[tipo](tipo, self.storage_map[tipo] - quantita)
            return True

    def getMagazzino(self, nome):
        return self.storage_map[nome]
