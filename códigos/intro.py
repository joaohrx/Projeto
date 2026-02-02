import pygame
from config import X, Y, FPS


def intro(tela):
    clock = pygame.time.Clock()

    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 16)

    pygame.mixer.music.load("assets/#1.mp3")
    pygame.mixer.music.play(-1)

    linhas = [
        "Meu pai foi um advogado ilustre. Defendia desde industrialistas a figurões da política, se sentava no escritório com eles,",
        "",
        "ria com eles, discutia com eles. Mas era █████. Um bom █████, diziam. Nenhum levantou um dedo para se opor a perseguição.",
        "",
        "Minha mãe era uma socialite de Berlim. Alemã, foi ostracizada desde o 30 de Janeiro por se relacionar com um █████.",
        "",
        "Mesmo depois do afundar na treva, vivemos na medida do possível, até que chegou o Mandato de ██████████.",
        "",
        "Foi dela a ideia de fugir e se esconder na casa remota do Arquivista. Um velho amigo. Estou seguro? Estamos seguros?"
    ]

    linha_atual = 0
    tempo_ultima_linha = pygame.time.get_ticks()
    INTERVALO = 2000  # ms
    INTERVALO_ENTER = 1800
    enter_liberado = False

    rodando = True
    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(1500)
                return "sair"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and enter_liberado:
                    pygame.mixer.music.fadeout(2000)
                    return "fase1"
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "sair"

        agora = pygame.time.get_ticks()
        if agora - tempo_ultima_linha > INTERVALO and linha_atual < len(linhas):
            linha_atual += 1
            tempo_ultima_linha = agora
            
        if linha_atual == len(linhas) and agora - tempo_ultima_linha > INTERVALO_ENTER:
            enter_liberado = True

        tela.fill((0, 0, 0))

        y_base = Y // 2 - 120
        for i in range(linha_atual):
            texto = fonte.render(linhas[i], True, (255, 255, 255))
            rect = texto.get_rect(center=(X // 2, y_base + i * 30))
            tela.blit(texto, rect)

        if enter_liberado:
            aviso = fonte.render("Pressione ENTER", True, (180, 180, 180))
            tela.blit(aviso, aviso.get_rect(center=(X // 2, Y - 80)))

        pygame.display.update()
