class Richiesta:
    __slots__ = 'id_richiesta', 'tipo', 'quantita'

    def __init__(self, id_richiesta, tipo, quantita):
        """
        Inizializza un oggetto Richiesta con un ID, un tipo e una quantità specificati.
        """
        self.id_richiesta = id_richiesta
        self.tipo = tipo
        self.quantita = quantita

    def __str__(self):
        """
        Restituisce una rappresentazione testuale dell'oggetto Richiesta.
        """
        return "Richiesta: " + str(self.id_richiesta) + " - " + str(self.tipo) + " - " + str(self.quantita)

    def get_id(self):
        """
        Restituisce l'ID della richiesta.
        """
        return self.id_richiesta

    def get_tipo(self):
        """
        Restituisce il tipo della richiesta.
        """
        return self.tipo

    def get_quantita(self):
        """
        Restituisce la quantità della richiesta.
        """
        return self.quantita
