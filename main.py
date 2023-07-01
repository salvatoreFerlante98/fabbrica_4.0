import threading
from controllers.userController import UserController
from controllers.IslandsController import IslandsController
from controllers.StorageController import StorageController
from CronJob import Cronjob
from services.UserService import UserService

# Creazione delle istanze dei controller e del servizio
island_controller = IslandsController()
storage_controller = StorageController()
user_controller = UserController()

# Creazione dell'oggetto Cronjob e avvio del thread per l'esecuzione periodica
cronjob = Cronjob(island_controller, storage_controller)
cronjobThread = threading.Thread(target=cronjob.run)
cronjobThread.start()

# Creazione dell'oggetto UserService e avvio del programma principale
userService = UserService(island_controller, storage_controller, user_controller)
userService.run()
