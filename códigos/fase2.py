import pygame
from config import X, Y, FPS
from personagens import Protagonista


def fase2(tela):
    clock = pygame.time.Clock()

    pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
    pygame.mixer.music.play(-1)

    fundo_jogo = pygame.image.load('assets/Mappa.png').convert()
    fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))
    
    som_alucinacao = pygame.mixer.Sound("assets/alucinacao.wav")
    som_alucinacao.set_volume(0.6)

    imagem_estante = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante = pygame.transform.scale(imagem_estante, (600, 400))

    imagem_estante_central = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante_central = pygame.transform.scale(imagem_estante_central, (600, 400))

    imagem_estante3 = pygame.image.load('assets/MODRFT1.png').convert_alpha()
    imagem_estante3 = pygame.transform.scale(imagem_estante3, (600, 400))

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 16)

    protagonista = Protagonista()

    # Áreas
    area_estante = pygame.Rect(302, 302, 90, 90)
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

    #alucinado
    alucinou_livro2 = False
    alucinou_livro3 = False

    em_alucinacao = False
    inicio_alucinacao = 0
    DURACAO_ALUCINACAO = 900

    TEXTO_INTRUSIVO = ""
   
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
                        agora = pygame.time.get_ticks()

                        #alucinado
                        if mostrando_livro2 and not alucinou_livro2:
                            em_alucinacao = True
                            inicio_alucinacao = agora
                            TEXTO_INTRUSIVO = "WIR WISSEN, WO IHR SEID. ES GIBT KEIN VERSTECK", "ES IST NUR EINE FRAGE DER ZEIT."
                            som_alucinacao.play()
                            alucinou_livro2 = True

                        elif mostrando_livro3 and not alucinou_livro3:
                            em_alucinacao = True
                            inicio_alucinacao = agora
                            TEXTO_INTRUSIVO = "Deutschland wird gereinigt.", "EIN VOLK, EIN REICH, EIN FÜHRER."
                            som_alucinacao.play()
                            alucinou_livro3 = True

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

        tela.fill((0, 0, 0))
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
            t = fonte.render("Pressione ESC para fechar", True, (255, 255, 0))
            tela.blit(t, (500, 690))

        elif mostrando_estante_central:
            mostrar_imagem(tela, imagem_estante_central)
            t = fonte.render("Pressione ESC para fechar", True, (255, 255, 0))
            tela.blit(t, (500, 690))

        elif mostrando_estante3:
            mostrar_imagem(tela, imagem_estante3)
            t = fonte.render("Pressione ESC para fechar", True, (255, 255, 0))
            tela.blit(t, (500, 690))

        elif mostrando_livro1:
            mostrar_texto(tela, fonte, [
                "24/07/08",
                "as coiSas pioraram",
                "estou passando mais tEmpo do que é necessário na escola",
                "me envolvI em projetos e pesquisas chatas",
                "não quero voltar pra caSa.",
                "ainda venho pra cá porque, por algum motivo",
                "que não sei explicar, percebi que",
                "ele fica mais calmo aqui do que em casa."
            ])

        elif mostrando_diario_texto:
            mostrar_texto(
                tela, fonte,
                [
                    "08/08/08",
                    "Isso não é ele. Isso não é você."
                ],
                rodape="Pressione ENTER"
            )

        elif mostrando_livro2:
            mostrar_texto(tela, fonte, [
                "30/07/08",
                "toda noite é a mesma coisa",
                "suspeito que mamãe esteja tOmando remédios para dormir,",
                "também suspeito que ela não sabe dIsso.. ",
                "as brigas ficaram mais pesadas, ele joga",
                "coisas pela casa e fala que deveriamos ser gratas",
                "por esse emprego, e que ele se mata de trabalhar",
                "por nós. ele não percebe? não percebe que por algum moTivo,",
                "por mais que ele trabalhe dia e noite, a gente não tem recebido",
                "nada.. Mamãe acha que ele está traindo ela, por isso as brigas",
                "não sei bem o que pensar, nunca vi nenhuma mulher entrar",
                "no tempo que passO aqui.."
            ])

        elif mostrando_livro3:
            mostrar_texto(tela, fonte, [
                "06/08/08",
                "mamãe foi embora.",
                "ela não deixou cartaS nem me acordou para ir com ela.",
                "nos primeiros dias eu pensei que ela podia ter saido",
                "esfriar a cabeça, mas ela não vOltou..",
                "quase não vejo meu pai, na verdade eu evito ele propositalmente",
                "dentro de Casa, quando ele saí eu espero um tempo e venho para cá",
                "sei que ele almoça aqui, e cOmo eu disse",
                "fica totalmente diferente, mais calmo e controlado,",
                "ainda com os olhos meio vazios, mas nada compaRado",
                "com aquilo que moRa comigo. Queria que mamãe voltasse logO",
                "sei que ela me ama, deve estar preparando algum lugar",
                "para a gente ficar."
            ])

        #alucinado
        if em_alucinacao:
            agora = pygame.time.get_ticks()
            if agora - inicio_alucinacao < DURACAO_ALUCINACAO:
                efeito_alucinacao(tela, fonte, TEXTO_INTRUSIVO)
            else:
                em_alucinacao = False

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


#alucinado
def efeito_alucinacao(tela, fonte, texto_intrusivo):
    offset_x = pygame.time.get_ticks() % 6 - 3
    offset_y = pygame.time.get_ticks() % 6 - 3

    copia = tela.copy()
    tela.blit(copia, (offset_x, offset_y))

    overlay = pygame.Surface((X, Y), pygame.SRCALPHA)
    overlay.fill((120, 0, 0, 80))
    tela.blit(overlay, (0, 0))

    texto = fonte.render(texto_intrusivo, True, (255, 255, 255))
    rect = texto.get_rect(center=(X // 2, Y // 2))
    tela.blit(texto, rect)

