import pygame
from config import X, Y

def tela_inicial(tela):
    imagem_inicial = pygame.image.load('assets/Tela_inicial.png')
    imagem_inicial = pygame.transform.scale(imagem_inicial, (X, Y))
    esperando = True

    while esperando:
        tela.blit(imagem_inicial, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                esperando = False