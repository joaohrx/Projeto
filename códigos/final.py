import pygame
from config import *
import math

def final(tela):
    clock = pygame.time.Clock()

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 20)
    fonteLogo = pygame.font.Font("assets/Faith_Collapsing.ttf", 140)

    pygame.mixer.music.load("assets/#19.mp3")
    pygame.mixer.music.play(-1)

    linhas = [
        "TEXTO NARRATIVO / CONTEXTO HISTÓRICO",
        "",
        "Linha narrativa 1...",
        "Linha narrativa 2...",
        "Linha narrativa 3...",
        "",
        "",
        "CRÉDITOS",
        "",
        "Trilha sonora:",
        "Todas as faixas do jogo foram retiradas do álbum Selected Ambient Works Volume II.",
        "#1 - Aphex Twin",
        "#5 - Aphex Twin",
        "#9 - Aphex Twin",
        "#19 - Aphex Twin",
        "",
        "Sprites:",
        "  - Fonte / autor",
        "",
        "Desenvolvimento:",
        "Este jogo foi desenvolvido por Andresa Dantas e João Victor Rocha.",
        "",
        "",
        "",  # espaço antes da logo
    ]

    # Renderiza textos normais
    superfices = []
    for linha in linhas:
        surf = fonte.render(linha, True, (230, 230, 230))
        superfices.append(surf)

    # Renderiza logo
    logo_surf = fonteLogo.render("Ecos", True, (218, 152, 85))

    # Efeito de scroll (tipo créditos de cinema)
    y = Y + 20
    velocidade_base = 40
    fim_scroll = False
    enter_liberado = False
    
    tempo_total = 0
    pausa_final = 2.5
    tempo_pausa = 0

    # Fade
    fade = pygame.Surface((X, Y))
    fade.fill((0, 0, 0))
    alpha = 255
    fade_in = True

    rodando = True
    while rodando:
        dt = clock.tick(FPS) / 1000
        tempo_total += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "sair"
                if event.key == pygame.K_RETURN and enter_liberado:
                    return "fase1"

        tela.fill((0, 0, 0))

        y_atual = y

        # Desenha textos
        for surf in superfices:
            rect = surf.get_rect(center=(X // 2, y_atual))
            tela.blit(surf, rect)
            y_atual += surf.get_height() + 12

        # Desenha logo no final
        logo_rect = logo_surf.get_rect(center=(X // 2, y_atual + 60))
        tela.blit(logo_surf, logo_rect)

        # Scroll
        if not fim_scroll:
            easing = 1 - math.cos(min(tempo_total / 6, 1) * math.pi / 2)
            y -= velocidade_base * easing * dt

            if logo_rect.top < Y // 2:
                fim_scroll = True

        else:
            tempo_pausa += dt
            if tempo_pausa >= pausa_final:
                enter_liberado = True

        # Aviso final
        if enter_liberado:
            aviso = fonte.render(
                "Pressione ENTER para jogar novamente",
                True,
                (180, 180, 180)
            )
            tela.blit(aviso, aviso.get_rect(center=(X // 2, Y - 80)))

        # Fade-in
        if fade_in:
            alpha -= 180 * dt
            if alpha <= 0:
                alpha = 0
                fade_in = False

        fade.set_alpha(int(alpha))
        tela.blit(fade, (0, 0))

        pygame.display.flip()
   
