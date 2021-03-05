import arcade

class Mapa():
    def montar_mapa(self, nome_arquivo):
        imagem_mapa = open(nome_arquivo)
        lista_mapa = []

        for k in imagem_mapa:
            k = k.strip()
            fila_mapa = k.split(",")

            for i, l in enumerate(fila_mapa):
                fila_mapa[i] = int(l)

            lista_mapa.append(fila_mapa)
        return lista_mapa
