from data_structures.TreeMultiLeaf import TreeMultiLeaf


class Permissions:

    def __init__(self):
        """
        Inizializza un oggetto Permissions con un albero dei permessi predefinito.
        """
        self._permission = TreeMultiLeaf('admin')
        self._permission + 'responsabile_macchinari'
        self._permission + 'responsabile_logistica'
        self._permission + 'risorse_umane'
        self._permission['responsabile_macchinari'] + 'punte'
        self._permission['responsabile_macchinari'] + 'astucci'
        self._permission['responsabile_macchinari'] + 'tappi'
        self._permission['responsabile_macchinari'] + 'penne'

    def get_permission(self, role):
        """
        Restituisce i permessi associati al ruolo specificato.
        """
        return self._permission[role]
