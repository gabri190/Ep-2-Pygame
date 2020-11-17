#EP - Design de Software
#Dupla: Breno Alencar, Gabriel Araújo e Nívea Abreu
#Data:11/11/2020

#JOGO

#Inicialização

#Importando bibliotecas
import pygame

#Iniciando pacotes


pygame.init()
x=400
y=100
velocidade=10
fundo=pygame.image.load('fundo.png')
pygame.mixer.init()
#Tela do jogo
largura=1070
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

janela_aberta=True
while janela_aberta:
	pygame.time.delay(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			janela_aberta=False
	comandos=pygame.key.get_pressed()
	if comandos[pygame.K_UP]:
		y -=velocidade
	if comandos[pygame.K_DOWN]:
		y +=velocidade
	if comandos[pygame.K_RIGHT]:
		x +=velocidade
	if comandos[pygame.K_LEFT]:
		x -=velocidade

#Frame rate do jogo
clock=pygame.time.Clock()
FPS=30
