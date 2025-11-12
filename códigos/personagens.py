import pygame
from abc import ABC, abstractmethod
from colisao import colisoes

class Personagem(ABC):
    def __init__(self, imagem_path, tamanho, posi, velocidade, vida):
        self.imagem = pygame.image.load(imagem_path).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, tamanho)
        self.posi = list(posi)
        self.velocidade = velocidade
        self.vivo = True
        self.rect = pygame.Rect(self.posi[0], self.posi[1], tamanho[0], tamanho[1])
        self.vida = vida

    @abstractmethod
    def atualizar(self, teclas):
        pass

    def desenhar(self, tela):
        if self.vivo:
            tela.blit(self.imagem, self.posi)

    def mover(self, dx, dy):
        nova_posi = [self.posi[0] + dx, self.posi[1] + dy]
        novo_rect = pygame.Rect(nova_posi[0], nova_posi[1], self.rect.width, self.rect.height)

        if not any(novo_rect.colliderect(c) for c in colisoes):
            self.posi = nova_posi
            self.rect.topleft = self.posi


class Protagonista(Personagem):
    def __init__(self):
        super().__init__('assets/Protagonista.png', (50, 50), (500, 300), 0.5, 100)

    def atualizar(self, teclas):
        dx = dy = 0
        if teclas[pygame.K_w]: dy -= self.velocidade
        if teclas[pygame.K_s]: dy += self.velocidade
        if teclas[pygame.K_a]: dx -= self.velocidade
        if teclas[pygame.K_d]: dx += self.velocidade
        self.mover(dx, dy)

class Ceifador(Personagem):
    def __init__(self):
        super().__init__('assets/monstro.png', (200, 200), (-300, 300), 0.7, 40)

    def atualizar(self, teclas):
        self.mover(self.velocidade, 0)

class Lanterna():
    pass