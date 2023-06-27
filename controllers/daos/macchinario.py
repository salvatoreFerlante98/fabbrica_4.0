from time import sleep


class Macchinario:
    __slots__ = 'id_macchinario', 'stato', 'tempo_lavorazione', 'isola'

    def __init__(self, id_macchinario, stato, tempo_lavorazione, isola):
        self.id_macchinario = id_macchinario
        self.stato = stato
        self.tempo_lavorazione = tempo_lavorazione
        self.isola = isola

    def __lt__(self, other):
        return self.tempo_lavorazione < other.tempo_lavorazione

    def getId(self):
        return self.id_macchinario

    def getStato(self):
        return self.stato

    def getTempoLavorazione(self):
        return self.tempo_lavorazione

    def getIsola(self):
        return self.isola

    def lavora(self, magazzino, consumo):
        if self.stato == 'On' and self.stato != 'Lavorando' and magazzino.usaPezzo(self.isola, consumo) is True:
            self.stato = 'Lavorando'
            sleep(self.tempo_lavorazione)
            self.stato = 'On'
            return True
        return False


