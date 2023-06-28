import schedule
import time
from controllers.islands_controller import IslandsController
from controllers.storage_controller import Storage


class Cronjob:
    def __init__(self):
        self._islands = IslandsController()
        self._storages = Storage()
        self._richiesta_penne = 1000

    @staticmethod
    def check_status_and_create_request(magazzino, risorsa, penne_da_produrre):
        n_macchinari = round(
            (magazzino / penne_da_produrre) * 4
        )
        while (risorsa < (magazzino * n_macchinari)) or (n_macchinari > 0):
            n_macchinari -= 1
        if n_macchinari > 0:
            return n_macchinari
        else:
            return -1

    def my_task(self):
        magazzini = ['plastica', 'metallo', 'cartucce']
        for magazzino in magazzini:
            if self._storages.get_magazzino(magazzino) < 100:
                self._storages.crea_richiesta(magazzino)

        penne_da_produrre = self._richiesta_penne - self._storages.get_magazzino('penne')

        n_macchinari = self.check_status_and_create_request(self._storages.get_magazzino('punte'),
                                                            self._storages.get_magazzino('metallo'), penne_da_produrre)
        if n_macchinari > 0:
            self._islands.crea_richiesta('punte', n_macchinari)

        n_macchinari = self.check_status_and_create_request(self._storages.get_magazzino('astucci'),
                                                            self._storages.get_magazzino('plastica'), penne_da_produrre)
        if n_macchinari > 0:
            self._islands.crea_richiesta('astucci', n_macchinari)

        n_macchinari = self.check_status_and_create_request(self._storages.get_magazzino('tappi'),
                                                            self._storages.get_magazzino('plastica'), penne_da_produrre)
        if n_macchinari > 0:
            self._islands.crea_richiesta('tappi', n_macchinari)

        n_macchinari = round(
            (self._storages.get_magazzino('penne') / (
                    self._richiesta_penne - self._storages.get_magazzino('penne'))) * 4
        )
        while (self._storages.get_magazzino('punte') < (
                1 * n_macchinari)) and (
                self._storages.get_magazzino('tappi') < (
                1 * n_macchinari)) and (
                self._storages.get_magazzino('astucci') < (
                1 * n_macchinari)) or (n_macchinari > 0):
            n_macchinari -= 1
        if n_macchinari > 0:
            self._islands.crea_richiesta('penne', n_macchinari)


cronjob = Cronjob()
schedule.every(1).seconds.do(cronjob.my_task)  # Use the method from the cronjob instance

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
