import pygame
from config import X, Y, FPS
from personagens import Protagonista, Ceifador

def fase2(tela):
    clock = pygame.time.Clock()

    pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
    pygame.mixer.music.play(-1)

    fundo_jogo = pygame.image.load('assets/Mappa.png').convert()
    fundo_jogo = pygame.transform.scale(fundo_jogo, (X, Y))

    imagem_estante = pygame.image.load('assets/estante01.png').convert_alpha()
    imagem_estante = pygame.transform.scale(imagem_estante, (600, 400))

    fonte = pygame.font.Font(None, 22)

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

                #Interação com a estante
                if event.key == pygame.K_l and protagonista.rect.colliderect(area_livro):
                    mostrando_estante = not mostrando_estante

                #interação com o diario
                elif event.key == pygame.K_l and protagonista.rect.colliderect(area_diario):
                    mostrando_diario_texto = True

                if event.key == pygame.K_RETURN:
                    if mostrando_diario_texto:
                        return "diario2"

        tela.blit(fundo_jogo, (0, 0))

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

            #Texto estante
            if protagonista.rect.colliderect(area_livro):
                t = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(t, (protagonista.posi[0], protagonista.posi[1] - 20))

            #Texto diario
            if protagonista.rect.colliderect(area_diario):
                d = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(d, (protagonista.posi[0], protagonista.posi[1] - 20))

        if mostrando_estante:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            x_img = X // 2 - imagem_estante.get_width() // 2
            y_img = Y // 2 - imagem_estante.get_height() // 2
            tela.blit(imagem_estante, (x_img, y_img))


        if mostrando_diario_texto:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            texto1 = fonte.render("Alguma couisa aqui...", True, (255, 255, 255))
            texto2 = fonte.render("Alguma couisa acola.", True, (255, 255, 255))
            texto3 = fonte.render("Pressione enter.", True, (255, 255, 0))

            tela.blit(texto1, (X//2 - 150, Y//2 - 80))
            tela.blit(texto2, (X//2 - 150, Y//2 - 40))
            tela.blit(texto3, (X//2 - 150, Y//2 + 20))

        pygame.display.update()
