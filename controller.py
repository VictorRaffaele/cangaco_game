import arcade
from mapa import *
from personagem import *

MOVIMENTACAO = 2
PULO = 8

MAIN = 0
INTRODUCAO = 1
JOGANDO = 2
FIM = 3
map = Mapa()

class Controller():
    def controller_setup(self):

        self.fundo = arcade.load_texture("sprite_telas/vegetacaocaatinga.JPG")

        # Config default do jogo
        self.estado_jogo = MAIN
        self.tempo_total = 0.0
        self.pontuacao = 15
        self.pause = False
        self.visao_lados = 0
        self.visao_superficie = 0

        # Personagem
        self.character_list = arcade.SpriteList()
        self.piso_list = arcade.SpriteList()
        self.parede_list = arcade.SpriteList()

        self.character = Personagem(90, 20)

        # Sprite do personagem
        self.character.stand_right_textures = []
        self.character.stand_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro3.png",
                                                                       scale=self.character.escala))

        self.character.stand_left_textures = []
        self.character.stand_left_textures.append(arcade.load_texture("sprite_boneco/cangaceiro3.png",
                                                                      scale=self.character.escala, mirrored=True))

        self.character.walk_right_textures = []
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro4.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro4.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro4.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro4.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro5.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro5.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro5.png",
                                                                      scale=self.character.escala))
        self.character.walk_right_textures.append(arcade.load_texture("sprite_boneco/cangaceiro5.png",
                                                                      scale=self.character.escala))


        self.character.walk_left_textures = []

        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro4.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro4.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro4.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro4.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro5.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro5.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro5.png", scale=self.character.escala, mirrored=True))
        self.character.walk_left_textures.append(
            arcade.load_texture("sprite_boneco/cangaceiro5.png", scale=self.character.escala, mirrored=True))


        self.character.center_x = self.character.centro_x
        self.character.center_y = self.character.centro_y
        self.character_list.append(self.character)

        # Moeda
        escala_moeda = 0.1
        coin = "sprite_coin/coin.png"
        self.moeda_list = arcade.SpriteList()

        moeda1 = arcade.Sprite(coin, escala_moeda, center_x=450, center_y=230)
        moeda2 = arcade.Sprite(coin, escala_moeda, center_x=900, center_y=230)
        moeda3 = arcade.Sprite(coin, escala_moeda, center_x=1500, center_y=270)
        moeda4 = arcade.Sprite(coin, escala_moeda, center_x=1700, center_y=400)
        moeda5 = arcade.Sprite(coin, escala_moeda, center_x=1700, center_y=600)
        moeda6 = arcade.Sprite(coin, escala_moeda, center_x=980, center_y=600)
        moeda7 = arcade.Sprite(coin, escala_moeda, center_x=700, center_y=500)
        moeda8 = arcade.Sprite(coin, escala_moeda, center_x=100, center_y=550)
        moeda9 = arcade.Sprite(coin, escala_moeda, center_x=420, center_y=800)
        moeda10 = arcade.Sprite(coin, escala_moeda, center_x=660, center_y=850)
        moeda11 = arcade.Sprite(coin, escala_moeda, center_x=980, center_y=850)
        moeda12 = arcade.Sprite(coin, escala_moeda, center_x=1240, center_y=800)
        moeda13 = arcade.Sprite(coin, escala_moeda, center_x=1370, center_y=850)
        moeda14 = arcade.Sprite(coin, escala_moeda, center_x=1700, center_y=730)
        moeda15 = arcade.Sprite(coin, escala_moeda, center_x=1700, center_y=850)

        self.moeda_list.append(moeda1)
        self.moeda_list.append(moeda2)
        self.moeda_list.append(moeda3)
        self.moeda_list.append(moeda4)
        self.moeda_list.append(moeda5)
        self.moeda_list.append(moeda6)
        self.moeda_list.append(moeda7)
        self.moeda_list.append(moeda8)
        self.moeda_list.append(moeda9)
        self.moeda_list.append(moeda10)
        self.moeda_list.append(moeda11)
        self.moeda_list.append(moeda12)
        self.moeda_list.append(moeda13)
        self.moeda_list.append(moeda14)
        self.moeda_list.append(moeda15)

        # Botao
        self.button_list = []

        # Chao
        mapa = map.montar_mapa("sprite_telas/caatinga.csv")

        for k in range(len(mapa)):
            for i in range(len(mapa[k])):
                item = mapa[k][i]

                if item == 19:
                    piso = arcade.Sprite("tile/1.png", scale=1.5)
                elif item == 20:
                    piso = arcade.Sprite("tile/2.png", scale=1.5)
                elif item == 21:
                    piso = arcade.Sprite("tile/3.png", scale=1.5)
                elif item == 22:
                    piso = arcade.Sprite("tile/4.png", scale=1.5)
                elif item == 23:
                    piso = arcade.Sprite("tile/5.png", scale=1.5)
                elif item == 24:
                    piso = arcade.Sprite("tile/6.png", scale=1.5)
                elif item == 25:
                    piso = arcade.Sprite("tile/7.png", scale=1.5)
                elif item == 26:
                    piso = arcade.Sprite("tile/8.png", scale=1.5)
                elif item == 27:
                    piso = arcade.Sprite("tile/9.png", scale=1.5)
                elif item == 28:
                    piso = arcade.Sprite("tile/10.png", scale=1.5)
                elif item == 29:
                    piso = arcade.Sprite("tile/11.png", scale=1.5)
                elif item == 30:
                    piso = arcade.Sprite("tile/13.png", scale=1.5)
                elif item == 31:
                    piso = arcade.Sprite("tile/14.png", scale=1.5)
                elif item == 32:
                    piso = arcade.Sprite("tile/15.png", scale=1.5)
                elif item == 33:
                    piso = arcade.Sprite("tile/16.png", scale=1.5)

                if item >= 19:
                    piso.left = i * 64
                    piso.top = (15 - k) * 64
                    if item == 22 or item == 24:
                        self.parede_list.append(piso)
                    else:
                        self.piso_list.append(piso)

        # Fisica
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.character, self.piso_list, 0.7)
        self.physics_piso = arcade.PhysicsEnginePlatformer(self.character, self.parede_list, 0.1)

    def controller_uptade(self, desenhar_jogo, MARGEM_VIEW, LARGURA_TELA, ALTURA_TELA, delta_time):

        if self.estado_jogo == JOGANDO:

            #atualizacao de imagens
            self.physics_engine.update()
            self.physics_piso.update()
            self.character_list.update()
            self.character_list.update_animation()
            self.moeda_list.update()
            self.tempo_total += delta_time

            #coleta de moeda
            hit_list = arcade.check_for_collision_with_list(self.character, self.moeda_list)

            for moeda in hit_list:
                moeda.kill()
                self.pontuacao -= 1

            changed = False

            #Movimentacao da tela
            borda_esquerda = self.visao_lados + MARGEM_VIEW
            if self.character.left < borda_esquerda:
                self.visao_lados -= borda_esquerda - self.character.left
                changed = True

            borda_direita = self.visao_lados + LARGURA_TELA - MARGEM_VIEW
            if self.character.right > borda_direita:
                self.visao_lados += self.character.right - borda_direita
                changed = True

            borda_cima = self.visao_superficie + ALTURA_TELA - MARGEM_VIEW
            if self.character.top > borda_cima:
                self.visao_superficie += self.character.top - borda_cima
                changed = True

            borda_baixo = self.visao_superficie + 50
            if self.character.bottom < borda_baixo:
                self.visao_superficie -= borda_baixo - self.character.bottom
                changed = True

            self.visao_lados = int(self.visao_lados)
            self.visao_superficie = int(self.visao_superficie)

            if changed:
                arcade.set_viewport(self.visao_lados, LARGURA_TELA + self.visao_lados - 1, self.visao_superficie,
                                    ALTURA_TELA + self.visao_superficie - 1)

            if self.pontuacao > 0:
                desenhar_jogo()
            else:
                self.estado_jogo = FIM
                self.board()

    def controller_key(self, key):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.character.change_y = PULO
        elif key == arcade.key.DOWN:
            self.character.change_y = - MOVIMENTACAO
        elif key == arcade.key.LEFT:
            self.character.change_x = - MOVIMENTACAO
        elif key == arcade.key.RIGHT:
            self.character.change_x = MOVIMENTACAO


    def controller_release(self, key):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.character.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.character.change_x = 0

    def controller_mouse(self):
        if self.estado_jogo == MAIN:
            self.estado_jogo = INTRODUCAO

        elif self.estado_jogo == INTRODUCAO:
            arcade.load_sound("gaita.mp3")
            arcade.play_sound("gaita.mp3")
            self.estado_jogo = JOGANDO

        elif self.estado_jogo == FIM:
            self.controller_setup()
            self.estado_jogo = INTRODUCAO

    def board(self):
        self.lista = open("melhor_tempo.txt", "a")
        self.lista.write(str(self.tempo_total) + "\n")
        self.lista.close()

