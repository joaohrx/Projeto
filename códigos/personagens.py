import pygame
from abc import ABC, abstractmethod
import colisao
import os

def teclas_normais():
    teclas_cru = pygame.key.get_pressed()
    return {
        "cima": teclas_cru[pygame.K_UP],
        "baixo": teclas_cru[pygame.K_DOWN],
        "esq": teclas_cru[pygame.K_LEFT],
        "dir": teclas_cru[pygame.K_RIGHT],
        "w": teclas_cru[pygame.K_w],
        "s": teclas_cru[pygame.K_s],
        "a": teclas_cru[pygame.K_a],
        "d": teclas_cru[pygame.K_d],
    }

class Personagem(ABC):
    def __init__(self, imagem_path, tamanho, posi, velocidade, vida):
        self.posi = list(posi)
        self.velocidade = velocidade
        self.vivo = True
        self.vida = vida

        self.rect = pygame.Rect(posi[0], posi[1], tamanho[0], tamanho[1])

        #animaçao
        self.animacoes = {}
        self.direcao = "direita"
        self.frame_atual = 0
        self.tempo_animacao = 0
        self.delay_animacao = 100  # ms

        #imagempadrão
        if imagem_path:
            self.imagem = pygame.image.load(imagem_path).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, tamanho)
        else:
            self.imagem = None

    @abstractmethod
    def atualizar(self, teclas):
        pass

    def desenhar(self, tela):
        if self.vivo and self.imagem:
            tela.blit(self.imagem, self.posi)

    def mover(self, dx, dy):
        nova_posi = [self.posi[0] + dx, self.posi[1] + dy]
        novo_rect = pygame.Rect(
            nova_posi[0], nova_posi[1],
            self.rect.width, self.rect.height
        )

        if not any(novo_rect.colliderect(c) for c in colisao.colisoes):
            self.posi = nova_posi
            self.rect.topleft = self.posi

    def animar(self):
        agora = pygame.time.get_ticks()

        if agora - self.tempo_animacao > self.delay_animacao:
            self.tempo_animacao = agora
            self.frame_atual += 1

            if self.frame_atual >= len(self.animacoes[self.direcao]):
                self.frame_atual = 0

            self.imagem = self.animacoes[self.direcao][self.frame_atual]

class Protagonista(Personagem):
    def __init__(self, posi_inicial=(500, 300)):
        super().__init__(
            None,
            (50, 50),
            posi_inicial,
            0.5,
            100
        )

        self.animacoes["direita"] = self.carregar_animacao(
            "assets/protagonista/direita", 6
        )
        self.animacoes["esquerda"] = self.carregar_animacao(
            "assets/protagonista/esquerda", 6
        )

        self.imagem = self.animacoes["direita"][0]
        
    def carregar_animacao(self, pasta, quantidade):
      frames = []
      for i in range(1, quantidade + 1):
        caminho = os.path.join(pasta, f"{i}.png")
        img = pygame.image.load(caminho).convert_alpha()
        img = pygame.transform.scale(img, (50, 50))
        frames.append(img)
      return frames


    def atualizar(self, teclas):
        dx = dy = 0
        movimento = False

        if teclas["w"] or teclas["cima"]:
            dy -= self.velocidade

        if teclas["s"] or teclas["baixo"]:
            dy += self.velocidade

        if teclas["a"] or teclas["esq"]:
            dx -= self.velocidade
            self.direcao = "esquerda"
            movimento = True

        if teclas["d"] or teclas["dir"]:
            dx += self.velocidade
            self.direcao = "direita"
            movimento = True

        self.mover(dx, dy)

        if movimento:
            self.animar()
        else:
            self.frame_atual = 0
            self.imagem = self.animacoes[self.direcao][0]
            
        
