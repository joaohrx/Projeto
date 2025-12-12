import pygame

# Colisão da fase 3
# x, y, largura, altura
colisoes = [
    pygame.Rect(0, 10, 1280, 300), # Borda superior
    pygame.Rect(1245, 215, 35, 515), # Borda direita
    pygame.Rect(0, 590, 1280, 315), # Borda inferior
    pygame.Rect(380, 310, 155, 40), # Estante
    pygame.Rect(0, 310, 125, 65), # Mesa superior esquerda
    pygame.Rect(900, 310, 255, 55), # Mesa superior direita
    pygame.Rect(185, 530, 145, 60), # Mesa inferior esquerda
    pygame.Rect(745, 530, 160, 60), # Mesa inferior direita
    pygame.Rect(0, 0, 0, 0), #
    pygame.Rect(0, 0, 0, 0), #
    pygame.Rect(0, 0, 0, 0), #
]