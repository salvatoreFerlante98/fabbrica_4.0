from dataStructures.Tree import Tree


class Permissions:

    def __init__(self):
        self.__permission = Tree("admin")
        self.__permission + "responsabile tecnico"
        self.__permission + "responsabile magazziniere"
        self.__permission.addSubchild("responsabile tecnico", "isola_punte")
        self.__permission.addSubchild("responsabile tecnico", "isola_astucci")
        self.__permission.addSubchild("responsabile tecnico", "isola_penne")
        self.__permission.addSubchild("responsabile tecnico", "isola_tappi")
        self.__permission.addSubchild("responsabile magazziniere", "magazzino")
        self.__permission.addSubchild("responsabile magazziniere", "spedizioniere")

    def get_permission(self, role):
        return self.__permission.search(role)
