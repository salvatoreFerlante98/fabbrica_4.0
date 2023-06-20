class Tree:
    """
    Classe base astratta che rappresenta una struttura da albero.
    """
    # ---------------------------------------- classe Position innestata -----------------------------------------------
    class Position:
        """
        Astrazione che rappresenta la posizione di un singolo elemento.
        """

        def element(self):
            """
            Restituisce l'elemento memorizzato in questa posizione.
            """
            raise NotImplementedError('Deve essere implementato dalla sotto-classe')

        def __eq__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione.
            """
            raise NotImplementedError('Deve essere implementato dalla sotto-classe')

        def __ne__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione.
            """
            return not (self == other)

    # --------------------- metodi astratti che la sotto classe concreta deve supportare -------------------------------

    def root(self):
        """
        Restituisce Position che rappresenta la radice dell'albero (None se è vuoto).
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    def parent(self, p):
        """
        Restituisce Position che rappresenta il genitore di 'p' (None se 'p' è radice).
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    def num_children(self, p):
        """
        Restituisce il numero di figli della Position 'p'.
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'.
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    def __len__(self):
        """
        Restituisce il numero totale di elementi nell'albero.
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    # ------------------------------ metodi concreti implementati in questa classe -------------------------------------

    def is_root(self, p):
        """
        Restituisce True se la Position 'p' è la radice dell'albero.
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        Restituisce True se la Position 'p' non ha figli.
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        Restituisce True se l'albero è vuoto.
        """
        return len(self) == 0
