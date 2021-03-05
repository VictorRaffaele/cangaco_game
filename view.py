import arcade
import os
import random
from mapa import *
from controller import *

LARGURA_TELA= 800
ALTURA_TELA = 600
MARGEM_VIEW = 200

con = Controller()
class View(arcade.Window):

    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, fullscreen = False)
        arcade.set_background_color(arcade.color.BROWN_NOSE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        largura, altura = self.get_size()
        self.set_viewport(0, largura, 0, altura)
        self.is_full_screen = True

    def setup(self):
        con.controller_setup()

    def tela_home(self):
        self.home = arcade.load_texture("sprite_telas/main.png")
        arcade.draw_texture_rectangle(LARGURA_TELA / 2, ALTURA_TELA / 2, LARGURA_TELA, ALTURA_TELA, self.home)

    def tela_intro(self):
        self.intro = arcade.load_texture("sprite_telas/introducao.png")
        arcade.draw_texture_rectangle(LARGURA_TELA / 2, ALTURA_TELA / 2, LARGURA_TELA, ALTURA_TELA, self.intro)

    #Visual do jogo
    def desenhar_jogo(self):
        left, largura_tela, bottom, altura_tela = self.get_viewport()
        self.fundo = arcade.load_texture("sprite_telas/vegetacaocaatinga.JPG")
        minutos = int(con.tempo_total) // 60
        segundos = int(con.tempo_total) % 60

        pontos = f"Moedas Restantes: {con.pontuacao}"
        relogio = f"Tempo: {minutos:02d}:{segundos:02d}"
        arcade.draw_texture_rectangle(LARGURA_TELA * 1.13, ALTURA_TELA / 1.25, 1700, 850,
                                      self.fundo)
        con.character_list.draw()
        con.piso_list.draw()
        con.parede_list.draw()
        con.moeda_list.draw()
        arcade.draw_text(pontos, largura_tela - 780, altura_tela - 580, arcade.color.BLACK, 10, bold=True)
        arcade.draw_text(relogio, largura_tela - 115, altura_tela - 50, arcade.color.BLACK)

    def fim_de_jogo(self):
        left, largura_tela, bottom, altura_tela = self.get_viewport()

        mensagem = "Fim de Jogo"
        novamente = "Clique para jogar novamente"

        arcade.draw_text(mensagem, con.character.center_x - 330, con.character.center_y, arcade.color.BLACK, 54)
        arcade.draw_text(novamente, con.character.center_x - 330, con.character.center_y - 70, arcade.color.BLACK, 24)

    #Mostrar na tela
    def on_draw(self):
        arcade.start_render()

        if con.estado_jogo == MAIN:
            self.tela_home()

        elif con.estado_jogo == INTRODUCAO:
            self.tela_intro()

        elif con.estado_jogo == JOGANDO:
            self.desenhar_jogo()

        if con.estado_jogo == FIM:
            self.pause = True
            self.desenhar_jogo()
            self.fim_de_jogo()

        for botao in con.button_list:
            botao.draw()

    #Atualização de quadros
    def update(self, delta_time):
        con.controller_uptade(self.desenhar_jogo, MARGEM_VIEW, LARGURA_TELA, ALTURA_TELA, delta_time)


    # Movimentacao
    def on_key_press(self, key, modifiers):
        con.controller_key(key)

        if key == arcade.key.F11:
            self.is_full_screen = not self.is_full_screen
            self.set_fullscreen(self.is_full_screen)

            left, largura_tela, bottom, altura_tela = self.get_viewport()
            self.set_viewport(0, largura_tela, 0, altura_tela)


    #cliques
    def on_key_release(self, key, modifiers):
        con.controller_release(key)

    def on_mouse_press(self, x, y, button, key_modifiers):
        con.controller_mouse()

