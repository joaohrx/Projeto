import pygame
from config import X, Y

def tela_inicial(tela):
    imagem_inicial = pygame.image.load('assets/Tela_inicial.png')
    imagem_inicial = pygame.transform.scale(imagem_inicial, (X, Y))

    esperando = True
    clock = pygame.time.Clock()

    while esperando:
        clock.tick(60)

        tela.blit(imagem_inicial, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            elif event.type == pygame.KEYDOWN:
                return "intro" 
