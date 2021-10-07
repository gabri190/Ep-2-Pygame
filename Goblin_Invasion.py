
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
bgs = [pygame.image.load('frame-001.gif'), pygame.image.load('frame-002.gif'), pygame.image.load('frame-003.gif'), pygame.image.load('frame-004.gif'), pygame.image.load('frame-005.gif'), pygame.image.load('frame-006.gif'), pygame.image.load('frame-007.gif'), pygame.image.load('frame-008.gif'), pygame.image.load('frame-009.gif'), pygame.image.load('frame-010.gif'), pygame.image.load('frame-011.gif'), pygame.image.load('frame-012.gif'), pygame.image.load('frame-013.gif'), pygame.image.load('frame-014.gif'), pygame.image.load('frame-015.gif'), pygame.image.load('frame-016.gif'), pygame.image.load('frame-017.gif'), pygame.image.load('frame-018.gif'), pygame.image.load('frame-019.gif'), pygame.image.load('frame-020.gif'), pygame.image.load('frame-021.gif'), pygame.image.load('frame-022.gif'), pygame.image.load('frame-023.gif'), pygame.image.load('frame-024.gif'), pygame.image.load('frame-025.gif'), pygame.image.load('frame-026.gif'), pygame.image.load('frame-027.gif'), pygame.image.load('frame-028.gif'), pygame.image.load('frame-029.gif'), pygame.image.load('frame-030.gif'), pygame.image.load('frame-031.gif'), pygame.image.load('frame-032.gif'), pygame.image.load('frame-033.gif'), pygame.image.load('frame-034.gif'), pygame.image.load('frame-035.gif'), pygame.image.load('frame-036.gif'), pygame.image.load('frame-037.gif'), pygame.image.load('frame-038.gif'), pygame.image.load('frame-039.gif'), pygame.image.load('frame-040.gif'), pygame.image.load('frame-041.gif'), pygame.image.load('frame-042.gif'), pygame.image.load('frame-043.gif'), pygame.image.load('frame-044.gif'), pygame.image.load('frame-045.gif'), pygame.image.load('frame-046.gif'), pygame.image.load('frame-047.gif'), pygame.image.load('frame-048.gif'), pygame.image.load('frame-049.gif')]


#Criando instância de tempo 
clock = pygame.time.Clock()

#Som da bala e do hit 
bulletSound = pygame.mixer.Sound('bullet.mp3')
hitSound = pygame.mixer.Sound('hit.mp3')

#Carrega música de fundo 
music = pygame.mixer.music.load('musicafundo.mp3')
pygame.mixer.music.play(-1)

