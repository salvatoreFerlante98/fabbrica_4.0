from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    """
    Mappa hash implementata con esplorazione lineare per la risoluzione delle collisioni.
    """

    _AVAIL_ = object()  # Sentinella relativa a cancellazioni -> oggetto di qualsiasi tipo

    def _is_available(self, j):
        """
        Restituisce True se l'indice j è disponibile nella tabella
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL_

    def _find_slot(self, j, k):
        """
        Cerca la chiave K nel bucket j
        Restituisce la tupla ('successo','indice') nei seguenti casi:
        - se è stata trovata una corrispondenza, 'successo' sarà True e 'indice' la sua posizione
        - se non è stata trovata una corrispondenza, 'successo' sarà False e 'indice' il primo slot disponibile
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j  # marca la pos j come prima dipsonibile
                if self._table[j] is None:
                    return (False, firstAvail)  # corrispondenza non trovata
            elif k == self._table[j]._key:
                return (True, j)  # corrispondenza trovata
            j = (j + 1) % len(self._table)  # continua a cercare (ciclicamente)

    def _bucket_getitem(self, j, k):
        """
        Restituisce l'elemento con chiave k contenuto nel bucket individuato nella tabella mendiante l'hash j
        """
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error' + repr(j))
        return self._table[s]._value

    def _bucket_setitem(self, j, key, value):
        """
        Inserisce l'elemento (KEY-VALUE) nel bucket con hash j
        """
        found, s = self._find_slot(j, key)
        if not found:
            self._table[s] = self._Item(key, value)  # insierisce un nuovo elemento
            self._n += 1  # incrementa in numero di elementi contenuti nella tab
        else:
            self._table[s]._value = value  # sovrascrive quello esistente

    def _bucket_delitem(self, j, key):
        """
        Elimina l'elemento con chiave KEY contenuto nel bucket j
        """
        found, s = self._find_slot(j, key)
        if not found:
            raise KeyError('Key Error' + repr(key))
        self._table[s] = ProbeHashMap._AVAIL_  # contrassegna come libero (= None)

    def __iter__(self):
        """
        Scorre per chiavi
        """
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
