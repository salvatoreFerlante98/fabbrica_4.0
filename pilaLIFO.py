from empty import Empty


class ArrayStack:
    """
    Implementazione di una pila LIFO utilizzando una lista
    come memoria sottostante.
    """

    def __init__(self):
        """
        Crea una pila vupta
        """
        self._data = []

    def __len__(self):
        """
        Restituisce il numero di elementi nella pila
        """
        return len(self._data)

    def is_empty(self):
        """
        Restituisce True se la pila è vuota
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Aggiunge un elemento 'e' in cima.
        """
        self._data.append(e)

    def top(self):
        """
        Restituisce senza eliminare l'elemento in cima alla pila
        Solleva l'eccezione Empty se la pil aè vuota
        """
        if self.is_empty():
            raise Empty('La pila è vuota')
        return self._data[-1]

    def pop(self):
        """
        Restituisce e rimuove l'elemento in cima alla pila (LIFO)
        Solleva l'eccezione Empty se la pila è vuota.
        """
        if self.is_empty():
            raise Empty('La pila è vuota')
        return self._data.pop()
