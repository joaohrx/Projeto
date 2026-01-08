import pygame
from config import X, Y, FPS

def diario(tela):
    clock = pygame.time.Clock()

    #Fonte
    fonte = pygame.font.Font("assets/DepartureMono-Regular.otf", 32)
    fonte_erro = pygame.font.Font("assets/DepartureMono-Regular.otf", 26)

    #Entrada
    texto_digitado = ""
    codigo_correto = "temquevercomoscarala"
    codigo_hugo = "821715"

    #erro
    mensagem_erro = ""
    tempo_erro = 0

    #Imagem
    Hugo = pygame.image.load("assets/aihugo.jpg").convert()
    Hugo = pygame.transform.scale(Hugo, (X, Y))

    Visao = pygame.image.load("assets/eye.png").convert()
    Visao = pygame.transform.scale(Visao, (X, Y))

    # Som
    Hugo_som = None
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        Hugo_som = pygame.mixer.Sound("assets/AIHUGO.mp3")
    except:
        Hugo_som = None

    rodando = True

    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "sair"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "fase1"

                if event.key == pygame.K_RETURN:

                    # Easter egg
                    if texto_digitado.strip() == codigo_hugo:
                        if Hugo_som:
                            Hugo_som.play()

                        tela.blit(Hugo, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        return "fase1"

                    # Código correto
                    if texto_digitado.lower().strip() == codigo_correto:
                        tela.blit(Visao, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(100)
                        return "fase2"

                    # Código errado
                    texto_digitado = ""
                    mensagem_erro = "Não foram esses..."
                    tempo_erro = pygame.time.get_ticks()

                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]

                else:
                    if event.unicode.isalnum():
                        texto_digitado += event.unicode

      
        tela.fill((0, 0, 0))

        #Texto fixo
        dica = fonte.render("....", True, (255, 255, 255))
        tela.blit(dica, (X // 2 - 150, Y // 2 - 60))

        #Texto digitado
        entrada = fonte.render(texto_digitado, True, (255, 255, 0))
        tela.blit(entrada, (X // 2 - 150, Y // 2 - 20))

        #Mensagem de erro 
        if mensagem_erro:
            if pygame.time.get_ticks() - tempo_erro < 2000:
                erro = fonte_erro.render(mensagem_erro, True, (200, 50, 50))
                tela.blit(erro, (X // 2 - 150, Y // 2 + 30))
            else:
                mensagem_erro = ""

        pygame.display.update()
