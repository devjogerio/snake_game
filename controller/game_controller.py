import pygame
import sys
from model.snake import Snake
from model.food import Food
from view.view import View, Button

LARGURA = 600
ALTURA = 400
TAMANHO_BLOCO = 20
FPS = 8  # Velocidade reduzida


class GameController:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Jogo da Cobrinha')
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont('arial', 25)
        self.view = View(LARGURA, ALTURA, self.fonte)
        self.estado = 'NOME'  # Novo estado inicial
        self.pontuacao = 0
        self.snake = None
        self.food = None
        self.rodando = True
        self.nome_usuario = ''
        self.digitando_nome = True

    def iniciar_jogo(self):
        self.snake = Snake(LARGURA, ALTURA, TAMANHO_BLOCO)
        self.food = Food(LARGURA, ALTURA, TAMANHO_BLOCO)
        self.pontuacao = 0
        self.estado = 'JOGO'

    def sair(self):
        pygame.quit()
        sys.exit()

    def reiniciar(self):
        self.iniciar_jogo()

    def loop(self):
        while self.rodando:
            if self.estado == 'NOME':
                self.tela.fill((255, 255, 255))
                self.view.mostrar_texto(
                    self.tela, 'Digite seu nome:', (0, 0, 0), 100)
                self.view.mostrar_texto(
                    self.tela, self.nome_usuario + ('|' if self.digitando_nome else ''), (0, 0, 255), 150)
                pygame.display.update()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.rodando = False
                    elif evento.type == pygame.KEYDOWN and self.digitando_nome:
                        if evento.key == pygame.K_RETURN and len(self.nome_usuario) > 0:
                            self.estado = 'INICIO'
                        elif evento.key == pygame.K_BACKSPACE:
                            self.nome_usuario = self.nome_usuario[:-1]
                        elif len(self.nome_usuario) < 15:
                            if evento.unicode.isprintable() and not evento.unicode.isspace():
                                self.nome_usuario += evento.unicode
            elif self.estado == 'INICIO':
                botao_jogar = Button(
                    'Jogar', 200, 150, 200, 50, (200, 200, 200), (0, 255, 0), self.iniciar_jogo, self.fonte)
                botao_sair = Button(
                    'Sair', 200, 220, 200, 50, (200, 200, 200), (255, 0, 0), self.sair, self.fonte)
                self.view.tela_inicial(
                    self.tela, botao_jogar, botao_sair, self.nome_usuario)
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.rodando = False
            elif self.estado == 'JOGO':
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.rodando = False
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_UP:
                            self.snake.mudar_direcao('CIMA')
                        elif evento.key == pygame.K_DOWN:
                            self.snake.mudar_direcao('BAIXO')
                        elif evento.key == pygame.K_LEFT:
                            self.snake.mudar_direcao('ESQUERDA')
                        elif evento.key == pygame.K_RIGHT:
                            self.snake.mudar_direcao('DIREITA')
                self.snake.mover()
                if self.snake.corpo[0] == self.food.posicao:
                    self.snake.crescer = True
                    self.food.nova_posicao()
                    self.pontuacao += 1
                if self.snake.colidiu():
                    self.estado = 'GAME_OVER'
                self.tela.fill((255, 255, 255))
                self.view.desenhar_comida(self.tela, self.food.posicao)
                self.view.desenhar_cobrinha(self.tela, self.snake.corpo)
                self.view.mostrar_texto(
                    self.tela, f'Pontuação: {self.pontuacao}', (0, 0, 0), 10)
                self.view.mostrar_texto(
                    self.tela, f'Jogador: {self.nome_usuario}', (0, 0, 128), 40)
                pygame.display.update()
                self.clock.tick(FPS)
            elif self.estado == 'GAME_OVER':
                botao_reiniciar = Button(
                    'Reiniciar', 200, 180, 200, 50, (200, 200, 200), (0, 255, 0), self.reiniciar, self.fonte)
                botao_sair = Button(
                    'Sair', 200, 250, 200, 50, (200, 200, 200), (255, 0, 0), self.sair, self.fonte)
                self.view.tela_game_over(
                    self.tela, botao_reiniciar, botao_sair, self.pontuacao, self.nome_usuario)
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.rodando = False
        pygame.quit()


if __name__ == '__main__':
    GameController().loop()
