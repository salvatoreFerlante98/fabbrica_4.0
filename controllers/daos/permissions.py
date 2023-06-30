from dataStructures.Tree import Tree


class Permissions:

    def __init__(self):
        self._permission = Tree('admin')
        self._permission + 'responsabile_macchinari'
        self._permission + 'responsabile_logistica'
        self._permission + 'responsabile_spedizioni'
        self._permission['responsabile_macchinari'] + 'punte'
        self._permission['responsabile_macchinari'] + 'astucci'
        self._permission['responsabile_macchinari'] + 'tappi'
        self._permission['responsabile_macchinari'] + 'penne'

    def get_permission(self, role):
        return self._permission[role]
