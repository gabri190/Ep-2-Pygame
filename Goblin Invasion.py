
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

#Definido classe do jogador
class player(object):
    def __init__(self,x,y,width,height):  #Construtor da classe e parâmetros iniciais 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2.5                    #Velocidade do jogador
        self.velJump = 0                  #Velocidade do pulo
        self.isJump = False               #"Estado de pulo"
        self.left = False                 #"Estado de personagem encarando a esquerda"
        self.right = True                 #"Estado de personagem encarando a direita"
        self.standing = True              #Permanecer
        self.walkCount = 0                #Contador de passos
        self.gravity = 1.5                #Gravidade
        self.velJump=0                    #Velocidade do pulo
        self.health=10                    #vida do personagem
        self.countHit=0                   #Contador de hit
        self.countRecover=0               #Contador de recuperação
        self.imunityTime=0                #Tempo de imunidade
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)     #Caixa de colisão

    #Criando função de desenho na tela
    def draw(self, win):
        
        #Se toma dano, printa na tela '-1hp' em posição definida, decrementa contador de hit
        
        if self.countHit>0:
            font1 = pygame.font.SysFont('roboto', 50)
            text = font1.render('-1 hp', 1, (175,0,0))
            win.blit(text, (self.x+self.width/2 - (text.get_width()/2),self.y-50))
            self.countHit-=1
        
        #Se colide com o coração, printa na tela '+1hp' em posição definida, decrementa contador de recuperação
        
        if self.countRecover>0:
            font1 = pygame.font.SysFont('roboto', 50)
            text = font1.render('+1 hp', 1, (0,175,0))
            win.blit(text, (self.x+self.width/2 - (text.get_width()/2),self.y-50))
            self.countRecover-=1
        
        #Se tempo de imunidade maior que zero, decrementa tempo
        
        if self.imunityTime>0:
            self.imunityTime-=1

        #Se o contador de passos mais 1 for maior que o numero de sprite vezes 6 frames, retorna a zero
        if self.walkCount + 1 >= 54:
            self.walkCount = 0
            
         #Se não estiver parado, atualiza na tela elementos da lista de acordo com os passos e esquerda ou direita
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//6], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//6], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        #Desenha a barra de vida vermelha e uma verde por cima, reduzindo a verde de acordo com a saúde
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        
        #Posiciona hitbox
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

        #Criando caixa de colisão para compreender bugs nas colisões
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    #Define hit(colisão)
    def hit(self):
        if self.imunityTime==0:#se tempo de imunidade esgotado
            self.health-=1#jogador perde 1 de vida
            self.isJump = False#jogador não está pulando
            self.velJump=0#velocidade do jogador igual a 0
            self.walkCount = 0#contador de passos igual a 0
            self.countHit=10#contador de colisao
    def recover(self):#recuperação de vidas
        self.health+=1#incrementa 1 na vida ao jogador
        self.countRecover=10#contador de recuperacao
#classe projétil
class projectile(object):
    def __init__(self,x,y,radius,color1,color2,facing): #Construtor da classe e parâmetros iniciais 
        self.x = x
        self.y = y
        self.radius = radius#raio do circulo que corresponde ao projetil
        self.color1 = color1#cor 1
        self.color2 = color2#cor2
        self.facing = facing#lado que o projétil voa
        self.vel = 4 * facing#velocidade do projetil
#cria a função de desenho
    def draw(self,win):
        pygame.draw.circle(win, self.color1, (self.x,self.y), self.radius)   #desenho do círculo interno
        pygame.draw.circle(win, self.color2, (self.x,self.y), self.radius,1) #desenho do círculo externo


#classe do inimigo
class enemy(object):
    #caminha para direita(imagens)
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    #caminha para a esquerda(imagens)
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end): #Construtor da classe e parâmetros iniciais 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end#ate onde o inimigo pode caminhar
        self.path = [self.x, self.end]#lista com a posicao em inicial e a posicao final, que o inimigo pode ir 
        self.walkCount = random.randint(1,66)#contador de passos aleatório
        self.vel = random.randint(-150,150)/100#velocidade aleátoria do inimigo
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)#hitbox (eixo x,eixoy,largura ,altura)
        self.health = 10#vida do inimigo
        self.bullets=[]#balas
#cria a função de desenho do inimigo
    def draw(self,win):
        self.move()#inimigo se movendo  
        if self.walkCount + 1 >= 66:#contador de passos nao pode ser maior q 66
            self.walkCount = 0#reseta a contagem
        if self.walkCount==48:
            self.shoot()#atira 
