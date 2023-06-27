from dataStructures.coda_conc_circ import CircularQueue


class Isola:

    def __init__(self, nome, consumo):
        self.nome = nome
        self.consumo = consumo

    def get_nome(self):
        return self.nome

    def get_consumo(self):
        return self.consumo

    def carica_macchinari(self):
        macchinari = CircularQueue()

