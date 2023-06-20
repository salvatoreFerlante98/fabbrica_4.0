from random import randrange

import MapBase

class HashMapBase(MapBase.MapBase):
    """
    Classe astratta di base per la mappa che utilizza una tabella Hash con compressione MAD
    """
    def __init__(self, cap: object = 11, p: object = 109345121) -> object:
        """
        Costruttore -> crea Hash Map vuota
        """
        self._table = cap * [None]
        self._n = 0 #numero di voci nella tabella Hash
        self._prime = p #numero primo per compressione MAD
        self._scale = 1 + randrange(p-1) #scala da 1 a p-1 per MAD
        self._shift = randrange(p) #shift da 0 a p-1 per MAD

    def _hash_function(self,k):
        """
        Calcola hash per il valore K
        """
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        """
        Restituisce il numero di elementi distinti attualmente memorizzati nella tabella Hash
        """
        return self._n

    def __getitem__(self, k):
        """
        Restituisce l'elemento associato alla chiave k
        """
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)

    def __setitem__(self, key, value):
        """
        Inserisce un elemento (KEY-VALUE) nella tabella hash
        """
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)
        if self._n > len(self._table) // 2: #per mantenere il fattore di carico <= 0.5
            self._resize(2* len(self._table) - 1 )

    def __delitem__(self,key):
        """
        Elimina l'elemento avente chiave KEY dalla tabella hash
        """
        j = self._hash_function(key)
        self._bucket_delitem(j,key)
        self._n -= 1

    def _resize (self, c):
        """
        Ridimensione la tabella hash alla dimensione c (cioè l'array di bucket)
        """
        old = list(self.items())  #registra gli elementi in una lista
        self._table = c *[None]   #ridimensiona la tabella alla capcacità desiderata
        self._n = 0               #_n viene ricalcolato
        for (k,v) in old:
            self[k] = v           # re-inserisce le vecchie coppie (K, V)