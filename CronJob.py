import time

import schedule


class Cronjob:
    def __init__(self, islands, storage):
        self._islands = islands
        self._storages = storage
        self._richiesta_penne = 1000

    @staticmethod
    def check_status_and_choose_machines(prodotto, consumo, risorsa, penne_da_produrre):
        """
        Controlla lo stato e sceglie il numero di macchinari necessari per produrre le penne.
        Calcola il numero di macchinari in base al rapporto tra il prodotto richiesto e il numero di penne da produrre.
        Verifica che la quantità di risorsa disponibile sia sufficiente e che il numero di macchinari non sia zero.
        Restituisce il numero di macchinari scelto. Se non è possibile soddisfare le condizioni, restituisce -1.
        """
        n_macchinari = round((prodotto / penne_da_produrre) * 40)
        while (risorsa < (consumo * n_macchinari)) or (n_macchinari == 0):
            n_macchinari -= 1
        if n_macchinari > 0:
            return n_macchinari
        else:
            return -1

    def my_task(self):
        """
        Esegue il compito pianificato.
        Controlla lo stato dei magazzini e crea richieste se la quantità di un magazzino è inferiore a 100.
        Calcola il numero di macchinari necessari per produrre le penne in base allo stato delle isole e dei magazzini.
        Crea richieste di macchinari per i tipi 'punte', 'astucci', 'tappi' se il numero di macchinari è maggiore di zero.
        Calcola il numero di macchinari necessari per produrre le penne in base allo stato delle penne e dei magazzini.
        Crea una richiesta di macchinari per il tipo 'penne' se il numero di macchinari è maggiore di zero.
        Esegue le richieste presenti nella coda delle richieste delle isole.
        """
        magazzini = ['plastica', 'metallo', 'cartucce']
        for magazzino in magazzini:
            if self._storages[magazzino].value < 100:
                self._storages.crea_richiesta(magazzino)

        penne_da_produrre = self._richiesta_penne - self._storages['penne'].value

        n_macchinari = self.check_status_and_choose_machines(self._storages['punte'].value,
                                                             self._islands.get_consume('punte'),
                                                             self._storages['metallo'].value, penne_da_produrre)
        if n_macchinari > 0:
            self._islands.crea_richiesta('punte', n_macchinari)

        n_macchinari = self.check_status_and_choose_machines(self._storages['astucci'].value,
                                                             self._islands.get_consume('astucci'),
                                                             self._storages['plastica'].value, penne_da_produrre)
        if n_macchinari > 0:
            self._islands.crea_richiesta('astucci', n_macchinari)

        n_macchinari = self.check_status_and_choose_machines(self._storages['tappi'].value,
                                                             self._islands.get_consume('tappi'),
                                                             self._storages['plastica'].value, penne_da_produrre)
        if n_macchinari > 0:
            self._islands.crea_richiesta('tappi', n_macchinari)

        n_macchinari = round(
            (self._storages['penne'].value / (
                    self._richiesta_penne - self._storages['penne'].value)) * 40
        )
        while ((self._storages['punte'].value < n_macchinari) and (
                self._storages['tappi'].value < n_macchinari) and (
                self._storages['astucci'].value < n_macchinari) ) or (n_macchinari == 0):
            n_macchinari -= 1
        if n_macchinari > 0:
            self._islands.crea_richiesta('penne', n_macchinari)

        self._islands.esegui_richieste()

    def run(self):
        """
        Esegue il cronjob.
        Pianifica la chiamata al metodo my_task ogni secondo utilizzando la libreria schedule.
        Esegue continuamente le attività pianificate finché il programma è in esecuzione.
        """
        schedule.every(1).seconds.do(self.my_task)
        while True:
            schedule.run_pending()
            time.sleep(1)
