from empty import Empty


class ArrayQueue:
    """
    Implementazione della coda FIFO utilizzando una lista Python come memoria sottostante.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """
        Crea una coda vuota.
        """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Restituisce il numero di elementi in coda
        """
        return self._size

    def is_empty(self):
        """
        Restituisce True se la coda è vuota
        """
        return self._size == 0

    def first(self):
        """
        Restituisce ma non elimina l'elemento in testa alla coda
        Solleva l'eccezione Empty se la coda è vuota
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        return self._data[self._front]

    def dequeue(self):
        """
        Rimuove e restituisce l'elemento in testa alla coda(FIFO).
        Solleva l'eccezione Empty se la coda è vuota
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """
        Aggiunge un elemento in fondo alla coda.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """
        Ridimensiona la lista con capacità >= len(self)
        """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
