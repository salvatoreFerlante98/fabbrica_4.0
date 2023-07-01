from time import sleep
from threading import Thread


class Macchinario:
    __slots__ = '_id_macchinario', '_stato', '_tempo_lavorazione', '_lavorato', '_isola'

    def __init__(self, id_macchinario, stato, tempo_lavorazione, isola):
        """
        Inizializza un oggetto Macchinario con l'id, lo stato, il tempo di lavorazione e l'isola specificati.
        """
        self._id_macchinario = id_macchinario
        self._stato = stato
        self._tempo_lavorazione = tempo_lavorazione
        self._lavorato = False
        self._isola = isola

    def __lt__(self, other):
        """
        Confronta due macchinari in base al loro tempo di lavorazione.
        """
        return self._tempo_lavorazione < other._tempo_lavorazione

    def get_id(self):
        """
        Restituisce l'id del macchinario.
        """
        return self._id_macchinario

    def get_stato(self):
        """
        Restituisce lo stato del macchinario.
        """
        return self._stato

    def get_tempo_lavorazione(self):
        """
        Restituisce il tempo di lavorazione del macchinario.
        """
        return self._tempo_lavorazione

    def get_isola(self):
        """
        Restituisce l'isola a cui appartiene il macchinario.
        """
        return self._isola

    def accendi_macchinario(self):
        """
        Accende il macchinario.
        """
        self._stato = 'On'

    def spegni_macchinario(self):
        """
        Spegne il macchinario.
        """
        self._stato = 'Off'

    def _work(self):
        """
        Simula il lavoro del macchinario. Cambia lo stato del macchinario in 'Lavorando' per il tempo di lavorazione
        specificato, quindi ritorna allo stato 'On'.
        """
        if self._stato == 'On' and self._stato != 'Lavorando':
            self._lavorato = True
            self._stato = 'Lavorando'
            sleep(self._tempo_lavorazione)
            self._stato = 'On'
        else:
            self._lavorato = False

    def lavora(self):
        """
        Avvia il lavoro del macchinario in un thread separato.
        """
        thread = Thread(self._work())
        thread.start()
        thread.join()
        if self._lavorato:
            self._lavorato = False
            return True
        else:
            return False
