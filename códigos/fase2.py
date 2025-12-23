import pygame
from config import X, Y, FPS
from personagens import Protagonista, Ceifador

def fase2(tela):
    clock = pygame.time.Clock()

   
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.load('assets/FUNDO_MUSICAL.mp3')
        pygame.mixer.music.play(-1)
    except:
        pass 

    
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

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "sair"

                if event.key == pygame.K_l and protagonista.rect.colliderect(area_livro):
                    mostrando_estante = not mostrando_estante

                elif event.key == pygame.K_l and protagonista.rect.colliderect(area_diario):
                    mostrando_diario_texto = True

                if event.key == pygame.K_RETURN and mostrando_diario_texto:
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

            if protagonista.rect.colliderect(area_livro):
                t = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(t, (protagonista.posi[0], protagonista.posi[1] - 20))

            if protagonista.rect.colliderect(area_diario):
                d = fonte.render("Investigar (L)", True, (255, 255, 0))
                tela.blit(d, (protagonista.posi[0], protagonista.posi[1] - 20))

        if mostrando_estante:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            tela.blit(
                imagem_estante,
                (X // 2 - imagem_estante.get_width() // 2,
                 Y // 2 - imagem_estante.get_height() // 2)
            )

        if mostrando_diario_texto:
            overlay = pygame.Surface((X, Y))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            tela.blit(overlay, (0, 0))

            tela.blit(fonte.render("Alguma coisa aqui...", True, (255, 255, 255)), (X//2 - 150, Y//2 - 80))
            tela.blit(fonte.render("Alguma coisa acolá.", True, (255, 255, 255)), (X//2 - 150, Y//2 - 40))
            tela.blit(fonte.render("Pressione ENTER.", True, (255, 255, 0)), (X//2 - 150, Y//2 + 20))

        pygame.display.update()
