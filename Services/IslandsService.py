import tkinter as tk

from controllers.daos.isola import Isola


class IslandService:
    def __init__(self, island: Isola, magazzino):
        self.logout_button = None
        self.logout_layout = None
        self.opera_button = None
        self.button_layout = None
        self.status_layout = None
        self.label_layout = None
        self.vertical_layout = None
        self.central_widget = None
        self.menu_bar = None
        self.root = tk.Tk()
        self.root.title("MainWindow")
        self.create_widgets()
        self._island = island
        self.magazzino = magazzino

    def create_widgets(self):
        self.central_widget = tk.Frame(self.root)
        self.central_widget.pack()

        self.vertical_layout = tk.Frame(self.central_widget)
        self.vertical_layout.pack()

        self.label_layout = tk.Frame(self.vertical_layout)
        self.label_layout.pack()

        label_texts = ["Macchinario 1", "Macchinario 2", "Macchinario 3", "Macchinario 4"]
        for text in label_texts:
            label = tk.Label(self.label_layout, text=text)
            label.pack(side=tk.LEFT)

        self.status_layout = tk.Frame(self.vertical_layout)
        self.status_layout.pack()

        status_texts = self._island.get_status_macchinari()
        for text in status_texts:
            status_label = tk.Label(self.status_layout, text=text)
            status_label.pack(side=tk.LEFT)

        self.button_layout = tk.Frame(self.central_widget)
        self.button_layout.pack()

        self.opera_button = tk.Button(self.button_layout, text="Opera macchinario", command=self.opera_macchinario)
        self.opera_button.pack()

    def opera_macchinario(self):
        if self._island.get_nome() != 'penne':
            self.magazzino -= self._island.get_consumo()
        else:
            for magazzino in self.magazzino:
                magazzino -= 1
        self._island.opera_macchinario()

    def run(self):
        self.root.mainloop()
