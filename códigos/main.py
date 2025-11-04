import pygame
from config import X, Y, FPS, CAPTION
from personagens import Protagonista, Ceifador
from telas import tela_inicial
from colisao import colisoes

pygame.init()
fullscreen = True
tela = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
pygame.mixer.music.play(-1)

# Fundos
fundo_menu = pygame.image.load('assets/telainicial.png').convert()
fundo_menu = pygame.transform.scale(fundo_menu, (X, Y))

fundo_jogo = pygame.image.load('assets/Mapaa.png').convert()
fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))

protagonista = Protagonista()
monstro = Ceifador()
monstros_mortos = 0
max_monstros = 3

tela_inicial(tela)

def transicao_fade(tela, img_saida, img_entrada, duracao=1500):
    clock = pygame.time.Clock()
    fade_surface = pygame.Surface((X, Y))
    fade_surface.fill((0, 0, 0))

    for alpha in range(0, 255, 10):
        tela.blit(img_saida, (0, 0))
        fade_surface.set_alpha(alpha)
        tela.blit(fade_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

    for alpha in range(255, -1, -10):
        tela.blit(img_entrada, (0, 0))
        fade_surface.set_alpha(alpha)
        tela.blit(fade_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

transicao_fade(tela, fundo_menu, fundo_jogo, duracao=1500)

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

    tela.blit(fundo_jogo, (0, 0))

    if monstros_mortos < max_monstros and monstro.vivo:
        monstro.atualizar(None)
        monstro.desenhar(tela)
        if monstro.posi[0] > 1200:
            monstros_mortos += 1
            monstro.vivo = False
    elif monstros_mortos < max_monstros:
        monstro = Ceifador()

    teclas = pygame.key.get_pressed()
    protagonista.atualizar(teclas)
    protagonista.desenhar(tela)

    for c in colisoes:
        pygame.draw.rect(tela, (255, 0, 0), c, 2)

    pygame.display.update()
