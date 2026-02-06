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
    tempo_paranoia = 12000
    tempo_escuridao = 20000
    inicio_escuridao = None

    rodando = True
    while rodando:
        clock.tick(FPS)
        agora = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "sair"

        # Transições
        if not paranoia and agora - tempo_inicio > tempo_paranoia:
            paranoia = True

        if paranoia and not escuridao and agora - tempo_inicio > tempo_escuridao:
            escuridao = True
            inicio_escuridao = agora
            pygame.mixer.music.fadeout(2000)
            pygame.mixer.music.load('assets/#19.mp3')
            pygame.mixer.music.play(-1)

        # Teclas e inversão
        teclas_cru = pygame.key.get_pressed()

        teclas_normais = {
            "cima": teclas_cru[pygame.K_UP],
            "baixo": teclas_cru[pygame.K_DOWN],
            "esq": teclas_cru[pygame.K_LEFT],
            "dir": teclas_cru[pygame.K_RIGHT],
            "w": teclas_cru[pygame.K_w],
            "s": teclas_cru[pygame.K_s],
            "a": teclas_cru[pygame.K_a],
            "d": teclas_cru[pygame.K_d],
        }

        if paranoia:
            teclas = {
                "cima": teclas_normais["baixo"],
                "baixo": teclas_normais["cima"],
                "esq": teclas_normais["dir"],
                "dir": teclas_normais["esq"],
                "w": teclas_normais["s"],
                "s": teclas_normais["w"],
                "a": teclas_normais["d"],
                "d": teclas_normais["a"],
            }
        else:
            teclas = teclas_normais

        protagonista.atualizar(teclas)

        tela.blit(fundo, (0, 0))
        protagonista.desenhar(tela)

        # Paranoia
        if paranoia:
            dx = random.randint(-4, 4)
            dy = random.randint(-4, 4)
            copia = tela.copy()
            tela.blit(copia, (dx, dy))

            overlay = pygame.Surface((X, Y), pygame.SRCALPHA)
            overlay.fill((120, 0, 0, 80))
            tela.blit(overlay, (0, 0))

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