from data_structures.empty import Empty


class LinkedQueue:
    """
    Implementazione della coda FIFO utilizzando una lista semplicemente concatenata.
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
        self._head = None
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
        return self._head._element

    def dequeue(self):
        """
        Rimuove e restituisce l'elemento in testa alla coda(FIFO).
        Solleva l'eccezione Empty se la coda è vuota
        """
        if self.is_empty():
            raise Empty('La coda è vuota')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """
        Aggiunge un elemento in fondo alla coda.
        """
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
