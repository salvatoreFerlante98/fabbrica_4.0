from data_structures.TreeMultiLeaf import TreeMultiLeaf


class Permissions:

    def __init__(self):
        """
        Inizializza un oggetto Permissions con un albero dei permessi predefinito.
        """
        self._permission = TreeMultiLeaf('admin')
        self._permission + 'responsabile_macchinari'  # Aggiunge un ruolo al livello superiore dell'albero
        self._permission + 'responsabile_logistica'  # Aggiunge un ruolo al livello superiore dell'albero
        self._permission + 'responsabile_spedizioni'  # Aggiunge un ruolo al livello superiore dell'albero
        self._permission['responsabile_macchinari'] + 'punte'  # Aggiunge un permesso al ruolo 'responsabile_macchinari'
        self._permission['responsabile_macchinari'] + 'astucci' # Aggiunge un permesso al ruolo 'responsabile_macchinari'
        self._permission['responsabile_macchinari'] + 'tappi'  # Aggiunge un permesso al ruolo 'responsabile_macchinari'
        self._permission['responsabile_macchinari'] + 'penne'  # Aggiunge un permesso al ruolo 'responsabile_macchinari'

    def get_permission(self, role):
        """
        Restituisce i permessi associati al ruolo specificato.
        """
        return self._permission[role]
