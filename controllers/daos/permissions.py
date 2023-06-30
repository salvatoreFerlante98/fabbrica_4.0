from dataStructures.Tree import Tree


class Permissions:

    def __init__(self):
        self.__permission = Tree('admin')
        self.__permission + 'responsabile_macchinari'
        self.__permission + 'responsabile_logistica'
        self.__permission + 'responsabile_spedizioni'

    def get_permission(self, role):
        return self.__permission.search(role)
