from collections.abc import MutableMapping


class MapBase(MutableMapping):
    """
    Classe base astratta che include una classe _Item
    """

    # -------------------------------------------- Classe _Item --------------------------------------------------------
    class _Item:
        """
        Classe innestata che figura una coppia K-V contenuti all'interno della mappa.
        """
        __slots__ = '_key', 'value'

        def __init__(self, Key, Value):
            """
            Inizializza un oggetto ti tipo _Item.
            """
            self._key = Key
            self.value = Value

        def __eq__(self, other):
            return self._key == other._key  # Confronta in base alla chiave

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key  # confronta gli elementi in base alla chiave
