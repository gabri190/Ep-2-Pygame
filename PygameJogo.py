#EP - Design de Software
#Dupla: Breno Alencar, Gabriel Araújo e Nívea Abreu
#Data:11/11/2020

#JOGO

#Inicialização

#Importando bibliotecas
import pygame

#Iniciando pacotes

pygame.init()
pygame.mixer.init()
#Tela do jogo
largura=800
altura=600
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("projeto python")

#Música

from pygame import mixer 
mixer.init()
mixer.music.load('musicafundo.mp3')
mixer.music.play()
#declarando classes
#chão
Class Ground(pygame.sprite.Sprite):
    def__init__(self):
        pygame.sprite.Sprite__init__(self)

    def update(self):
#heroi do jogo
Class Hero(pygame.sprite.Sprite):
    def__init__(self):
        pygame.sprite.Sprite__init__(self)

    def update(self):
#osbtáculos
Class Obstacles(pygame.sprite.Sprite):
    def__init__(self):
        pygame.sprite.Sprite__init__(self)

    def update(self):

#Todos os direitos reservados a Yasumu pela música utilizada neste jogo.

#Frame rate do jogo
clock=pygame.time.Clock()
FPS=30
