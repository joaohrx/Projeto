import pygame
from abc import ABC, abstractmethod
import colisao
import os
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
            
            if self.lanterna and self.lanterna.ligada and self.lanterna.energia > 0:
                lanterna_pos = (
                    self.posi[0] + 20 if self.direcao == "direita" else self.posi[0] - 10,
                    self.posi[1] + 15
                )  
                self.lanterna.desenhar(tela, lanterna_pos)

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
        
        self.lanterna = Lanterna(
        "assets/lanterna_spritesheet.png",
        frame_w=32,
        frame_h=32,
        frames=8
        )

    def carregar_animacao(self, pasta, quantidade):
      frames = []
      for i in range(1, quantidade + 1):
        caminho = os.path.join(pasta, f"{i}.png")
        img = pygame.image.load(caminho).convert_alpha()
        img = pygame.transform.scale(img, (50, 50))
        frames.append(img)
      return frames


    def atualizar(self, teclas, lanterna_ligada = False):
        dx = dy = 0
        movimento = False

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            dy -= self.velocidade

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            dy += self.velocidade

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            dx -= self.velocidade
            self.direcao = "esquerda"
            movimento = True

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            dx += self.velocidade
            self.direcao = "direita"
            movimento = True

        self.mover(dx, dy)

        if movimento:
            self.animar()
        else:
            self.frame_atual = 0
            self.imagem = self.animacoes[self.direcao][0]
            
        if self.lanterna.ligada and self.lanterna.energia > 0:
            self.lanterna.atualizar(lanterna_ligada)


class Lanterna:
    def __init__(self, caminho_spritesheet, frame_w, frame_h, frames):
        self.frames = []
        self.frame_atual = 0
        self.tempo_animacao = 0
        self.delay = 80

        self.energia = 100
        self.ligada = False

        sheet = pygame.image.load(caminho_spritesheet).convert_alpha()

        for i in range(frames):
            frame = sheet.subsurface(
                pygame.Rect(i * frame_w, 0, frame_w, frame_h)
            )
            frame = pygame.transform.scale(frame, (40, 40))
            self.frames.append(frame)

    def atualizar(self, ligada):
        agora = pygame.time.get_ticks()
        self.ligada = ligada

        if self.ligada and self.energia > 0:
            self.energia -= 0.2

            if agora - self.tempo_animacao > self.delay:
                self.tempo_animacao = agora
                self.frame_atual = (self.frame_atual + 1) % len(self.frames)

        else:
            self.frame_atual = 0

    def desenhar(self, tela, pos):
        if self.energia <= 0:
            return

        tela.blit(self.frames[self.frame_atual], pos)
        
