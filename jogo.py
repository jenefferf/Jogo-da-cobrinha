import pygame
import sys
from cobra import Cobra
from comida import Comida
import time

# iniciar fonte
pygame.font.init()
minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)

# iniciciando o pygame
pygame.init()
TAM_TELA = (300, 400)
tela = pygame.display.set_mode(TAM_TELA)
tempo = pygame.time.Clock()
cobra = Cobra()
comida = Comida()
pos_comida = comida.posicao
pontuacao = 0

# iniciando o loop do jogo
while True:

    tela.fill((7, 0, 35))  # RGB - Red, Green, Blue

    for evento in pygame.event.get():
        # listener - mouse ou teclado
        if evento.type == pygame.QUIT:
            # interrompe pygame
            pygame.quit()
            # fechar o script
            sys.exit()

        # se uma tecla for pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                cobra.muda_direcao('DIREITA')
            if evento.key == pygame.K_LEFT:
                cobra.muda_direcao('ESQUERDA')
            if evento.key == pygame.K_UP:
                cobra.muda_direcao('CIMA')
            if evento.key == pygame.K_DOWN:
                cobra.muda_direcao('BAIXO')

    pos_comida = comida.gera_nova_comida()

    # se a cobra comeu a comida:
    if cobra.move(pos_comida):
        comida.devorada = True
        pontuacao += 1

    if cobra.verfica_colisao():
        perdeu = minha_fonte.render("Você perdeu!", True, (255, 255, 255))
        pontos = minha_fonte.render(
            f'Pontuação {pontuacao}', True, (255, 255, 255))
        tela.blit(pontos, (10, 10))
        tela.blit(perdeu, (80, 180))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # texto de pontuação
    pontos = minha_fonte.render(
        f'Pontuação {pontuacao}', True, (255, 255, 255))
    tela.blit(pontos, (10, 10))

    # desenha a cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255, 204, 0),
                         #esquerda, cima, largura,altura
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # desenha comida
    pygame.draw.rect(tela, pygame.Color(255, 0, 0),
                     pygame.Rect(pos_comida[0], pos_comida[1], 10, 10))

    # atualiza a tela a cada frame
    pygame.display.update()

    # Frames
    tempo.tick(30)
