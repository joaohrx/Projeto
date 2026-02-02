import pygame
import random
from config import X, Y, FPS
from personagens import Protagonista
import colisao
import colisaocorredor


def fase3(tela):
    clock = pygame.time.Clock()

    colisao.colisoes = colisaocorredor.colisoes

    pygame.mixer.music.load('assets/#5.mp3')
    pygame.mixer.music.play(-1)

    fundo = pygame.image.load('assets/image.11.png').convert()
    fundo = pygame.transform.scale(fundo, (X, Y))

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 40)
    fonte_intrusiva = pygame.font.Font("assets/DepartureMono-Regular.otf", 30)

    protagonista = Protagonista(posi_inicial=(500, 400))

    paranoia = False
    escuridao = False

    tempo_inicio = pygame.time.get_ticks()
    tempo_paranoia = 12000      # ms até paranoia
    tempo_escuridao = 20000     # ms até escuridão total
    inicio_escuridao = None
    


    rodando = True
    while rodando:
        clock.tick(FPS)
        agora = pygame.time.get_ticks()
        
        teclas_cru = pygame.key.get_pressed()

        teclas = {
            "cima": teclas_cru[pygame.K_DOWN],   # invertido
            "baixo": teclas_cru[pygame.K_UP],
            "esq": teclas_cru[pygame.K_RIGHT],
            "dir": teclas_cru[pygame.K_LEFT],
            "w": teclas_cru[pygame.K_s],
            "s": teclas_cru[pygame.K_w],
            "a": teclas_cru[pygame.K_d],
            "d": teclas_cru[pygame.K_a],
}

        # Transições
        if not paranoia and agora - tempo_inicio > tempo_paranoia:
            paranoia = True

        if paranoia and not escuridao and agora - tempo_inicio > tempo_escuridao:
            escuridao = True
            inicio_escuridao = agora
            pygame.mixer.music.fadeout(2000)
            pygame.mixer.music.load('assets/#19.mp3')
            pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "sair"

        teclas_cru = pygame.key.get_pressed()

        # Controles invertidos
        protagonista.atualizar(teclas)

        tela.blit(fundo, (0, 0))
        protagonista.desenhar(tela)

        # Efeitos visuais
        if paranoia:
            # tremor
            dx = random.randint(-4, 4)
            dy = random.randint(-4, 4)
            copia = tela.copy()
            tela.blit(copia, (dx, dy))

            # overlay vermelho
            overlay = pygame.Surface((X, Y), pygame.SRCALPHA)
            overlay.fill((120, 0, 0, 80))
            tela.blit(overlay, (0, 0))

            # texto intrusivo ocasional
            if random.randint(0, 120) == 0:
                msg = random.choice(["VOLTE", "NÃO CORRA", "ELES ESTÃO AQUI"])
                texto = fonte_intrusiva.render(msg, True, (255, 255, 255))
                tela.blit(texto, texto.get_rect(center=(X // 2, Y // 2)))

        # Escuridão
        if escuridao:
            delta = agora - inicio_escuridao
            alpha = min(delta // 15, 255)

            sombra = pygame.Surface((X, Y))
            sombra.fill((0, 0, 0))
            sombra.set_alpha(alpha)
            tela.blit(sombra, (0, 0))

            if alpha >= 255:
                return "final"

        pygame.display.update()