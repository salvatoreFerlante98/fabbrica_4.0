from dataStructures.empty import Empty
from dataStructures.coda_prioritaria_base import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """
    Coda con priorità implementata con un heap binario
    """

    # ------------------------------------------ Metodi non pubblici ---------------------------------------------------
    def _parent(self, j):
        """
        Per accedere al genitore
        """
        return (j - 1) // 2

    def _left(self, j):
        """
        Per accedere al figlio sinistro
        """
        return 2 * j + 1

    def _right(self, j):
        """
        Per accedere al figlio destro
        """
        return 2 * j + 2

    def _has_left(self, j):
        """
        Controllo se esiste il figlio sinistro
        """
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        """
        Controllo se esiste il figlio destro
        """
        return self._right(j) < len(self._data)

    def swap(self, i, j):
        """
        Scambia gli elementi nell'indice dell'array
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _uphead(self, j):
        """
        Spostamento item dal basso verso l'alto (dalla fine all'inizio)
        """
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self.swap(j, parent)
            self._uphead(parent)  # prosegue nella posizione del genitore di j (dove ora c'è j)

    def _downhead(self, j):
        """
        Spostamento item dall'alto verso il basso (dall'inizio alla fine)
        """
        if self._has_left(j):
            # se J ha figlio sinistro
            left_child_pos = self._left(j)
            small_child = left_child_pos
            if self._has_right(j):
                # se J ha figlio destro
                right_child_pos = self._right(j)
                if self._data[right_child_pos] < self._data[left_child_pos]:
                    small_child = right_child_pos  # il figlio destro ha chiave più piccola
                if self._data[small_child] < self._data[j]:
                    self.swap(j, small_child)
                    self._downhead(small_child)  # prosegue dalla posizione dello small_child

    # -------------------------------------------- Metodi pubblici -----------------------------------------------------

    def __init__(self):
        """
        Crea lista vuota.
        """
        self._data = []

    def __len__(self):
        """
        Restituisce il num di elementi (item) contenuti in _data
        """
        return len(self._data)

    def add(self, key, value: object):
        """
        Aggiunge una coppia (KEY-VALUE) nella coda prio
        """
        self._data.append(self._Item(key, value))
        self._uphead(len(self._data) - 1)  # se l'item ha priorità superiore lo fa "risalire" all'interno della coda

    def min(self):
        """
        Restituisce l'elemento (item) che ha priorità massima nella coda (cioè chiave minima)

        Solleva L'eccezzione Empty se la coda è vuota
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        item = self._data[0]
        return (item._key, item.value)

    def remove_min(self):
        """
        Restituisce e rimuove l'item con priorità massima, cioè situato nella prima posizione della coda

        Solleva L'eccezione Empty se la coda è vuota
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        self.swap(0, len(self._data) - 1)  # mette l'item con prio max alla fine
        item = self._data.pop()
        self._downhead(0)  # sistema la coda in base alla key
        return (item._key, item.value)
