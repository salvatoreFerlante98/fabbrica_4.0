from dataStructures.UnsortedTableMap import UnsortedTableMap
from dataStructures.codaFIFO import ArrayQueue


class Storage:
    class Richiesta:
        __slots__ = 'id_richiesta', 'tipo', 'data', 'quantita'

        def __init__(self, id_richiesta, tipo, data, quantita):
            self.id_richiesta = id_richiesta
            self.tipo = tipo
            self.data = data
            self.quantita = quantita

        def __str__(self):
            return "Richiesta: " + str(self.id_richiesta) + " - " + str(self.tipo) + " - " + str(self.data) + " - " + str(self.quantita) + "\n"

        def getId(self):
            return self.id_richiesta

        def getTipo(self):
            return self.tipo

        def getData(self):
            return self.data

        def getQuantita(self):
            return self.quantita

    def __init__(self):
        self.richieste = ArrayQueue()
        self.storage_map = UnsortedTableMap()
        self.id = 0

    def mapIsEmpty(self):
        return len(self.richieste) == 0

    def creaRichiesta(self, tipo, data, quantita):
        self.id += 1
        richiesta = self.Richiesta(self.id, tipo, data, quantita)
        self.richieste.enqueue(richiesta)
        return richiesta

    def eseguiRichiesta(self):
        if self.richieste.is_empty():
            print("Non ci sono richieste da eseguire")

        else:
            richiesta = self.richieste.first()
            quantita = self.storage_map.__getitem__(richiesta.getTipo()) + richiesta.getQuantita()
            self.storage_map.__setitem__(richiesta.getTipo(), quantita)
            self.richieste.dequeue()
            print("Richiesta eseguita")

    def usaPezzo(self, tipo, quantita):
        if self.storage_map.__getitem__(tipo) - quantita < 0:
            print("Non ci sono abbastanza pezzi")
        else:
            self.storage_map.__setitem__(tipo, self.storage_map.__getitem__(tipo) - quantita)
            print("Pezzi usati")

    def getMagazzino(self):
        return self.storage_map
