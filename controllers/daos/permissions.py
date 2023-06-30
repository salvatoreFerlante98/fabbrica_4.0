from dataStructures.albero_binario_conc1 import LinkedBinaryTree


class Permissions:

    def __init__(self):
        self.__permission = LinkedBinaryTree()
        self.__permission.add_root('admin')
        self.__permission.add_left('admin', 'responsabile_tecnico')
        self.__permission.add_right('admin', 'centro_logistico')
        self.__permission.add_left('centro logistico', 'centro_logistico ufficio')
        self.__permission.add_right('centro logistico', 'centro_logistico magazziniere')

    def get_permission(self, role):
        return self.__permission.search(role)
