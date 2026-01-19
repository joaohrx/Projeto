import pygame
from config import X, Y, FPS
from personagens import Protagonista
import colisao
import colisaocorredor
from audio import *
stream = None

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
    
    stream = iniciar_microfone()
    
    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if stream:
                    stream.stop()
                    stream.close()
                return "sair"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if stream:
                        stream.stop()
                        stream.close()
                    return "sair"


        teclas = pygame.key.get_pressed()
        
        if stream:
            volume = pegar_volume()
        else:
            volume = 0           
        lanterna_ligada = volume > 0.25
        protagonista.atualizar(teclas, lanterna_ligada)

       
        tela.blit(fundo_fase2, (0, 0))

        protagonista.desenhar(tela)
        
        pygame.display.update()