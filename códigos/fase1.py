import pygame
from config import X, Y, FPS
from personagens import Protagonista, Ceifador


def fase1(tela):
    clock = pygame.time.Clock()

    # Música de fundo
    pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
    pygame.mixer.music.play(-1)

    # Fundo
    fundo_jogo = pygame.image.load('assets/Mappa.png').convert()
    fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))

    # Imagem da estante
    imagem_estante = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante = pygame.transform.scale(imagem_estante, (600, 400))

    
    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 16)

    
    protagonista = Protagonista()
    monstro = Ceifador()

    monstros_mortos = 0
    max_monstros = 3

    #Areas de interação
    area_livro = pygame.Rect(302, 302, 90, 90)
    area_diario = pygame.Rect(1180, 440, 65, 65)
    area_livro1 = pygame.Rect(100, 400, 80, 120)

    #Estados de tela
    mostrando_estante = False
    mostrando_diario_texto = False
    mostrando_livro1 = False

    while True:
        clock.tick(FPS)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    if mostrando_estante or mostrando_diario_texto or mostrando_livro1:
                        mostrando_estante = False
                        mostrando_diario_texto = False
                        mostrando_livro1 = False
                    else:
                        return "sair"

                #Estante
                if (
                    event.key == pygame.K_l
                    and protagonista.rect.colliderect(area_livro)
                    and not mostrando_diario_texto
                    and not mostrando_livro1
                ):
                    mostrando_estante = not mostrando_estante

                #Diario
                elif (
                    event.key == pygame.K_l
                    and protagonista.rect.colliderect(area_diario)
                    and not mostrando_estante
                    and not mostrando_livro1
                ):
                    mostrando_diario_texto = True

                #Livro 1 (texto)
                elif (
                    event.key == pygame.K_l
                    and protagonista.rect.colliderect(area_livro1)
                    and not mostrando_estante
                    and not mostrando_diario_texto
                ):
                    mostrando_livro1 = True

                #Entrar no diário (tela separada)
                if event.key == pygame.K_RETURN and mostrando_diario_texto:
                    return "diario"

        
        tela.blit(fundo_jogo, (0, 0))

       
        if not mostrando_estante and not mostrando_diario_texto and not mostrando_livro1:

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

            #Areas de interação
            if protagonista.rect.colliderect(area_livro):
                t = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(t, (protagonista.posi[0], protagonista.posi[1] - 20))

            if protagonista.rect.colliderect(area_diario):
                d = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(d, (protagonista.posi[0], protagonista.posi[1] - 20))

            if protagonista.rect.colliderect(area_livro1):
                i = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(i, (protagonista.posi[0], protagonista.posi[1] - 20))

        
        elif mostrando_estante:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            tela.blit(
                imagem_estante,
                (X // 2 - imagem_estante.get_width() // 2,
                 Y // 2 - imagem_estante.get_height() // 2)
            )

        # Livro1 Texto
        elif mostrando_livro1:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            linhas_livro1 = [
                "28/06/08",
                "Ok, retiro o que eu disse sobre não ter nada de interessante.",
                "As pessoas são bem receptivas e eu já tenho até alguns amigos",
                "Eles fizeram uma careta estranha quando eu contei sobre o emprego do meu pai",
                "e não quiseram vir comigo pra cá depois da aula..",
                "As vezes eles só não gostam de ler né?",
                "Ser arquivista não é o emprego mais empolgante do mundo.",
                "Pai chegou estressado hoje, não sei porque,",
                "o movimento foi fraco e ele tá ganhando bem",
                "mãe me pediu para subir mais cedo pro quarto,",
                "estou escrevendo isso para passar o tempo.",
            ]

            y_inicial = Y // 2 - 120
            espacamento = 22

            for i, linha in enumerate(linhas_livro1):
                texto = fonte.render(linha, True, (255, 255, 255))
                rect = texto.get_rect(center=(X // 2, y_inicial + i * espacamento))
                tela.blit(texto, rect)

            fechar = fonte.render("Pressione ESC para fechar", True, (255, 255, 0))
            tela.blit(
                fechar,
                fechar.get_rect(center=(X // 2, y_inicial + len(linhas_livro1) * espacamento + 30))
            )

        # Diario Texto
        elif mostrando_diario_texto:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            linhas = [
                "24/06/08",
                "Terceiro dia na cidade. Meu pai conseguiu um emprego de arquivista",
                "aqui na biblioteca local, nada interessante.",
                "Depois da escola eu venho para cá e decidi fazer leituras",
                "aleatórias baseadas na ordem alfabética para passar o tempo",
                "vou escrever alguns na proxíma página..",
                "Espero me manter entretida até as férias",
            ]

            y_inicial = Y // 2 - 120
            espacamento = 22

            for i, linha in enumerate(linhas):
                texto = fonte.render(linha, True, (255, 255, 255))
                rect = texto.get_rect(center=(X // 2, y_inicial + i * espacamento))
                tela.blit(texto, rect)

            enter = fonte.render("Pressione ENTER", True, (255, 255, 0))
            tela.blit(
                enter,
                enter.get_rect(center=(X // 2, y_inicial + len(linhas) * espacamento + 30))
            )

        pygame.display.update()
