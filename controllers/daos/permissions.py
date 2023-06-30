from dataStructures.Tree import Tree


class Permissions:

    def __init__(self):
        self.__permission = Tree("admin")
        self.__permission + "responsabile_tecnico"
        self.__permission + "responsabile_magazzino"
        self.__permission.addSubchild("responsabile_tecnico", "isola_punte")
        self.__permission.addSubchild("responsabile_tecnico", "isola_astucci")
        self.__permission.addSubchild("responsabile_tecnico", "isola_penne")
        self.__permission.addSubchild("responsabile_tecnico", "isola_tappi")
        self.__permission.addSubchild("responsabile_magazzino", "magazziniere")
        self.__permission.addSubchild("responsabile_magazzino", "spedizioniere")

    def get_permission(self, role):
        return self.__permission.search(role)
