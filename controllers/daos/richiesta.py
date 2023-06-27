class Richiesta:
    __slots__ = 'id_richiesta', 'tipo', 'data', 'quantita'

    def __init__(self, id_richiesta, tipo, data, quantita):
        self.id_richiesta = id_richiesta
        self.tipo = tipo
        self.data = data
        self.quantita = quantita

    def __str__(self):
        return "Richiesta: " + str(self.id_richiesta) + " - " + str(self.tipo) + " - " + str(self.data) + " - " + str(
            self.quantita) + "\n"

    def get_id(self):
        return self.id_richiesta

    def get_tipo(self):
        return self.tipo

    def get_data(self):
        return self.data

    def get_quantita(self):
        return self.quantita
