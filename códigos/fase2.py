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

    imagem_estante = pygame.image.load('assets/AA2.png').convert_alpha()
    imagem_estante = escalar_sem_distorcer(imagem_estante, X * 0.95, Y * 0.95)

    imagem_estante3 = pygame.image.load('assets/ESTANTECC.png').convert_alpha()
    imagem_estante = escalar_sem_distorcer(imagem_estante, X * 0.95, Y * 0.95)

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
    mostrando_aviso_estante_central = False 
   

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
                        mostrando_livro3,
                        mostrando_aviso_estante_central
                    ]):
                        agora = pygame.time.get_ticks()

                        #alucinado
                        if mostrando_livro2 and not alucinou_livro2:
                            em_alucinacao = True
                            inicio_alucinacao = agora
                            TEXTO_INTRUSIVO = "14/7."
                            som_alucinacao.play()
                            alucinou_livro2 = True

                        elif mostrando_livro3 and not alucinou_livro3:
                            em_alucinacao = True
                            inicio_alucinacao = agora
                            TEXTO_INTRUSIVO = "EIN VOLK, EIN REICH, EIN FÜHRER."
                            som_alucinacao.play()
                            alucinou_livro3 = True

                        mostrando_estante = False
                        mostrando_estante_central = False
                        mostrando_estante3 = False
                        mostrando_diario_texto = False
                        mostrando_livro1 = False
                        mostrando_livro2 = False
                        mostrando_livro3 = False
                        mostrando_aviso_estante_central = False
                    else:
                        return "sair"

                elif event.key == pygame.K_l:
                    if protagonista.rect.colliderect(area_estante):
                        mostrando_estante = True
                    elif protagonista.rect.colliderect(area_estante_central):
                        mostrando_aviso_estante_central = True
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
            mostrando_livro3,
            mostrando_aviso_estante_central
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

        elif mostrando_aviso_estante_central:
            mostrar_texto(
                tela,
                fonte,
                ["Não é seguro ficar muito perto."]
            )
        elif mostrando_estante3:
            mostrar_imagem(tela, imagem_estante3)
            t = fonte.render("Pressione ESC para fechar", True, (255, 255, 0))
            tela.blit(t, (500, 690))

        elif mostrando_livro1:
            mostrar_texto(tela, fonte, [
            "A casa encolheu. Somos seis aqui e ficou",
            "cheio demais, alguem precisa ir embora.",
            "Aprendemos a medir o dia pelos passos do lado de fora,",
            "não pelo relógio. Comemos devagar para não fazer barulho.",
            "Até em nossos pensamentos precisamos agir devagar para não chamar atenção.",
            "Às vezes esqueço como era andar sem ter que pedir permissão ao chão.",
            "Não estamos escondidos dos guardas. Estamos escondidos de algo maior.",
            "Eles dizem que querem unificar ou algo assim, mas não entendo o que realmente querem dizer",
            "com isso."
            ])

        elif mostrando_diario_texto:
            mostrar_texto(
                tela, fonte,
                [
                    "Sombras sussurram."
                ],
                rodape="Pressione ENTER"
            )

        elif mostrando_livro2:
            mostrar_texto(tela, fonte, [
                "Eu já tinha idade suficiente para andar sozinho pelo bairro onde vivíamos quando eles",
                "chegaram em Budapeste. Minha mãe me disse que nós seríamos **********.",
                "Eu não tinha certeza sobre o que aquilo queria dizer, apenas sabia que estávamos partindo. ",
                "Parecia uma aventura, mas minha mãe disse que era sério.",
                "Fomos parte de um grupo de ******* que eles estavam trocando por caminhões.",
                "Partimos em trens. À noite, dormíamos do lado de fora, em barracas.",
                "Lá era lamacento e meus sapatos ficaram em frangalhos.",
                "Aquilo me impedia de correr, a única diversão que tínhamos.",
            ])

        elif mostrando_livro3:
            mostrar_texto(tela, fonte, [
                'Alguns meses após eu chegar em *********, acho que quase todo mundo ficou doente.',
                'Minha mãe havia tido malária, mas nunca teve tifo. Eu acabei contraíndo tifo, ',
                'e não lembro muito bem o que aconteceu naquele período, só sei que minha mãe me vestia toda manhã,',
                'e me arrastava para o trabalho, pois assim eu não corria o risco de apanhar ou de ser levada. ',
                'Então, minha mãe me arrastava de um lado para o outro, mas era óbvio que eu não estava bem.',
                'Uma vez, houve uma seleção para as ******* ** *** e nós estávamos em pé, do lado de fora, quando um guarda das [] mandou que eu fosse para um lado',
                'e que minha mãe fosse para outro porque eu parecia estar muito doente e era claro que ',
                'eu estava apenas desperdiçando a comida, a dieta de duzentas calorias que recebíamos por dia.' ,
                'Então, minha mãe implorou a ele dizendo que eu era filha dela e pediu para ir junto comigo: ela não pode vir comigo?,',
                'eu não posso ir junto com ela?, e ele disse que não, até que enfim falou: se você está tão preocupada com sua filha, vá com ela',
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

def escalar_sem_distorcer(imagem, largura_max, altura_max):
    largura_original, altura_original = imagem.get_size()
    proporcao = min(
        largura_max / largura_original,
        altura_max / altura_original
    )

    nova_largura = int(largura_original * proporcao)
    nova_altura = int(altura_original * proporcao)

    return pygame.transform.scale(imagem, (nova_largura, nova_altura))
    
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

