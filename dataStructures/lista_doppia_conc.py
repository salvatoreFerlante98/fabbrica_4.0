class _DoublyLinkedBase:
    """
    Una classe che fornisce una rappresentazione di lista doppiamente concatenata.
    """

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            """
            Inizializza i campi del nodo.
            """
            self._element = element
            self._prev = prev
            self._next = next

    # ---------------------------------------- metodi della lista -----------------------------------------------------

    def __init__(self):
        """
        Crea una lista vuota.
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
        Restituisce il numero di elementi nella lista.
        """
        return self._size

    def is_empty(self):
        """
        Restituisce True se la lista è vuota
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Aggiunge l'elemento 'e' tra due nodi esistenti e restituisce un nuovo nodo.
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Elimina il nodo non-sentinella dalla lista e restituisce il suo elemento.
        """
        predeccessor = node._prev
        successor = node._next
        predeccessor._next = successor
        successor._prev = predeccessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
