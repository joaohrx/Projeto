import pygame
import random



pygame.init()
#tela
x = 1280
y = 720
tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('ECOS')
#carregar background
fundo = pygame.image.load('assets/image.1.png').convert_alpha()
fundo = pygame.transform.scale(fundo, (x, y))
#carregar monstros
monstro_img = pygame.image.load('assets/monstro.png').convert_alpha()
monstro_img = pygame.transform.scale(monstro_img, (200, 200))


#respawn de montros
def respawn():
    x = -200
    y = 200
    return [x, y]


monstros_mortos = 0
monstro_vivo = True
pos_monstro = respawn() # o respawn já está definido nos tamanhos x,y
max_monstros = 3

#velocidade do monstro
velocidade = 0.5


#sistema de rodar
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.blit(fundo, (0, 0))

#sistema de morte de monstros após 3 spawns 
    if monstros_mortos < max_monstros and monstro_vivo:
        pos_monstro[0] += velocidade
        tela.blit(monstro_img, pos_monstro)

        
        if pos_monstro[0] > 1300:
            monstros_mortos += 1
            monstro_vivo = False

   
    if not monstro_vivo and monstros_mortos < max_monstros:
        pos_monstro = respawn()
        monstro_vivo = True

    pygame.display.update()



