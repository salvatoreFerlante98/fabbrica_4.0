class Richiesta:
    __slots__ = 'id_richiesta', 'tipo','quantita'

    def __init__(self, id_richiesta, tipo, quantita):
        self.id_richiesta = id_richiesta
        self.tipo = tipo
        self.quantita = quantita

    def __str__(self):
        return "Richiesta: " + str(self.id_richiesta) + " - " + str(self.tipo) + " - " + str(self.quantita)
    def get_id(self):
        return self.id_richiesta

    def get_tipo(self):
        return self.tipo

    def get_quantita(self):
        return self.quantita
