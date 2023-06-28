from HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
    """
    Mappa hash implementata con esplorazione lineare per la risoluzione delle collisioni.
    """

    _AVAIL = object()  # Sentinella relativa a cancellazioni -> oggetto di qualsiasi tipo

    def _is_available(self, j):
        """
        Restituisce True se l'indice j è disponibile nella tabella.
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, key):
        """
        Cerca la chiave key nel bucket j.
        Restituisce la tupla ('successo', 'indice') nei seguenti casi:
        - se è stata trovata una corrispondenza, 'successo' sarà True e 'indice' la sua posizione
        - se non è stata trovata una corrispondenza, 'successo' sarà False e 'indice' il primo slot disponibile
        """
        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j  # marca la posizione j come la prima disponibile
                if self._table[j] is None:
                    return (False, first_avail)  # corrispondenza non trovata
            elif key == self._table[j]._key:
                return (True, j)  # corrispondenza trovata
            j = (j + 1) % len(self._table)  # continua a cercare (ciclicamente)

    def _bucket_getitem(self, j, key):
        """
        Restituisce l'elemento con chiave key contenuto nel bucket individuato nella tabella mediante l'hash j.
        """
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))
        return self._table[s]._value

    def _bucket_setitem(self, j, key, value):
        """
        Inserisce l'elemento (key-value) nel bucket con hash j.
        """
        found, s = self._find_slot(j, key)
        if not found:
            self._table[s] = self._Item(key, value)  # inserisce un nuovo elemento
            self._n += 1  # incrementa il numero di elementi contenuti nella tabella
        else:
            self._table[s]._value = value  # sovrascrive quello esistente

    def _bucket_delitem(self, j, key):
        """
        Elimina l'elemento con chiave key contenuto nel bucket j.
        """
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))
        self._table[s] = ProbeHashMap._AVAIL  # contrassegna come libero (= None)

    def __iter__(self):
        """
        Scorre per chiavi.
        """
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

    def __len__(self):
        """
        Restituisce il numero di elementi contenuti nella tabella.
        """
        return self._n

    def __getitem__(self, key):
        """
        Restituisce l'elemento con chiave key.
        """
        j = self._hash_function(key)
        return self._bucket_getitem(j, key)

    def __setitem__(self, key, value):
        """
        Inserisce l'elemento (key-value).
        """
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)

    def __delitem__(self, key):
        """
        Elimina l'elemento con chiave key.
        """
        j = self._hash_function(key)
        self._bucket_delitem(j, key)

    def __contains__(self, key):
        """
        Restituisce True se la chiave key è contenuta nella tabella.
        """
        j = self._hash_function(key)
        return self._bucket_getitem(j, key) is not None

    def __str__(self):
        """
        Restituisce la stringa rappresentante la tabella.
        """
        return str(self._table)
