from window import Window
from obj import Obj

class Game:

    def __init__(self):
        self.tela = Window(1280, 720, "Pong Futeball")

        self.bg = Obj("assets/field.png", 0, 0)
        self.tela.add_obj(self.bg.drawing(self.tela.window))

        self.player1 = Obj("assets/player1.png", 50, 300)
        self.tela.add_obj(self.player1.drawing(self.tela.window))

Game().tela.updates()