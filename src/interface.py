import tkinter as tk
from tkinter import colorchooser, messagebox


class InterfaceModelador:
    def __init__(self, root):
        self.root = root
        self.root.title = "Modelador 3D - Pipeline Alvy-Ray-Smith"

        # Configuração do Canvas
        self.largura = 800
        self.altura = 600
        self.canvas = tk.Canvas(
            root, width=self.largura, height=self.altura, bg="black"
        )

        # Inicialização da cena (lógica)
        # self.cena = Cena()
        # self.renderizador = Renderizador(self.largura, self.altura)

        # Painel de Controles
        self._criar_painel_controles()

    def _criar_painel_controles(self):
    
    def adicionar_cubo(self):

    def selecionar_objeto(self, event):

    def atualizar_cena(self):

    def renderizar_final(self):

if __name__ = "__main__":
    root = tk.Tk()
    app = InterfaceModelador(root)
    root.mainloop()
