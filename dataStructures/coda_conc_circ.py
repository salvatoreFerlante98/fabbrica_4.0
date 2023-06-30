from dataStructures.empty import Empty


class CircularQueue:
    """
    Implementazione della coda usando una lista concatenata circolare per l'archiviazione.
    """

    class _Node:
        """
               Classe leggera, non pubblica per la memorizzazione di un nodo collegato singolarmente.
               """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            """
            Inizializza i campi del nodo.
            """
            self._element = element
            self._next = next

    # ---------------------------------------- metodi della coda -----------------------------------------------------

    def __init__(self):
        """
        Crea una coda vuota.
        """
        self._tail = None
        self._size = 0

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
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        Rimuove e restituisce l'elemento in testa alla coda(FIFO).
        Solleva l'eccezione Empty se la coda è vuota
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """
        Aggiunge un elemento in fondo alla coda.
        """
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """
        Ruota l'elemento frontale sul retro della coda.
        """
        if self._size > 0:
            self._tail = self._tail._next

    def __iter__(self):
        """
        Returns an iterator for the CircularQueue.
        """
        if self.is_empty():
            return iter([])  # Return an empty iterator

        start = self._tail._next
        current = start
        while True:
            yield current._element
            current = current._next
            if current is start:
                break
