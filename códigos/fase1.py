import pygame
from config import X, Y, FPS
from personagens import Protagonista, Ceifador
from colisao import colisoes


def fase1(tela):
    clock = pygame.time.Clock()

    pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
    pygame.mixer.music.play(-1)

    fundo_jogo = pygame.image.load('assets/Mappa.png').convert()
    fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))

    imagem_estante = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante = pygame.transform.scale(imagem_estante, (600, 400))

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 16)

    protagonista = Protagonista()
    monstro = Ceifador()
    monstros_mortos = 0
    max_monstros = 3

    area_livro = pygame.Rect(302, 302, 90, 90)
    area_diario = pygame.Rect(1180, 440, 65, 65)

    mostrando_estante = False
    mostrando_diario_texto = False

    rodando = True

    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "sair"

                # Interação com a estante
                if (
                    event.key == pygame.K_l
                    and protagonista.rect.colliderect(area_livro)
                    and not mostrando_diario_texto
                ):
                    mostrando_estante = not mostrando_estante

                # Interação com o diário
                elif (
                    event.key == pygame.K_l
                    and protagonista.rect.colliderect(area_diario)
                    and not mostrando_estante
                    and not mostrando_diario_texto
                ):
                    mostrando_diario_texto = True

                # Saída do diário
                if event.key == pygame.K_RETURN and mostrando_diario_texto:
                    return "diario"

        tela.blit(fundo_jogo, (0, 0))

        # ================= JOGO NORMAL =================
        if not mostrando_estante and not mostrando_diario_texto:

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

            # Texto estante
            if protagonista.rect.colliderect(area_livro):
                t = fonte.render("Investigar (L)", True, (255, 255, 0))
                rect = t.get_rect(center=(protagonista.posi[0], protagonista.posi[1] - 20))
                tela.blit(t, rect)

            # Texto diário
            if protagonista.rect.colliderect(area_diario):
                d = fonte.render("Investigar (L)", True, (255, 255, 0))
                rect = d.get_rect(center=(protagonista.posi[0], protagonista.posi[1] - 20))
                tela.blit(d, rect)

        # ================= ESTANTE =================
        elif mostrando_estante:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            x_img = X // 2 - imagem_estante.get_width() // 2
            y_img = Y // 2 - imagem_estante.get_height() // 2
            tela.blit(imagem_estante, (x_img, y_img))

        # ================= DIÁRIO =================
        elif mostrando_diario_texto:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            linhas = [
                "24/06/08"
                "Terceiro dia na cidade. Meu pai conseguiu um emprego de arquivista",
                "aqui na biblioteca local, nada interessante.",
                "Depois da escola eu venho para cá e decidi fazer leituras",
                "aleatórias baseadas na ordem alfabética para passar o tempo",
                "vou escrever alguns exemplos depois..",
                "Espero me manter entretida até as férias",
            ]

            y_inicial = Y // 2 - 100
            espacamento = 22

            for i, linha in enumerate(linhas):
                texto = fonte.render(linha, True, (255, 255, 255))
                rect = texto.get_rect(center=(X // 2, y_inicial + i * espacamento))
                tela.blit(texto, rect)

            texto_enter = fonte.render("Pressione ENTER", True, (255, 255, 0))
            rect_enter = texto_enter.get_rect(
                center=(X // 2, y_inicial + len(linhas) * espacamento + 30)
            )
            tela.blit(texto_enter, rect_enter)

        pygame.display.update()
