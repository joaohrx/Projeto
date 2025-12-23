import pygame
from config import X, Y, FPS
from personagens import Protagonista
import colisao
import colisaocorredor

def fase3(tela):
    clock = pygame.time.Clock()

    colisao.colisoes = colisaocorredor.colisoes

    pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
    pygame.mixer.music.play(-1)

    
    fundo_fase2 = pygame.image.load('assets/image.11.png').convert()
    fundo_fase2 = pygame.transform.scale(fundo_fase2, (X, Y))

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 40)

    protagonista = Protagonista(posi_inicial=(500, 400))

    rodando = True

    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "sair"


        teclas = pygame.key.get_pressed()
        protagonista.atualizar(teclas)

       
        tela.blit(fundo_fase2, (0, 0))

        protagonista.desenhar(tela)

        pygame.display.update()