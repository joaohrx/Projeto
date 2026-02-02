import pygame
from config import *

def final(tela):
   clock = pygame.time.Clock() 
   
   pygame.mixer.music.load('assets/#19.mp3')
   pygame.mixer.music.play(-1)

   for event in pygame.event.get():
         if event.type == pygame.QUIT:
                return "sair"
         if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                    return "sair"

   
