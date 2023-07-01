import hash_map_base
import unsorted_table_map


class ChainHashMap(hash_map_base.HashMapBase):
    """
    Mappa hash implementata con concatenazione separata per la risoluzione delle collisioni.
    """

    def _bucket_getitem(self, j, key):
        """
        Restituisce l'elemento con chiave k contenuto nel bucket individuato nella tabella mendiante l'hash j
        """
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error' + repr(key))
        return bucket[key]

    def _bucket_setitem(self, j, key, value):
        """
        Inserisce l'elemento (KEY-VALUE) nel bucket con hash j
        """
        if self._table[j] is None:
            self._table[j] = unsorted_table_map.UnsortedTableMap()  # creo un nuovo bucket nella tabella
        oldSize = len(self._table[j])
        self._table[j][key] = value
        if len(self._table[j]) > oldSize:
            self._n += 1

    def _bucket_delitem(self, j, key):
        """
        Elimina l'elemento con chiave KEY contenuto nel bucket j
        """
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error' + repr(key))
        del bucket[key]

    def __iter__(self):
        """
        Iteratore
        """
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

    def is_empty(self):
        """
        :return:
        """
        return self._n == 0
