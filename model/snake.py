import random


class Snake:
    def __init__(self, largura, altura, tamanho_bloco):
        self.largura = largura
        self.altura = altura
        self.tamanho_bloco = tamanho_bloco
        self.corpo = [[largura // 2, altura // 2]]
        self.direcao = 'DIREITA'
        self.crescer = False

    def mover(self):
        x, y = self.corpo[0]
        if self.direcao == 'CIMA':
            y -= self.tamanho_bloco
        elif self.direcao == 'BAIXO':
            y += self.tamanho_bloco
        elif self.direcao == 'ESQUERDA':
            x -= self.tamanho_bloco
        elif self.direcao == 'DIREITA':
            x += self.tamanho_bloco
        novo_cabeca = [x, y]
        self.corpo.insert(0, novo_cabeca)
        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def mudar_direcao(self, direcao):
        opostos = {'CIMA': 'BAIXO', 'BAIXO': 'CIMA',
                   'ESQUERDA': 'DIREITA', 'DIREITA': 'ESQUERDA'}
        if direcao != opostos.get(self.direcao):
            self.direcao = direcao

    def colidiu(self):
        x, y = self.corpo[0]
        if x < 0 or x >= self.largura or y < 0 or y >= self.altura:
            return True
        if self.corpo[0] in self.corpo[1:]:
            return True
        return False
