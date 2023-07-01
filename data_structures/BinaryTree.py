from Tree import Tree


class BinaryTree(Tree):
    """
    Classe base astratta che rappresenta una struttura da albero binario.
    """

    # -------------------------------------- metodi astratti condizionali ----------------------------------------------
    def left(self, p):
        """
        Restituisce una Position che rappresenta il figlio sinistro di 'p'.

        Restituisce None se 'p' non ha un figlio sinistro.
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    def right(self, p):
        """
        Restituisce una Position che rappresenta il figlio destro di 'p'.

        Restituisce None se 'p' non ha un figlio destro.
        """
        raise NotImplementedError('Deve essere implementato dalla sotto-classe')

    # ------------------------------ metodi concreti implementati in questa classe -------------------------------------
    def sibling(self, p):
        """
        Restituisce una Position che rappresenta il fratello di 'p' (o None se non è fratello).
        """
        parent = self. parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'.
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
