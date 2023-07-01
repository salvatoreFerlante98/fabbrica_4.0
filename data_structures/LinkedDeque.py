from DoublyLinkedBase import _DoublyLinkedBase
from empty import Empty


class LinkedDeque(_DoublyLinkedBase):
    """
    Implementazione di coda doppia con lista doppiamente concatenata.
    """

    def first(self):
        """
        Restituisce ma non rimuove il primo elemento della coda doppia.
        """
        if self.is_empty():
            raise Empty("La coda doppia è vuota")
        return self._header._next._element

    def last(self):
        """
        Restituisce ma non rimuove l'ultimo elemento della coda doppia.
        """
        if self.is_empty():
            raise Empty("La coda doppia è vuota")
        return self._trailer._prev._element

    def insert_first(self, e):
        """
        Aggiunge un elemento all'inizio della coda doppia.
        """
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """
        Aggiunge un elemento alla fine della coda doppia.
        """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Rimuove e restituisce il primo elemento della coda doppia.
        Solleva l'eccezione Empty se la coda doppia è vuota.
        """
        if self.is_empty():
            raise Empty("La coda doppia è vuota")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """
        Rimuove e restituisce l'ultimo elemento della coda doppia.
        Solleva l'eccezione Empty se la coda doppia è vuota.
        """
        if self.is_empty():
            raise Empty("La coda doppia è vuota")
        return self._delete_node(self._trailer._prev)
