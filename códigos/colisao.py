import pygame

# x, y, largura, altura
colisoes = [
    pygame.Rect(0, 10, 1280, 205), # Borda superior
    pygame.Rect(0, 215, 70, 515), # Borda esquerda
    pygame.Rect(70, 700, 1230, 100), # Borda inferior
    pygame.Rect(1245, 215, 35, 515), # Borda direita
    pygame.Rect(600, 215, 110, 150), # Estante central
    pygame.Rect(150, 215, 310, 150), # Estante esquerda
    pygame.Rect(850, 215, 310, 150), # Estante direita
    pygame.Rect(460, 330, 35, 35), # Livro avulso esquerdo
    pygame.Rect(815, 330, 35, 35), # Livro avulso direito
    pygame.Rect(345, 460, 170, 105), # Mesa centro-esquerda
    pygame.Rect(340, 570, 15, 15), # Pé esquerdo da mesa centro-esq
    pygame.Rect(505, 570, 15, 15), # Pé direito da mesa centro-esq
    pygame.Rect(795, 460, 170, 105), # Mesa centro-direita
    pygame.Rect(790, 570, 15, 15), # Pé esquerdo da mesa centro-dir
    pygame.Rect(955, 570, 15, 15), # Pé direito da mesa centro-dir
    pygame.Rect(70, 215, 80, 430), # Mesa da borda esquerda
    pygame.Rect(150, 365, 55, 60), # Papeis borda esquerda
    pygame.Rect(1180, 440, 65, 210), # Mesa da borda direita
    pygame.Rect(545, 660, 35, 35), # Papel avulso inferior
]