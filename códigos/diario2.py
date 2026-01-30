import pygame
import random
from config import X, Y, FPS


def diario2(tela):
    clock = pygame.time.Clock()
    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 32)
    fonte_erro = pygame.font.Font("assets/DepartureMono-Regular.otf", 26)

    texto_digitado = ""
    codigo_correto = "ss"
    codigo_hugo = "hugo"

    mensagem_erro = ""
    tempo_erro = 0

    Hugo = pygame.image.load("assets/aihugo.jpg").convert()
    Hugo = pygame.transform.scale(Hugo, (X, Y))

    try:
        Hugo_som = pygame.mixer.Sound("assets/AIHUGO.mp3")
    except:
        Hugo_som = None

    # transicao
    em_transicao = False
    inicio_transicao = 0
    DURACAO_TRANSICAO = 9000  # 20 segundos em milimaxsegundos

    rodando = True

    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:

                if em_transicao:
                    continue

                if event.key == pygame.K_ESCAPE:
                    return "fase2"

                if event.key == pygame.K_RETURN:

                    # Easter egg
                    if texto_digitado.strip() == codigo_hugo:

                        if Hugo_som:
                            Hugo_som.play()

                        tela.blit(Hugo, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(1000)

                        return "fase2"

                    # Código correto
                    if texto_digitado.lower() == codigo_correto:
                        em_transicao = True
                        inicio_transicao = pygame.time.get_ticks()
                        continue

                    # Código errado
                    texto_digitado = ""
                    mensagem_erro = "..."
                    tempo_erro = pygame.time.get_ticks()

                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]

                else:
                    if event.unicode.isalnum():
                        texto_digitado += event.unicode

          # transicao
        if em_transicao:
            tempo_atual = pygame.time.get_ticks()
            tempo_passado = tempo_atual - inicio_transicao

            tela.fill((0, 0, 0))

            # efeito glitch
            for _ in range(30):
                x = random.randint(0, X)
                y = random.randint(0, Y)
                w = random.randint(20, 120)
                h = random.randint(5, 25)
                cor = random.choice([(255, 255, 255), (255, 0, 0)])
                pygame.draw.rect(tela, cor, (x, y, w, h))

            fonteglitch = pygame.font.Font("assets/Faith_Collapsing.ttf", 60) 
            texto = fonteglitch.render("Rocha pense em algo que combine com sua fase",True, (255, 0, 0))
            tela.blit(texto, texto.get_rect(center=(X // 2, Y // 2)))

            pygame.display.update()

            if tempo_passado >= DURACAO_TRANSICAO:
                return "fase3"

            continue


        tela.fill((0, 0, 0))

        t1 = fonte.render("...", True, (255, 255, 255))
        tela.blit(t1, (X // 2 - 150, Y // 2 - 60))

        t2 = fonte.render(texto_digitado, True, (255, 255, 0))
        tela.blit(t2, (X // 2 - 150, Y // 2 - 20))
        
        if mensagem_erro:
            if pygame.time.get_ticks() - tempo_erro < 2000:
                erro = fonte_erro.render(mensagem_erro, True, (200, 50, 50))
                tela.blit(erro, (X // 2 - 150, Y // 2 + 30))
            else:
                mensagem_erro = ""

        pygame.display.update()
