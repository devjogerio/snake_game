import random


class Food:
    def __init__(self, largura, altura, tamanho_bloco):
        self.largura = largura
        self.altura = altura
        self.tamanho_bloco = tamanho_bloco
        self.posicao = self.gerar_posicao()

    def gerar_posicao(self):
        x = random.randrange(0, self.largura, self.tamanho_bloco)
        y = random.randrange(0, self.altura, self.tamanho_bloco)
        return [x, y]

    def nova_posicao(self):
        self.posicao = self.gerar_posicao()
