from map_base import MapBase

class UnsortedTableMap(MapBase):
    """
    Implementazione della mappa attraverso una lista non ordinata
    """
    def __init__(self):
        """
        Costruttore -> crea una mappa vuota
        """
        self._table = [] #Lista di _Item

    def __getitem__(self, k):
        """
        Restituisce il valore associato alla chiave 'k'

        (solleva KeyError se non trovare)
        """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError ('Key Error: '+ repr(k))

    def __setitem__(self, key, value):
        """
        Assegua il valore 'value' alla chiave 'key', sovrascrive il valore presente se è presente
        """
        for item in self._table:
            if key == item._key:
                item._value =value
                return
        #se non trova la chiave
        self._table.append(self._Item(key,value))

    def __delitem__(self, key):
        """
        Rimuove l'elemento associato alla chiave 'key'
        solleva KeyError se non trovato
        """
        for j in range(len(self._table)):
            if key == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError ('KeyError: ' + repr(key))

    def __len__(self):
        """
        Restituisce il numero di elementi contenuti nella mappa
        """
        return len(self._table)

    def __iter__(self):
        """
        Genera un interazione delle chiavi della mappa
        """
        for item in self._table:
            yield item._key