#definindo personagem(jogador e inimigo)
class character(object):
    def __init__(self,x,y,width,height,vel,walkCount,health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel 
        self.walkCount=walkCount
        self.health=health


#Definido classe do jogador
class player(character):
    walkRight=[]
    for i in range(1,10):
        string='R'+str(i)+'.png'
        walkRight.append(pygame.image.load(string))
    #imagens do inimigo caminhado para a esquerda
    walkLeft=[]
    for i in range(1,10):
        string='L'+str(i)+'.png'
        walkLeft.append(pygame.image.load(string))
   
    def __init__(self,x,y,width,height):  #Construtor da classe e parâmetros iniciais 
        super().__init__(x,y,width,height,2.5,0,10)
                          
        self.velJump = 0                  #Velocidade do pulo
        self.isJump = False               #"Estado de pulo"
        self.left = False                 #"Estado de personagem encarando a esquerda"
        self.right = True                 #"Estado de personagem encarando a direita"
        self.standing = True              #Permanecer
        self.gravity = 1.5                #Gravidade
        self.velJump=0                    #Velocidade do pulo
        #vida do personagem
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
                win.blit(player.walkLeft[self.walkCount//6], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(player.walkRight[self.walkCount//6], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(player.walkRight[0], (self.x, self.y))
            else:
                win.blit(player.walkLeft[0], (self.x, self.y))

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
class enemy(character):
    #imagens do inimigo caminhando para a direita
    walkRight=[]
    for i in range(1,12):
        string='R'+str(i)+'E.png'
        walkRight.append(pygame.image.load(string))
    #imagens do inimigo caminhado para a esquerda
    walkLeft=[]
    for i in range(1,12):
        string='L'+str(i)+'E.png'
        walkLeft.append(pygame.image.load(string))
   

    def __init__(self, x, y, width, height, end): #Construtor da classe e parâmetros iniciais 
        super().__init__(x,y,width,height,random.randint(-150,150)/100, random.randint(1,66),10)
        self.end = end#ate onde o inimigo pode caminhar
        self.path = [self.x, self.end]#lista com a posicao em inicial e a posicao final, que o inimigo pode ir 
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)#hitbox (eixo x,eixoy,largura ,altura)
       #vida do inimigo
        self.bullets=[]#balas
#cria a função de desenho do inimigo
    def draw(self,win):
        self.move()#inimigo se movendo  
        if self.walkCount + 1 >= 66:#contador de passos nao pode ser maior q 66
            self.walkCount = 0#reseta a contagem
        if self.walkCount==48:
            self.shoot()#atira 
#velocidade do inimigo maior que 0
        win.blit(self.walkLeft[self.walkCount //6], (self.x, self.y))
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //6], (self.x, self.y))#atualiza posicao do inimigo para direita
            self.walkCount += 1#incremento no contador de passo
        
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
        facing=1#face virada para a direita
        if self.vel < 0:#se velocidade menor que 0
            facing = -1 #face virada para a esquerda 
       
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

#classe que junta os obstaculos(obstacles) aos coracoes(heart_life)
class Scenario(object):
    def __init__(self, x, y, width, height,image,lista):#Construtor da classe e parâmetros iniciais
        self.x = x
        self.y = y
        self.width = width
        self.height = height    
        self.listImage=[pygame.image.load(image)]
        self.hitbox = [self.x+lista[0], self.y+lista[1], self.width+lista[2], self.height+lista[3]]

    def draw(self,win):
        image = pygame.transform.scale(self.listImage[0].convert_alpha(),(self.width,self.height))#transformação de escala da imagem
        win.blit(image,(self.x,self.y))#atualiza
#classe dos obstaculos
class obstacle(Scenario):
    def __init__(self, x, y, width, height):#Construtor da classe e parâmetros iniciais
        super().__init__( x, y, width, height,'caixa.png',[0,0,0,0])
       
    
    
        
#classe das vidas ganhar ao passar pelo coração
class heart_life(Scenario):
    def __init__(self, x, y, width, height):##Construtor da classe e parâmetros iniciais
        super().__init__( x, y, width, height,'heart.png',[4,4,-8,-10] )
        #hitbox do coracao
        
#Verifica o estado dos personagens
def estados_personagens():
    if man.health>0 and len(goblins)>0:
       return "vivo"
    elif(man.health==0):
        return "perdeu"
    elif(len(goblins)==0):
        return "ganhou"
    
        
#função principal de desenho
def redrawGameWindow(countBg):
    if countBg[0] > 146: #se o contador de background maior que 146
        countBg[0]=0 #reseta o contador de background
    
    win.blit(pygame.transform.scale(bgs[countBg[0]//3].convert_alpha(),(winWidth,winHeight)), (0,0)) #atualiza imagem de fundo
    text = font.render('Life: ' + str(man.health), 1, (100,255,100))#escreve um texto sobre a saude do homem
    win.blit(text, (350, 10))#atualiza o texto
#se saude do homem maior que 0 e se a lista de goblins não está vazia
    if estados_personagens()=="vivo":
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
    if estados_personagens()=="perdeu":
        font1 = pygame.font.SysFont('roboto', 50)
        text1 = font1.render('YOU DIE!!!', 1, (255,0,0))#texto voce morreu
        win.blit(text1, (winWidth/2 - (text1.get_width()/2),winHeight/2))#atualiza o texto

        font2 = pygame.font.SysFont('roboto', 30)
        text2 = font2.render('Press ENTER to Restart!', 1, (200,200,200))#texto pressiona enter 
        win.blit(text2, (winWidth/2 - (text2.get_width()/2),winHeight/2+50))#atuliza o texto

    #se a lista de goblins está vazia
    if  estados_personagens()=="ganhou":
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

# funca de atirar
def shoot(char,bullets):
    bulletSound.play()#som do tiro
    facing=1
    if char.left:#atirar para esquerda
        facing = -1#face voltada para a esquerda
    
   #quantidade de balas     
    if len(bullets) < 20:
        #adicao de balas na lista bullets colocando a posicao do projetil e as cores
        bullets.append(projectile(round(char.x + char.width //2), round(char.y + char.height//2), 6, (0,0,255),(0,0,0), facing))

def start():
    countBg=[0]#contador de background
    font = pygame.font.SysFont('comicsans', 30, True)#texto
    man = player(100, 500, 64,64)#posicao inicial do jogador
    goblins = [enemy(200, 500, 64, 64, 265),enemy(330, 500, 64, 64, 400),enemy(900, 500, 64, 64, 1000)]#posicao inicial dos 3 inimigos
#posicao da caixa (a cada 100 pixels no eixo x  ,no eixo y a posicao fica aleatória)
    caixas = [obstacle(500,random.randint(100,500),64,64),obstacle(600,random.randint(100,500),64,64),obstacle(700,random.randint(100,500),64,64),obstacle(800,random.randint(100,500),64,64)]
#posicao dos coracoes (nem todas as caixas possuem coração)   
    hearts = [heart_life(caixas[0].x+16,caixas[0].y-30,32,32),heart_life(caixas[1].x+16,caixas[1].y-30,32,32),heart_life(caixas[3].x+16,caixas[3].y-30,32,32)]
    shootLoop = 0 #variável para criar intervalo entre as balas
    bullets = []#lista de balas (inicialmente vao ser adicionadas balas)
    floor=500 #posição do chão
    run = True #variável de condição do laço
    return [countBg,font, man, goblins, caixas, hearts, shootLoop, bullets, floor, run] #retorna todas as variáveis
    
countBg,font, man, goblins, caixas, hearts, shootLoop, bullets, floor, run = start()# executa a função start 

#inicio do loop
while run:
    clock.tick(54)#contador de frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#se o usuário clicou para fechar o jogo
            run = False #variável de condição do laço igual a falso, interrompe laço
    keys = pygame.key.get_pressed()#havendo teclas pressionadas
    if (keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and (man.health == 0 or len(goblins)==0):#se a tecla enter é pressionada quando o jogador está morto ou matou todos os inimigos
            countBg,font, man, goblins, caixas, hearts, shootLoop, bullets, floor, run = start() #reinicia o jogo
#se saude do homem maior que 0 e se a lista de goblins não está vazia
    if man.health>0 and len(goblins)>0:
        for heart in hearts:
            #condicoes em que o homem encontra o coracao
            if man.hitbox[1] < heart.hitbox[1] + heart.hitbox[3] and man.hitbox[1] + man.hitbox[3] > heart.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > heart.hitbox[0] and man.hitbox[0] < heart.hitbox[0] + heart.hitbox[2]:
                    if man.health<10:#se saude menor que 10
                        man.recover()#recuperacao de vida
                    hearts.pop(hearts.index(heart))#remove o coracao
        for goblin in goblins:
            #condicoes de colisao entre homem e inimigo(goblin)
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    man.hit()#colisao do home
                    if man.imunityTime==0:#se tempo de imunidade do homem nulo
                        man.imunityTime=20#retorna ao tempo de imunidade inicial
                    
     
    #variável de delay entre os tiros
        if shootLoop > 0:#se variável de delay maior que 0
            shootLoop += 1#incremento na variavel de delay
        if shootLoop > 20:#se variável de delay maior que 20
            shootLoop = 0#reseta variável de delay, jogador pode atirar novamente
        
        
  #condicao em que a bala atinge o goblin      
        for bullet in bullets:
            for goblin in goblins:
                if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                    if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                        hitSound.play()
                        goblin.hit()#colisao do goblin com a bala
                        bullets.pop(bullets.index(bullet))#remocao da bala
                        if goblin.health==0:#se vida nula do inimigo(goblin)
                            goblins.pop(goblins.index(goblin))#ele é removido do jogo
                            
                
  #a bala nao pode ultrapassar no eixo x os pixels da tela                      
            if bullet.x < winWidth and bullet.x > 0:
                bullet.x += bullet.vel
            else:#caso contrario ela e removida
                bullets.pop(bullets.index(bullet))
 #goblin atirando no jogador       
        for goblin in goblins:
            for bullet in goblin.bullets:
                #condicoes para a bala atingir o jogador
                if bullet.y - bullet.radius < man.hitbox[1] + man.hitbox[3] and bullet.y + bullet.radius > man.hitbox[1]:
                    if bullet.x + bullet.radius > man.hitbox[0] and bullet.x - bullet.radius < man.hitbox[0] + man.hitbox[2]:
                        hitSound.play()
                        man.hit()#jogador atingido
                        goblin.bullets.pop(goblin.bullets.index(bullet))#bala removida
            #a bala nao pode ultrapassar no eixo x os pixels da tela            
                if bullet.x < winWidth and bullet.x > 0:
                    bullet.x += bullet.vel
                else:#caso contrario a bala é removida
                    goblin.bullets.pop(goblin.bullets.index(bullet))
        #apertando a tecla espaco
        if keys[pygame.K_SPACE] and shootLoop == 0:
            shoot(man,bullets)#atira as balas
            shootLoop = 1
#apertando o comando esquerda
        if keys[pygame.K_LEFT] and man.x > man.vel:
            canmove=True#homem pode se mover
            for caixa in caixas:
                if verificar(caixa,man.hitbox[0] - man.vel,man.hitbox[1]):#verifica condicoes de colisao nas laterais entre caixa e jogador
                    canmove=False#ele nao pode se mover
            if canmove:#se ele pode se mover
                man.x -= man.vel#muda a posição do jogador
                man.left = True #jogador encara a esquerda
                man.right = False
                man.standing = False
#apertando o comando direita         
        elif keys[pygame.K_RIGHT] and man.x < winWidth - man.width - man.vel:#condicoes para o homem se mover
            canmove=True#homem pode se mover
            for caixa in caixas:
                if verificar(caixa,man.hitbox[0] + man.vel,man.hitbox[1]):#verifica condicoes de colisao nas laterais entre caixa e jogador
                    canmove=False#ele nao pode se mover
            if canmove:#se ele pode se mover
                man.x += man.vel#muda a posição do jogador
                man.right = True #jogador encara a direita
                man.left = False
                man.standing = False
        else:#não apertou nenhum comando
            man.standing = True
            #man.walkCount = 0
#incrementa velocidade do pulo de acordo com a gravidade
        man.velJump += man.gravity
        man.y+=man.velJump#incrementa a posicao y do jogador
        if man.y>floor:#se posicao maior que o chão
            man.y=floor#posição do jogador igual a posição do chão
            man.velJump=0#velocidade do pulo nula
#verificando condicoes de colisao da caixa com o jogador        
        for caixa in caixas:
            if (man.hitbox[0]+man.hitbox[2] > caixa.hitbox[0] and man.hitbox[0] < caixa.hitbox[0]+caixa.hitbox[2] and man.velJump>0) and ((man.y+man.height > caixa.y and man.y < caixa.y and (man.y-man.velJump)+man.height<caixa.y) or man.y-man.velJump==caixa.y-man.height):
                man.y=caixa.y-man.height#atualiza posicao do jogador em y 
                man.velJump=0#velocidade do pulo nula
            
#condicao em que o homem nao esta pulando e a velocidade de pulo igual a zero      
        if not(man.isJump) and man.velJump==0:
            #aperta a tecla K_UP do teclado
            if keys[pygame.K_UP]:
                man.isJump = True#homem pula
                man.walkCount = 0#reseta contador de passos
                man.velJump = -30#define a velocidade do pulo
                cont=0
 #condicao em que o homem está pulando               
        else:
            #velocidade do pulo do jogador nula
            if man.velJump==0:
                cont+=1#incrementa o contador
            if cont==2:#2° contagem
                cont=0#volta ao inicio
                man.isJump = False#homem para de pular

 #desenho da tela atualizado
    redrawGameWindow(countBg)
    
#saida do jogo
pygame.quit()