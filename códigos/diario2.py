import pygame
from config import X, Y, FPS

def diario2(tela):
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 32)

    texto_digitado = ""
    codigo_correto = "temquevercomoscarala2"
    codigo_hugo = "821715"

  
    Hugo = pygame.image.load("assets/aihugo.jpg").convert()
    Hugo = pygame.transform.scale(Hugo, (X, Y))

    
    try:
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
                    return "fase2"

                if event.key == pygame.K_RETURN:

                    #Caso o codigo seja o easter egg
                    if texto_digitado.strip() == codigo_hugo:

                        if Hugo_som:
                            Hugo_som.play()

                       
                        tela.blit(Hugo, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(1000)

                       
                        return "fase2"

                    #Caso o codigo esteja correto
                    if texto_digitado.lower() == codigo_correto:
                        return "fase3"

                    # Caso o codigo esteja errado
                    return "fase2"

                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]

                else:
                    texto_digitado += event.unicode

      
        tela.fill((0, 0, 0))

        t1 = fonte.render("...", True, (255, 255, 255))
        tela.blit(t1, (X//2 - 150, Y//2 - 60))

        t2 = fonte.render(texto_digitado, True, (255, 255, 0))
        tela.blit(t2, (X//2 - 150, Y//2 - 20))

        pygame.display.update()
