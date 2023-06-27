from random import randint

from controllers.daos import macchinario
from controllers.storage_controllers import Storage
from dataStructures.coda_conc_circ import CircularQueue
from dataStructures.lista_posizionale import PositionalList
from daos.macchinario import Macchinario
from daos.isola import Isola


class IslandsController:

    def __init__(self):
        self.isole = PositionalList()
        isole_tipi = ['punte', 'astucci', 'tappi', 'penne']
        for nome in isole_tipi:
            self.macchinari = CircularQueue()
            self.isole.add_last(self.macchinari)
            t_lavorazione = randint(5, 10)
            for j in range(0, 4):
                self.macchinari.enqueue(Macchinario(j, 'Off', t_lavorazione, nome))

            self.isole.add_last(self.macchinari)

    def gestisci_macchinari(self):
        if Storage.usaPezzo():
            Macchinario.lavora(self.macchinari.first(), Isola.getConsumo(self.macchinari.first().tipo))
    def richiedi_rifornimento(self, quantita):

