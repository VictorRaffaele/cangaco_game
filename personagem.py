import arcade

class Personagem(arcade.AnimatedWalkingSprite):
    def __init__(self, x, y):
        super().__init__()
        self.escala = 0.02
        self.centro_x = x
        self.centro_y = y
