import pygame
from config import X, Y, FPS, CAPTION
from personagens import Protagonista, Ceifador
from telas import tela_inicial

pygame.init()
fullscreen = True
tela = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
pygame.mixer.music.play(-1)

# Fundo
fundo = pygame.image.load('assets/image.11.png').convert_alpha()
fundo = pygame.transform.scale(fundo, (X, Y))

protagonista = Protagonista()
monstro = Ceifador()
monstros_mortos = 0
max_monstros = 3
tela_inicial(tela)

rodando = True
while rodando:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                fullscreen = not fullscreen
                if fullscreen:
                    tela = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
                else:
                    tela = pygame.display.set_mode((X, Y))

    tela.blit(fundo, (0, 0))

    # Monstro
    if monstros_mortos < max_monstros and monstro.vivo:
        monstro.atualizar()
        monstro.desenhar(tela)
        if monstro.posi[0] > 1200:
            monstros_mortos += 1
            monstro.vivo = False
    elif monstros_mortos < max_monstros:
        monstro = Ceifador()

    teclas = pygame.key.get_pressed()
    protagonista.atualizar(teclas)
    protagonista.desenhar(tela)

    pygame.display.update()