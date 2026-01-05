import pygame
from config import X, Y, FPS
from personagens import Protagonista, Ceifador


def fase2(tela):
    clock = pygame.time.Clock()

    pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
    pygame.mixer.music.play(-1)

    fundo_jogo = pygame.image.load('assets/Mappa.png').convert()
    fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))

    imagem_estante = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante = pygame.transform.scale(imagem_estante, (600, 400))

    imagem_estante_central = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante_central = pygame.transform.scale(imagem_estante_central, (600, 400))

    imagem_estante3 = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante3 = pygame.transform.scale(imagem_estante3, (600, 400))

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 16)

    protagonista = Protagonista()
    monstro = Ceifador()

    monstros_mortos = 0
    max_monstros = 3

    # Áreas
    area_estante= pygame.Rect(302, 302, 90, 90)
    area_diario = pygame.Rect(100, 400, 80, 120)
    area_livro1 = pygame.Rect(1180, 440, 65, 65)
    area_livro2 = pygame.Rect(850, 550, 80, 80)
    area_estante_central = pygame.Rect(650, 330, 40, 40)
    area_estante3 = pygame.Rect(900, 310, 80, 80)
    area_livro3 = pygame.Rect(350, 500, 80, 80)
    

    # Estados
    mostrando_estante = False
    mostrando_estante_central = False
    mostrando_estante3 = False
    mostrando_diario_texto = False
    mostrando_livro1 = False
    mostrando_livro2 = False
    mostrando_livro3 = False

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    if any([
                        mostrando_estante,
                        mostrando_estante_central,
                        mostrando_estante3,
                        mostrando_diario_texto,
                        mostrando_livro1,
                        mostrando_livro2,
                        mostrando_livro3
                    ]):
                        mostrando_estante = False
                        mostrando_estante_central = False
                        mostrando_estante3 = False
                        mostrando_diario_texto = False
                        mostrando_livro1 = False
                        mostrando_livro2 = False
                        mostrando_livro3 = False
                    else:
                        return "sair"

                elif event.key == pygame.K_l:
                    if protagonista.rect.colliderect(area_estante):
                        mostrando_estante = True
                    elif protagonista.rect.colliderect(area_estante_central):
                        mostrando_estante_central = True
                    elif protagonista.rect.colliderect(area_estante3):
                        mostrando_estante3 = True
                    elif protagonista.rect.colliderect(area_diario):
                        mostrando_diario_texto = True
                    elif protagonista.rect.colliderect(area_livro1):
                        mostrando_livro1 = True
                    elif protagonista.rect.colliderect(area_livro2):
                        mostrando_livro2 = True
                    elif protagonista.rect.colliderect(area_livro3):
                        mostrando_livro3 = True

                if event.key == pygame.K_RETURN and mostrando_diario_texto:
                    return "diario2"

        tela.blit(fundo_jogo, (0, 0))

        if not any([
            mostrando_estante,
            mostrando_estante_central,
            mostrando_estante3,
            mostrando_diario_texto,
            mostrando_livro1,
            mostrando_livro2,
            mostrando_livro3
        ]):

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

            for area in [
                area_estante, area_estante_central, area_estante3,
                area_diario, area_livro1, area_livro2, area_livro3
            ]:
                if protagonista.rect.colliderect(area):
                    t = fonte.render("Investigar (L)", True, (255, 255, 0))
                    tela.blit(t, (protagonista.posi[0], protagonista.posi[1] - 20))

        elif mostrando_estante:
            mostrar_imagem(tela, imagem_estante)

        elif mostrando_estante_central:
            mostrar_imagem(tela, imagem_estante_central)

        elif mostrando_estante3:
            mostrar_imagem(tela, imagem_estante3)

        elif mostrando_livro1:
            mostrar_texto(tela, fonte, [
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
            ])

        elif mostrando_diario_texto:
            mostrar_texto(tela,fonte,
                [
                    "24/06/08",
                    "Terceiro dia na cidade. Meu pai conseguiu um emprego de arquivista",
                    "aqui na biblioteca local, nada interessante.",
                    "Depois da escola eu venho para cá e decidi fazer leituras",
                    "aleatórias baseadas na ordem alfabética para passar o tempo",
                    "vou escrever alguns na proxíma página..",
                    "Espero me manter entretida até as férias",
                ],
                rodape="Pressione ENTER"
            )

        elif mostrando_livro2:
            mostrar_texto(tela,fonte,
                [
                    "02/07/08",
                ]
            )

        elif mostrando_livro3:
            mostrar_texto(tela,fonte,
                [
                    "06/07/08",
                ]
            )

        pygame.display.update()


def mostrar_imagem(tela, imagem):
    overlay = pygame.Surface((X, Y))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    tela.blit(
        imagem,
        (X // 2 - imagem.get_width() // 2,
         Y // 2 - imagem.get_height() // 2)
    )


def mostrar_texto(tela, fonte, linhas, rodape="Pressione ESC para fechar"):
    overlay = pygame.Surface((X, Y))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    y_inicial = Y // 2 - 120
    espacamento = 22

    for i, linha in enumerate(linhas):
        texto = fonte.render(linha, True, (255, 255, 255))
        rect = texto.get_rect(center=(X // 2, y_inicial + i * espacamento))
        tela.blit(texto, rect)

    rodape_txt = fonte.render(rodape, True, (255, 255, 0))
    tela.blit(
        rodape_txt,
        rodape_txt.get_rect(center=(X // 2, y_inicial + len(linhas) * espacamento + 30))
    )
