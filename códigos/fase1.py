import pygame
from config import X, Y, FPS
from personagens import Protagonista, teclas_normais


def fase1(tela):
    clock = pygame.time.Clock()

    pygame.mixer.music.load('assets/#1.mp3')
    pygame.mixer.music.play(-1, fade_ms=2000)
    

    fundo_jogo = pygame.image.load('assets/Mappa.png').convert()
    fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))

    largura = int(X * 0.9)
    altura = int(Y * 0.9)

    imagem_estante = pygame.image.load('assets/ESTANTEAA.png').convert_alpha()
    imagem_estante = escalar_sem_distorcer(imagem_estante, X * 0.95, Y * 0.95)

    imagem_estante3 = pygame.image.load('assets/ESTANTECC.png').convert_alpha()
    imagem_estante3 = escalar_sem_distorcer(imagem_estante3, X * 0.95, Y * 0.95)
    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 16)

    protagonista = Protagonista()

    # Áreas
    area_estante = pygame.Rect(302, 302, 90, 90)
    area_diario = pygame.Rect(1180, 440, 65, 65)
    area_livro1 = pygame.Rect(100, 400, 80, 120)
    area_livro2 = pygame.Rect(850, 550, 80, 80)
    area_estante_central = pygame.Rect(650, 330, 40, 40)
    area_estante3 = pygame.Rect(900, 310, 80, 80)
    area_livro3 = pygame.Rect(350, 500, 80, 80)

    # Estados
    mostrando_estante = False
    mostrando_estante3 = False
    mostrando_diario_texto = False
    mostrando_livro1 = False
    mostrando_livro2 = False
    mostrando_livro3 = False
    mostrando_aviso_estante_central = False  

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    if any([
                        mostrando_estante,
                        mostrando_estante3,
                        mostrando_diario_texto,
                        mostrando_livro1,
                        mostrando_livro2,
                        mostrando_livro3,
                        mostrando_aviso_estante_central
                    ]):
                        mostrando_estante = False
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
                    return "diario"

        tela.blit(fundo_jogo, (0, 0))

        if not any([
            mostrando_estante,
            mostrando_estante3,
            mostrando_diario_texto,
            mostrando_livro1,
            mostrando_livro2,
            mostrando_livro3,
            mostrando_aviso_estante_central
        ]):

            teclas = teclas_normais()
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

        elif mostrando_estante3:
            mostrar_imagem(tela, imagem_estante3)

        elif mostrando_aviso_estante_central:
            mostrar_texto(
                tela,
                fonte,
                ["Não é seguro ficar muito perto."]
            )

        elif mostrando_livro1:
            mostrar_texto(tela, fonte, [
                "Quando chegamos aqui, meu pai estava feliz pelo escape, e ao mesmo tempo, irritado",
                "Disse que mamãe foi irresponsável, que ela não deveria ter passado aquela carta",
                "e nem ajudado o Sr. ██████████ a falsificar aquele visto.",
                "Ele disse que tudo isso nos colocou em perigo, e melhor teria sido se só ele tivesse sofrido",
                "e não nós duas. Nunca vou esquecer a brutalidade da ███████ e dos homens invadindo nossa casa.",
                "Lembre das iniciais."
            ])

        elif mostrando_diario_texto:
            mostrar_texto(
                tela, fonte,
                [
                    "Bem vindos a ███████████████",
                    "É importante manter a biblioteca organizada",
                    "e os livros catalogados. De vez em quando um ou outro",
                    "livros ficam sem identificação.",
                    "A estante central está infestada de cupins.",
                    "Tenha um bom dia."
                ],
                rodape="Pressione ENTER"
            )

        elif mostrando_livro2:
            mostrar_texto(tela, fonte, [
                'Guerra e Paz – Liev Tolstói',
                'adouT csmEpo e mB eiPdodr - Marcel Proust',
                'daatirS - Hermann Hesse',
                'dreoncTi eâ ópcCr - Henry Miller',
                    ])

        elif mostrando_livro3:
            mostrar_texto(tela, fonte, [
            'Gttg Qgxêtotg - Liev Tolstói',
            'Vkzkx Vgt - J. M. Barrie',
            'U Vxuikyyu - Franz Kafka',
            
            ])

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
