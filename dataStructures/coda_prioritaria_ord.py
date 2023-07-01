from empty import Empty
from coda_prioritaria_base import PriorityQueueBase
from lista_posizionale import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    """
    Coda prioritaria min-oriented implementata con una lista ordinata.
    """

    def __init__(self):
        """
        Crea una coda prio vuota
        """
        self._data = PositionalList()

    def __len__(self):
        """
        Restituisce il numero di elementi presenti nella coda prioritaria.
        """
        return len(self._data)

    def add(self, key, value: object):
        """
        Aggiunge una coppia KEY-VALUE nella coda prioritaria.
        """
        new = self._Item(key, value)  # Crea una nuova istanza di _Item
        walk = self._data.last()  # "Cammina" all'indietro per cercare la chiave più piccola
        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)  # la nuova chiave è la più piccola (in testa alla lista)
        else:
            self._data.add_after(walk, new)  # new inserito dopo walk

    def min(self):
        """
        Restituisce ma non elimina la coppia (KEY-VALUE) con chiave minima.
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        p = self._data.first()
        item = p.element()
        return (item._key, item.value)

    def remove_min(self):
        """
        Rimuove la coppia (KEY-VALUE) con chiave minore (prio max) e restituisce l'elemento
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        item = self._data.delete(self._data.first())
        return (item._key, item.value)
