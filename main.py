import threading
from controllers.userController import UserController
from controllers.IslandsController import IslandsController
from controllers.StorageController import StorageController
from CronJob import Cronjob
from services.UserService import UserService

island_controller = IslandsController()
storage_controller = StorageController()
user_controller = UserController()

cronjob = Cronjob(island_controller, storage_controller)
cronjobThread = threading.Thread(target=cronjob.run)
cronjobThread.start()

userService = UserService(island_controller, storage_controller, user_controller)
userService.run()
