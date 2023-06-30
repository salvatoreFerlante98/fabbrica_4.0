from dataStructures.map_base import MapBase

class UnsortedTableMap(MapBase):
    """
    Implementazione della mappa attraverso una lista non ordinata.
    """
    def __init__(self):
        """
        Costruttore -> crea una mappa vuota.
        """
        self._table = []  # Lista di _Item

    def __getitem__(self, key):
        """
        Restituisce il valore associato alla chiave 'key'.
        Solleva KeyError se non viene trovato.
        """
        for item in self._table:
            if key == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(key))

    def __setitem__(self, key, value):
        """
        Assegna il valore 'value' alla chiave 'key', sovrascrivendo il valore presente se è presente.
        """
        for item in self._table:
            if key == item._key:
                item._value = value
                return
        # Se non trova la chiave
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """
        Rimuove l'elemento associato alla chiave 'key'.
        Solleva KeyError se non viene trovato.
        """
        for j in range(len(self._table)):
            if key == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('KeyError: ' + repr(key))

    def __len__(self):
        """
        Restituisce il numero di elementi contenuti nella mappa.
        """
        return len(self._table)

    def __iter__(self):
        """
        Genera un'iterazione delle chiavi della mappa.
        """
        for item in self._table:
            yield item._key

    def get_magazzino(self, key):
        for item in self._table:
            if key == item._key:
                return item
        raise KeyError('Key Error: ' + repr(key))
