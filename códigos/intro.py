import pygame
from config import X, Y, FPS


def intro(tela):
    clock = pygame.time.Clock()

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 18)

    pygame.mixer.music.load("assets/#1.mp3")
    pygame.mixer.music.play(-1)

    linhas = [
        "calcinha preta.",
        "",
        "cavalo de pau.",
        "",
        "limão com mel.",
        "",
        "mastruz com leite.",
        "desejo de menina."
    ]

    linha_atual = 0
    tempo_ultima_linha = pygame.time.get_ticks()
    INTERVALO = 1700  # ms

    rodando = True
    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(1500)
                return "sair"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(2000)
                    return "fase1"

        agora = pygame.time.get_ticks()
        if agora - tempo_ultima_linha > INTERVALO and linha_atual < len(linhas):
            linha_atual += 1
            tempo_ultima_linha = agora

        tela.fill((0, 0, 0))

        y_base = Y // 2 - 120
        for i in range(linha_atual):
            texto = fonte.render(linhas[i], True, (255, 255, 255))
            rect = texto.get_rect(center=(X // 2, y_base + i * 30))
            tela.blit(texto, rect)

        if linha_atual == len(linhas):
            aviso = fonte.render("Pressione ENTER", True, (180, 180, 180))
            tela.blit(aviso, aviso.get_rect(center=(X // 2, Y - 80)))

        pygame.display.update()