#velocidade do inimigo maior que 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //6], (self.x, self.y))#atualiza posicao do inimigo para direita
            self.walkCount += 1#incremento no contador de passo
        else:
            win.blit(self.walkLeft[self.walkCount //6], (self.x, self.y))#atualiza posicao do inimigo para esquerda
            self.walkCount += 1#incremento no contador de passos
        
         #Desenha a barra de vida vermelha e uma verde por cima, reduzindo a verde de acordo com a saúde
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

        #Posiciona hitbox
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #Criando caixa de colisão para compreender bugs nas colisões
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        
 #função para o  inimigo atirar   
    def shoot(self):
        bulletSound.play()#som do tiro
        if self.vel < 0:#se velocidade menor que 0
            facing = -1 #face virada para a esquerda 
        else:
            facing = 1#face virada para a direita
#adicao de balas na lista bullets colocando a posicao do projetil e as cores
        self.bullets.append(projectile(round(self.x + self.width //2), round(self.y + self.height//2), 6, (255,0,0),(0,0,0), facing))

#inimigo se movimentando        
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:#se o inimigo pode ir ate a posicao 1 da lista path(fim da tela para o inimigo)
                self.x += self.vel #incrementa a posição x do inimigo
            else:                               #se o inimigo so nao pode ir ate a posicao 1 da lista path(fim da tela para o inimigo)
                self.vel = self.vel * -1 #inverte a velocidade
                self.walkCount = 0#reseta o contador de passos do inimigo
        else:
            if self.x - self.vel > self.path[0]:#se o inimigo pode ir ate a posicao 0 da lista path(fim da tela para o inimigo)
                self.x += self.vel #incrementa a posição x do inimigo
            else:                               #se o inimigo so nao pode ir ate a posicao 0 da lista path(fim da tela para o inimigo)
                self.vel = self.vel * -1 #inverte a velocidade
                self.walkCount = 0#reseta o contador de passos do inimigo
#colisao
    def hit(self):
        if self.health > 0:
            self.health -= 1#perde 1 de vida
            
#classe dos obstaculos
class obstacle(object):
    def __init__(self, x, y, width, height):#Construtor da classe e parâmetros iniciais
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.listObstacle = [pygame.image.load('caixa.png')]#imagem da caixa
        self.hitbox = [self.x, self.y, self.width, self.height]#hitbox da caixa
#cria a função de desenho dos obstaculos (caixas)
        
    def draw(self,win):
        image = pygame.transform.scale(self.listObstacle[0].convert_alpha(),(self.width,self.height))#transformação de escala da imagem
        win.blit(image,(self.x,self.y))#atualiza
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        
#classe das vidas ganhar ao passar pelo coração
class heart_life(object):
    def __init__(self, x, y, width, height):##Construtor da classe e parâmetros iniciais
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.listHearts = [pygame.image.load('heart.png')]#imagem coracao
        self.hitbox = [self.x+4, self.y+4, self.width-8, self.height-10]#hitbox do coracao
        
#desenho do coracao
    def draw(self,win):
        image = pygame.transform.scale(self.listHearts[0].convert_alpha(),(self.width,self.height))#transformação de escala
        win.blit(image,(self.x,self.y))#atualiza
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    #função de principal de desenho
def redrawGameWindow(countBg):
    if countBg[0] > 146: #se o contador de background maior que 146
        countBg[0]=0 #reseta o contador de background
    
    win.blit(pygame.transform.scale(bgs[countBg[0]//3].convert_alpha(),(winWidth,winHeight)), (0,0)) #atualiza imagem de fundo
    text = font.render('Life: ' + str(man.health), 1, (100,255,100))#escreve um texto sobre a saude do homem
    win.blit(text, (350, 10))#atualiza o texto
#se saude do homem maior que 0 e se a lista de goblins não está vazia
    if man.health>0 and len(goblins)>0:
        man.draw(win)#desenho na tela do homem
        #desenhos do goblin ,balas ,coração e caixa em cada grupo respectivo a essas classes
        for goblin in goblins:
            goblin.draw(win)
            for bullet in goblin.bullets:
                bullet.draw(win)
        for caixa in caixas:
            caixa.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        for heart in hearts:
            heart.draw(win)
    #se saude do homem igual a 0
    if man.health==0:
        font1 = pygame.font.SysFont('roboto', 50)
        text1 = font1.render('YOU DIE!!!', 1, (255,0,0))#texto voce morreu
        win.blit(text1, (winWidth/2 - (text1.get_width()/2),winHeight/2))#atualiza o texto

        font2 = pygame.font.SysFont('roboto', 30)
        text2 = font2.render('Press ENTER to Restart!', 1, (200,200,200))#texto pressiona enter 
        win.blit(text2, (winWidth/2 - (text2.get_width()/2),winHeight/2+50))#atuliza o texto

    #se a lista de goblins está vazia
    if len(goblins)==0:
        font1 = pygame.font.SysFont('roboto', 50)
        text1 = font1.render('YOU WIN!', 1, (0,255,0))#texto voce ganhou
        win.blit(text1, (winWidth/2 - (text1.get_width()/2),winHeight/2))#atualiza o texto

        font2 = pygame.font.SysFont('roboto', 30)
        text2 = font2.render('Press ENTER to Restart!', 1, (200,200,200))#texto pressiona enter
        win.blit(text2, (winWidth/2 - (text2.get_width()/2),winHeight/2+50))#atualiza o texto
    countBg[0]+=1 #incrementa o contador de background

        
#atualiza o jogo        
    pygame.display.update()
#verifica a condicao de colisao do homem e a caixa
def verificar(caixa,x,y):
    if y < caixa.hitbox[1] + caixa.hitbox[3] and y + man.hitbox[3] > caixa.hitbox[1]:
        if x + man.hitbox[2] > caixa.hitbox[0] and x < caixa.hitbox[0] + caixa.hitbox[2]:
            return True
    return False
   
