from random import randint

from controllers.daos.macchinario import Macchinario
from data_structures.CircularQueue import CircularQueue


class Isola:

    def __init__(self, nome, consumo):
        self._nome = nome
        self._consumo = consumo
        self._macchinari = self._carica_macchinari()

    def get_consumo(self):
        """
        Restituisce il consumo dell'isola.
        """
        return self._consumo

    def get_nome(self):
        """
        Restituisce il nome dell'isola.
        """
        return self._nome

    def _carica_macchinari(self):
        """
        Carica i macchinari nell'isola e restituisce una coda circolare contenente i macchinari.
        """
        macchinari = CircularQueue()
        t_lavorazione = randint(5, 10)
        for i in range(0, 4):
            macchinari.enqueue(Macchinario(i, 'Off', t_lavorazione, self._nome))
        return macchinari

    def gestione_macchinari(self, richiesta):
        """
        Gestisce l'accensione/spegnimento dei macchinari in base alla richiesta specificata.
        """
        macchinari_on = self._macchinari_accesi()
        if macchinari_on < richiesta:
            self._accendi_macchinari(richiesta -macchinari_on)
        elif macchinari_on > richiesta:
            self._spegni_macchinari(macchinari_on- richiesta)

    def _macchinari_accesi(self):
        """
        Restituisce il numero di macchinari accesi.
        """
        macchinari_on = 0
        for macchinario in self._macchinari:
            if macchinario.get_stato() == 'On':
                macchinari_on += 1

        return macchinari_on

    def _accendi_macchinari(self, num):
        """
        Accende il numero specificato di macchinari.
        """
        i = 0
        while i < num:
            macchinario = self._macchinari.first()
            stato = macchinario.get_stato()
            if stato == 'Off':
                macchinario.accendi_macchinario()
                self._macchinari.rotate()
                i += 1
            self._macchinari.rotate()

    def _spegni_macchinari(self, num):
        """
        Spegne il numero specificato di macchinari.
        """
        i = 0
        while i < num:
            macchinario = self._macchinari.first()
            stato = macchinario.get_stato()
            if stato == 'On':
                macchinario.spegni_macchinario()
                self._macchinari.rotate()
                i += 1
            self._macchinari.rotate()

    def get_status_macchinari(self):
        """
        Restituisce lo stato di tutti i macchinari nell'isola.
        """
        stati = []
        for macchinario in self._macchinari:
            stati.append(macchinario.get_stato())
        return stati

    def opera_macchinario(self):
        """
        Avvia il macchinario nell'isola se è acceso.
        """
        if self._macchinari.last().get_stato() == 'On':
            self._macchinari.last().lavora()
