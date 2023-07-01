import PySimpleGUI as sg
from controllers.daos.isola import Isola


class IslandService:
    def __init__(self, island: Isola, magazzino_materiale, magazzino_produzione):
        self.island = island
        self.magazzino_materiale = magazzino_materiale
        self.magazzino_produzione = magazzino_produzione

    def run(self):
        layout = [
            [sg.Text("Macchinario 1"), sg.Text(self.island.get_status_macchinari()[0])],
            [sg.Text("Macchinario 2"), sg.Text(self.island.get_status_macchinari()[1])],
            [sg.Text("Macchinario 3"), sg.Text(self.island.get_status_macchinari()[2])],
            [sg.Text("Macchinario 4"), sg.Text(self.island.get_status_macchinari()[3])],
            [sg.Button("Opera macchinario")]
        ]

        window = sg.Window("Island Service", layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Opera macchinario":
                if 'On' in self.island.get_status_macchinari():
                    if self.island.get_nome() != 'penne':
                        self.magazzino_materiale.value = self.magazzino_materiale.value - self.island.get_consumo()
                    else:
                        for magazzino in self.magazzino_materiale:
                            magazzino -= 1
                    self.island.opera_macchinario()
                    self.magazzino_produzione.value = self.magazzino_produzione.value + 1
                window.refresh()

        window.close()
