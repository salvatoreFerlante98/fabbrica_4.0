import schedule
import time
from controllers.islands_controller import IslandsController
from controllers.storage_controller import Storage


class Cronjob:
    def __init__(self):
        self._islands = IslandsController(1000)
        self._storages = Storage()

    def my_task(self):
        magazzini = ['plastica', 'metallo', 'cartucce']
        for magazzino in magazzini:
            if self._storages.get_magazzino(magazzino) < 100:
                self._storages.crea_richiesta()


    # Schedule the task to run every 5 minutes
    schedule.every(1).seconds.do(my_task)


# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
