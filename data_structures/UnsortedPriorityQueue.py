from data_structures.empty import Empty
from data_structures.PriorityQueueBase import PriorityQueueBase
from data_structures.PositionalList import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    """
    Coda con priorità min-oriented implementata con una lista non ordinata.
    """

    def __init__(self):
        """
        Crea una coda prioritaria vuota
        """
        self._data = PositionalList()

    def __len__(self):
        """
        Restituisce il num di elementi presenti nella coda prioritaria.
        """
        return len(self._data)

    def add(self, key, value):
        """
        Aggiunge una coppia chiave valore.
        """
        self._data.add_last(self._Item(key, value))  # alla fine della Lista Posizionale

    def _find_min(self):
        """
        Restituisce la Position dell'item con chiave minima
        """
        if self.is_empty():
            raise Empty('La coda prioritaria è vuota')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):
        """
        Restituisce senza rimuovere la tupla KEY-VALUE con chiave minima.
        """
        p = self._find_min()
        item = p.element()
        return item

    def remove_min(self):
        """
        Restituisce e rimuove la tupla KEY-VALUE con chiave minima.
        """
        p = self._find_min()
        item = self._data.delete(p)
        return item

    def _find_max(self):
        """
        Restituisce la Position dell'item con chiave massima.
        """
        if self.is_empty():
            raise Empty('La coda prioritaria è vuota')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() > small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def max(self):
        """
        Restituisce senza rimuovere la tupla KEY-VALUE con chiave minima.
        """
        p = self._find_max()
        item = p.element()
        return item

    def remove_max(self):
        """
        Restituisce e rimuove la tupla KEY-VALUE con chiave minima.
        """
        p = self._find_max()
        item = self._data.delete(p)
        return item._key
