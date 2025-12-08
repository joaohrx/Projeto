import pygame
from abc import ABC, abstractmethod
import colisao

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

        if not any(novo_rect.colliderect(c) for c in colisao.colisoes):
            self.posi = nova_posi
            self.rect.topleft = self.posi


class Protagonista(Personagem):
    def __init__(self, posi_inicial=(500, 300)):
        super().__init__('assets/Protagonista.png', (50, 50), posi_inicial, 0.5, 100)

    def atualizar(self, teclas):
        dx = dy = 0
        if teclas[pygame.K_w] or teclas[pygame.K_UP]: dy -= self.velocidade
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]: dy += self.velocidade
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]: dx -= self.velocidade
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]: dx += self.velocidade
        self.mover(dx, dy)

class Ceifador(Personagem):
    def __init__(self, dano = 10):
        self.dano = dano
        super().__init__('assets/monstro.png', (125, 125), (170, 335), 0.7, 40)

    def atualizar(self, teclas):
        self.mover(self.velocidade, 0)

class Lanterna:
    def __init__(self, energia = 100, usando = False, ultimo_uso = 0, tempo_recarga = 0, imagem = "assets/lanterna_spritesheet.png"):
        self.energia = energia
        self.usando = usando
        self.ultimo_uso = ultimo_uso
        self.tempo_recarga = tempo_recarga
        self.imagem = pygame.image.load(imagem).convert_alpha()

    def usar(self):
        if self.energia > 0:
            self.usando = True