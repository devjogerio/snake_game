import pygame

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
CINZA = (200, 200, 200)


class Button:
    def __init__(self, texto, x, y, largura, altura, cor, cor_hover, acao=None, fonte=None):
        self.texto = texto
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.cor_hover = cor_hover
        self.acao = acao
        self.fonte = fonte

    def desenhar(self, tela):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cor_atual = self.cor_hover if self.rect.collidepoint(
            mouse) else self.cor
        pygame.draw.rect(tela, cor_atual, self.rect)
        if self.fonte:
            texto_render = self.fonte.render(self.texto, True, PRETO)
            tela.blit(texto_render, (self.rect.x + (self.rect.width - texto_render.get_width()) // 2,
                                     self.rect.y + (self.rect.height - texto_render.get_height()) // 2))
        if self.rect.collidepoint(mouse) and click[0] == 1 and self.acao:
            self.acao()


class View:
    def __init__(self, largura, altura, fonte):
        self.largura = largura
        self.altura = altura
        self.fonte = fonte

    def desenhar_fundo_3d(self, tela):
        # Gradiente de fundo
        for i in range(self.altura):
            cor = (
                30 + int(80 * i / self.altura),
                30 + int(80 * i / self.altura),
                60 + int(120 * i / self.altura)
            )
            pygame.draw.line(tela, cor, (0, i), (self.largura, i))
        # Cubos 3D fake
        bloco = 40
        for y in range(0, self.altura, bloco):
            for x in range(0, self.largura, bloco):
                # Sombra lateral
                pygame.draw.polygon(tela, (40, 40, 60), [
                    (x, y), (x+bloco, y), (x+bloco-8, y+bloco-8), (x-8, y+bloco-8)
                ])
                # Topo do cubo
                pygame.draw.polygon(tela, (70, 70, 120), [
                    (x, y), (x+bloco, y), (x+bloco, y+bloco), (x, y+bloco)
                ])
                # Borda para dar efeito
                pygame.draw.line(tela, (100, 100, 180),
                                 (x, y), (x+bloco, y), 2)
                pygame.draw.line(tela, (50, 50, 90),
                                 (x, y+bloco), (x+bloco, y+bloco), 2)

    def mostrar_texto(self, tela, texto, cor, y):
        texto_render = self.fonte.render(texto, True, cor)
        tela.blit(texto_render,
                  ((self.largura - texto_render.get_width()) // 2, y))

    def desenhar_cobrinha(self, tela, corpo):
        for parte in corpo:
            # Sombra para efeito 3D
            pygame.draw.rect(tela, (0, 120, 0),
                             (parte[0]+3, parte[1]+3, 20, 20), border_radius=6)
            pygame.draw.rect(
                tela, VERDE, (parte[0], parte[1], 20, 20), border_radius=6)

    def desenhar_comida(self, tela, posicao):
        # Sombra para efeito 3D
        pygame.draw.ellipse(tela, (120, 0, 0),
                            (posicao[0]+2, posicao[1]+2, 20, 20))
        pygame.draw.ellipse(tela, VERMELHO, (posicao[0], posicao[1], 20, 20))

    def tela_inicial(self, tela, botao_jogar, botao_sair, nome_usuario=None):
        tela.fill(BRANCO)
        self.mostrar_texto(tela, 'Jogo da Cobrinha', PRETO, 60)
        if nome_usuario:
            self.mostrar_texto(
                tela, f'Jogador: {nome_usuario}', (0, 0, 128), 110)
        botao_jogar.desenhar(tela)
        botao_sair.desenhar(tela)
        pygame.display.update()

    def tela_game_over(self, tela, botao_reiniciar, botao_sair, pontuacao, nome_usuario=None):
        self.desenhar_fundo_3d(tela)
        self.mostrar_texto(tela, 'Game Over', VERMELHO, 60)
        if nome_usuario:
            self.mostrar_texto(
                tela, f'Jogador: {nome_usuario}', (0, 0, 128), 90)
        self.mostrar_texto(tela, f'Pontuação: {pontuacao}', PRETO, 120)
        botao_reiniciar.desenhar(tela)
        botao_sair.desenhar(tela)
        pygame.display.update()
