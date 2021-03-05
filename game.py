import arcade
from view import View

class Cangaco_game():
    def main(self):
        window = View()
        window.setup()
        arcade.run()

start = Cangaco_game()
start.main()
