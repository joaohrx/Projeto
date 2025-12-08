import pygame
from config import X, Y, CAPTION
from telas import tela_inicial
from fase1 import fase1
from fase2 import fase2
from fase3 import fase3
from diario import diario
from diario2 import diario2

pygame.init()

tela = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
pygame.display.set_caption(CAPTION)

tela_inicial(tela)

estado = "fase1"
rodando = True

while rodando:

    if estado == "fase1":
        estado = fase1(tela)

    elif estado == "diario":
        estado = diario(tela)
    
    elif estado == "fase3":
        estado = fase3(tela)
    
    elif estado == "fase2":
        estado = fase2(tela)
    
    elif estado =="diario2":
        estado =diario2(tela)
    
    elif estado == "fase3":
        estado = fase3(tela)

    elif estado == "sair":
        rodando = False

pygame.quit()
