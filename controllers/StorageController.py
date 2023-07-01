from controllers.daos.richiesta import Richiesta
from data_structures.UnsortedTableMap import UnsortedTableMap
from data_structures.HeapPriorityQueue import HeapPriorityQueue


class StorageController:

    def __init__(self):
        """
        Inizializza un oggetto StorageController.
        Viene inizializzata una coda a priorità per le richieste,
        una mappa non ordinata per il magazzino e vengono aggiunte alcune quantità iniziali per alcuni tipi.
        """
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
        """
        Verifica se la coda delle richieste è vuota.
        Restituisce True se la coda è vuota, altrimenti False.
        """
        return len(self._richieste) == 0

    def crea_richiesta(self, tipo):
        """
        Crea una nuova richiesta per il tipo specificato, utilizzando la priorità corrispondente dal magazzino.
        Assegna un ID incrementale alla richiesta.
        """
        priorita = self._storage_map[tipo]
        self.id += 1
        self._richieste.add(priorita, Richiesta(self.id, tipo, 100))

    def esegui_richiesta(self):
        """
        Esegue la richiesta con la priorità più bassa.
        Aggiorna la quantità corrispondente nel magazzino.
        Restituisce True se la richiesta viene eseguita con successo, altrimenti False se la coda delle richieste è vuota.
        """
        if self._richieste.is_empty():
            return False
        else:
            richiesta = self._richieste.remove_min()
            quantita = self._storage_map[richiesta.get_tipo()] + richiesta.get_quantita()
            self._storage_map[richiesta.get_tipo()] = quantita
            return True

    def spedisci_penne(self, quantita):
        """
        Spedisce una determinata quantità di penne.
        Verifica se il magazzino ha abbastanza penne disponibili per la spedizione.
        Restituisce True se la spedizione viene effettuata con successo, altrimenti False.
        """
        tipo = 'penne'
        if self._storage_map[tipo] - quantita < 0:
            return False
        else:
            self._storage_map[tipo] -= quantita
            return True

    def __getitem__(self, item):
        """
        Restituisce la quantità del tipo specificato nel magazzino.
        """
        return self._storage_map.get_magazzino(item)
