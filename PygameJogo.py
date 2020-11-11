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
mixer.music.load('SSSnes.mp3')
mixer.music.play()

#Todos os direitos reservados a Super Soccer, de onde vem a música utilizada neste jogo.

