
#EP - Design de Software
#Dupla: Breno Alencar, Gabriel Araújo e Nívea Abreu
#Data:11/11/2020

#JOGO

#Inicialização

#Importando bibliotecas
import pygame
import random

#Iniciando Pygame
pygame.init()

#Definido janela
winWidth=1070
winHeight=600
win = pygame.display.set_mode((winWidth,winHeight))

#Nome do jogo
pygame.display.set_caption("Goblin Invasion")

#Sprites do personagem principal
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bgs = [pygame.image.load('frame-001.gif'), pygame.image.load('frame-002.gif'), pygame.image.load('frame-003.gif'), pygame.image.load('frame-004.gif'), pygame.image.load('frame-005.gif'), pygame.image.load('frame-006.gif'), pygame.image.load('frame-007.gif'), pygame.image.load('frame-008.gif'), pygame.image.load('frame-009.gif'), pygame.image.load('frame-010.gif'), pygame.image.load('frame-011.gif'), pygame.image.load('frame-012.gif'), pygame.image.load('frame-013.gif'), pygame.image.load('frame-014.gif'), pygame.image.load('frame-015.gif'), pygame.image.load('frame-016.gif'), pygame.image.load('frame-017.gif'), pygame.image.load('frame-018.gif'), pygame.image.load('frame-019.gif'), pygame.image.load('frame-020.gif'), pygame.image.load('frame-021.gif'), pygame.image.load('frame-022.gif'), pygame.image.load('frame-023.gif'), pygame.image.load('frame-024.gif'), pygame.image.load('frame-025.gif'), pygame.image.load('frame-026.gif'), pygame.image.load('frame-027.gif'), pygame.image.load('frame-028.gif'), pygame.image.load('frame-029.gif'), pygame.image.load('frame-030.gif'), pygame.image.load('frame-031.gif'), pygame.image.load('frame-032.gif'), pygame.image.load('frame-033.gif'), pygame.image.load('frame-034.gif'), pygame.image.load('frame-035.gif'), pygame.image.load('frame-036.gif'), pygame.image.load('frame-037.gif'), pygame.image.load('frame-038.gif'), pygame.image.load('frame-039.gif'), pygame.image.load('frame-040.gif'), pygame.image.load('frame-041.gif'), pygame.image.load('frame-042.gif'), pygame.image.load('frame-043.gif'), pygame.image.load('frame-044.gif'), pygame.image.load('frame-045.gif'), pygame.image.load('frame-046.gif'), pygame.image.load('frame-047.gif'), pygame.image.load('frame-048.gif'), pygame.image.load('frame-049.gif')]


#Criando instância de tempo 
clock = pygame.time.Clock()

#Som da bala e do hit 
bulletSound = pygame.mixer.Sound('bullet.mp3')
hitSound = pygame.mixer.Sound('hit.mp3')

#Carrega música de fundo 
music = pygame.mixer.music.load('musicafundo.mp3')
pygame.mixer.music.play(-1)
