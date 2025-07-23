import pygame

from abc import ABC, abstractmethod
pygame.init()


#Tela
x = 1280
y = 720
tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('ECOS')


# Musica
pygame.mixer.music.load('FUNDO_MUSICAL.mp3')  
pygame.mixer.music.play(-1) 

# tela de start
def tela_inicial():
    imagem_inicial = pygame.image.load('imagem_inicial.png')  
    imagem_inicial = pygame.transform.scale(imagem_inicial, (x, y))
    esperando = True

    while esperando:
        tela.blit(imagem_inicial, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                esperando = False

class Personagem(ABC):
    def __init__(self, imagem_path, tamanho, posi, velocidade):
        self.imagem = pygame.image.load(imagem_path).convert_alpha() # definir imagem
        self.imagem = pygame.transform.scale(self.imagem, tamanho) # transformar imagem pra o tamanho certo
        self.posi = list(posi)
        self.velocidade = velocidade
        self.vivo = True

    @abstractmethod
    def atualizar(self):
        pass

    def desenhar(self, tela):
        if self.vivo:
            tela.blit(self.imagem, self.posi)
            
class Protagonista(Personagem):
    def __init__(self):
        super().__init__('Protagonista.png', (48, 48), (1050, 650), 0.5)

    def atualizar(self, teclas):
        if teclas[pygame.K_w]:
            self.posi[1] -= self.velocidade
        if teclas[pygame.K_s]:
            self.posi[1] += self.velocidade
        if teclas[pygame.K_a]:
            self.posi[0] -= self.velocidade
        if teclas[pygame.K_d]:
            self.posi[0] += self.velocidade
            
class Ceifador(Personagem): # monstro
    def __init__(self):
        super().__init__('monstro.png', (200, 200), (-200, 200), 0.7)
        
    def atualizar(self):
        self.posi [0] += self.velocidade
        


#Carregar plano de fundo
fundo = pygame.image.load('image.1.png').convert_alpha()
fundo = pygame.transform.scale(fundo, (x, y))

protagonista = Protagonista()
monstro = Ceifador()
monstros_mortos = 0
max_monstros = 3

protagonista_vivo = True

tela_inicial()

#inicializar
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.blit(fundo, (0, 0))


# desenhar o monstro e aplicar o limite de respawn
    if monstros_mortos < max_monstros and monstro.vivo:
        monstro.atualizar()
        monstro.desenhar(tela)
        
        if monstro.posi[0] > 1200:
            monstros_mortos += 1
            monstro.vivo = False  
    elif monstros_mortos < max_monstros:
         monstro = Ceifador()

    # atualizar e desenhar o protagonista
    teclas = pygame.key.get_pressed()
    protagonista.atualizar(teclas)
    protagonista.desenhar(tela)

    pygame.display.update()
    



