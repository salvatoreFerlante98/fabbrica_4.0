from albero_binario import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """
    Classe che definisce un albero binario concatenato
    """

    class _Node:
        """
        Classe leggera non pubblica per la memorizzazione di un nodo.
        """
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            """
            Costruttore di default
            """
            self._element = element
            self._parent = parent
            self._right = right
            self._left = left

    class Position(BinaryTree.Position):
        """
        Astrazione che rappresenta la posizione di un singolo elemento.
        """

        def __init__(self, container, node):
            """
            Costruttore
            """
            self._container = container
            self._node = node

        def element(self):
            """
            Restituisce l'elemento memorizzato in questa Position.
            """
            return self._node._element

        def __eq__(self, other):
            """
            Restituisce true se 'other' Position rappresenta la stessa posizione.
            """
            return type(other) is type(self) and other._node is self._node

    # -------------------------------------------------------------------------------------------------------------------
    def _validate(self, p):
        """
        Restituisce il nodo associato alla posizione 'p' se la posizione è valida
        """
        if not isinstance(p, self.Position):
            raise TypeError('p deve essere di tipo Position')
        if p._container is not self:
            raise ValueError('p non appartiene a questo contenitore')
        if p._node._parent is p._node:
            raise ValueError('p non è più valido')  # per i nofi deprecati
        return p._node

    def _make_position(self, node):
        """
        Restituisce l'istanza Position per il nodo dato (None se non viene passato nessun nodo)
        """
        return self.Position(self, node) if node is not None else None

    # -------------------------------------- costruttore dell'albero binario --------------------------------------------
    def __init__(self):
        """
        Costruttore:
        Crea un albero binario inizialmente vuoto
        """
        self._root = None
        self._size = 0

    # ---------------------------------------------- Metodi accessori --------------------------------------------------
    def __len__(self):
        """
        Restituisce il numero totale di elementi nell'albero
        """
        return self._size

    def root(self):
        """
        Restituisce l'istanza Position che rappresenta la radice dell'albero (None se l'albero è vuoto)
        """
        return self._make_position(self._root)

    def parent(self, p):
        """
        Restituisce l'istanza Position che rappresenta il genitore di 'p' (None se 'p' è la root)
        """
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """
        Restituisce l'istanza Position che rappresenta il figlio sinistro di 'p'.

        Restituisce None se 'p' non ha un figlio sinistro
        """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """
        Restituisce l'istanza Position che rappresenta il figlio destro di 'p'.

        Restituisce None se 'p' non ha un figlio destro
        """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """
        Restituisce il numero di figli di 'p'
        """
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """
        Posizione l'elemento 'e' alla radice di un albero vuoto e torna alla nuova Position

        Solleva ValueError se l'albero non è vuoto
        """
        if self._root is not None: raise ValueError('Albero non vuoto -> radice già esistente')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """
        Crea un nuovo figlio sinistro per la posizione 'p' cui memorizza 'e',
        restituisce la Position del nuovo nodo

        Solleva ValueError se 'p' ha gia un figlio sinistro
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child già esistente')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Crea un nuovo figlio destro per la posizione 'p' cui memorizza 'e',
        restituisce la Position del nuovo nodo

        (Solleva ValueError se 'p' ha gia un figlio destro)
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Left child già esistente')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """
        Sostituisce l'elemento in posizione 'p' con l'elemento 'e' e restituisce il vecchio elemento
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Rimuove il nodo in Position 'p' e lo sostituisce con il figlio, se è presente.

        Ritorna l'elemento che era stato memorizzato in 'p'

        Solleva ValueError se 'p' non è valida o se ha due figli
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p ha due figli')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent  # il nonno di child diventa suo padre
        if node is self._root:
            self._root = child  # il figlio di node diventa la radice
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """
        Collega gli alberi t1 e t2 come sottoalberi sinistro e destro della foglia p
        """
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('p deve essere una foglia')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('gli alberi devono essere dello stesso tipo')

        self._size += len(t1) + len(t2)
        if not t1.mapis_empty():  # collega t1 come sottoalbero sinistro di 'p'
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # imposta l'istanza di t1 come vuota
            t1._size = 0
        if not t2.mapis_empty():  # collega t2 come sottoalbero destro di 'p'
            t2._root._parente = node
            node._right = t2._root
            t2._root = None  # imposta l'istanza di t2 come vuota
            t2._size = 0

    def _subtree_preoreder(self, p):
        """
        Restituisce una lista contenente la preorder di tutte le foglie del sotto-albero di 'p'
        """
        yield p
        for c in self.children(p):
            for other in self._subtree_preoreder(c):
                yield other
