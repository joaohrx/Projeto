import pygame
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, imagem_path, tamanho, posi, velocidade):
        self.imagem = pygame.image.load(imagem_path).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, tamanho)
        self.posi = list(posi)
        self.velocidade = velocidade
        self.vivo = True

    @abstractmethod
    def atualizar(self): pass

    def desenhar(self, tela):
        if self.vivo:
            tela.blit(self.imagem, self.posi)

    def colisao(self):
        pass

class Protagonista(Personagem):
    def __init__(self):
        super().__init__('assets/Protagonista.png', (60, 60), (616, 336), 0.5)

    def atualizar(self, teclas):
        if teclas[pygame.K_w]: self.posi[1] -= self.velocidade
        if teclas[pygame.K_s]: self.posi[1] += self.velocidade
        if teclas[pygame.K_a]: self.posi[0] -= self.velocidade
        if teclas[pygame.K_d]: self.posi[0] += self.velocidade

class Ceifador(Personagem):
    def __init__(self):
        super().__init__('assets/monstro.png', (200, 200), (-200, 200), 0.7)

    def atualizar(self):
        self.posi[0] += self.velocidade