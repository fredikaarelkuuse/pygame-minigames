# Mäng 1 - pygame
# Autorid: Mihkel Põldvere, Fredi Kaarel Kuuse
import pygame
import random

screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
score = 0

#värvid
RED = (255,0,0)
GREEN = (0,255,0)
GREEN2 = (20,220,50)
BLUE = (0,0,255)
YELLOW = (255,255,0)
YELLOW2 = (220,220,30)
BLACK = (0,0,0)
WHITE = (255,255,255)

#sihtmärgid
targets = {
    "easy1": {"Value": 1, "Speed": 0.2, "Size": [100,100], "Location": [-100,-100], "Color": GREEN2, "HCOLOR": GREEN},
    "medium1": {"Value": 3, "Speed": 0.4, "Size": [76,76], "Location": [-100,-100], "Color": YELLOW2, "HCOLOR": YELLOW}
,    "hard1": {"Value": 10, "Speed": 1, "Size": [20,20], "Location": [-100,-100], "Color": RED, "HCOLOR": BLACK},
}

#teksti loomine
def CreateText(msg,font,fs,x,y,tc):
    Text = pygame.font.SysFont(font, fs)
    textSurf = Text.render(msg, True, tc)
    textRect = textSurf.get_rect()
    textRect.center = (x,y)
    screen.blit(textSurf, textRect)

#nupu loomine
def button(msg,x,y,w,h,c,tc,highlight,dt = False,tegevus = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #kas kursor on objekti kohal
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, highlight, (x, y, w, h))
        
        if click[0] == 1 and tegevus != None:
            tegevus()
    else:
        pygame.draw.rect(screen, c, (x, y, w, h))
    
    #teksti vari
    if dt == True:
        CreateText(msg, "Verdana", 30, x+(w/2)+1,y+(h/2)+1, BLACK)
    CreateText(msg, "Verdana", 30, x+(w/2) ,y+(h/2) ,tc)

#sihtmärgi joonistamine
def item(x,y,w,h,color,hcolor,p):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #kas kursor on objekti kohal
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hcolor, (x, y, w, h))
        
        if click[0] == 1 and p != None:
            reset_target(p)
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

#sihtmärgi 'resetimine' kui sellele pihta saadakse
def reset_target(t):
    global score
    #punktid
    score += targets[t]["Value"]
    
    #targets[t]["Idle"] = True
    targets[t]["Location"] = [random.randint(25, screen.get_size()[0] - 50),-targets[t]["Size"][1]]
    
pygame.init()
#screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)

#peafunktsioon
def game_aim():
    AimTraining = True
    global targets
    global score
    
    #reseti sihtmärgid enne mängu
    for target in targets:
        reset_target(target)
    score = 0
    while AimTraining:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        width, height = screen.get_size()
        #joonista taust
        screen.fill(WHITE)
        
        #implementeerida miinuspunkti lisamine möödavajutuse eest
        
        #sihtmärgite haldus
        for target in targets:
            # legacy kood, hiljem eemaldada
            #if targets[target]["Idle"]:
                #test väärtused, hiljem muuta
                #targets[target]["Location"] = [random.randint(25, width - 50),-targets[target]["Size"][1]]
                #targets[target]["Idle"] = False
            #else:
            
            targets[target]["Location"][1] += targets[target]["Speed"]
            x, y = targets[target]["Location"]
            w, h = targets[target]["Size"]
            item(x, y, w, h,targets[target]["Color"],targets[target]["HCOLOR"],target)
            if targets[target]["Location"][1] > height:
                targets[target]["Location"] = [random.randint(25, width - 50),-50]
                score -= 10
                
        
        
        #hiir
        mouse = pygame.mouse.get_pos()
        
        #nupud ja menüüelemendid
        #skoori paiknemine ülevaadata, praegu ajutine fix
        button("Back",50,height - 100,100,50,YELLOW2,WHITE,YELLOW,True)
        CreateText("Score: " + str(score), "Verdana", 24, 60 + 6*len(str(score)),10 ,BLACK)
        
        pygame.display.update()
game_aim()