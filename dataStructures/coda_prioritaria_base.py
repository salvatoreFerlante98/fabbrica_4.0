class PriorityQueueBase:
    """
    Classe di base astratta per una coda prioritaria
    """

    # ------------------------------------------ Classe Item innestata -------------------------------------------------
    class _Item:
        """
        Composito leggere per archiviare elementi della coda prio
        """
        __slots__ = '_key', '_value'

        def __init__(self, key, value: object):
            self._key = key
            self._value = value

        def __lt__(self, other):
            """
            LESS-THAN COMPARISON:
            Specifica qual è il criterio di confronto di due _Item: confronto per chiave
            """
            return self._key < other._key

    # ------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        """
        Restituisce True se la coda priorità è vuota
        """
        return len(self) == 0
