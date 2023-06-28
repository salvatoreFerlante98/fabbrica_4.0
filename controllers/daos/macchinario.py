from time import sleep
from threading import Thread


class Macchinario:
    __slots__ = '_id_macchinario', '_stato', '_tempo_lavorazione', '_lavorato', '_isola'

    def __init__(self, id_macchinario, stato, tempo_lavorazione, isola):
        self._id_macchinario = id_macchinario
        self._stato = stato
        self._tempo_lavorazione = tempo_lavorazione
        self._lavorato = False
        self._isola = isola

    def __lt__(self, other):
        return self._tempo_lavorazione < other._tempo_lavorazione

    def get_id(self):
        return self._id_macchinario

    def get_stato(self):
        return self._stato

    def get_tempo_lavorazione(self):
        return self._tempo_lavorazione

    def get_isola(self):
        return self._isola

    def accendi_macchinario(self):
        self._stato = 'On'

    def spegni_macchinario(self):
        self._stato = 'Off'

    def _work(self):
        if self._stato == 'On' and self._stato != 'Lavorando':
            self._lavorato = True
            self._stato = 'Lavorando'
            sleep(self._tempo_lavorazione)
            self._stato = 'On'
        else:
            self._lavorato = False

    def lavora(self):
        thread = Thread(self._work())
        thread.start()
        thread.join()
        if self._lavorato:
            self._lavorato = False
            return True
        else:
            return False


