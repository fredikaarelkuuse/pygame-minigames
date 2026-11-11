import pygame
import random

screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
score = 0

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
    "easy1": {"Idle": True, "Value": 1, "Speed": 0.2, "Size": [100,100], "Location": [-100,-100], "Color": GREEN2, "HCOLOR": GREEN},
    "medium1": {"Idle": True, "Value": 3, "Speed": 0.4, "Size": [76,76], "Location": [-100,-100], "Color": YELLOW2, "HCOLOR": YELLOW}
,    "hard1": {"Idle": True, "Value": 10, "Speed": 1, "Size": [20,20], "Location": [-100,-100], "Color": RED, "HCOLOR": BLACK},
}

def CreateText(msg,font,fs,x,y,tc):
    Text = pygame.font.SysFont(font, fs)
    textSurf = Text.render(msg, True, tc)
    textRect = textSurf.get_rect()
    textRect.center = (x,y)
    screen.blit(textSurf, textRect)

def button(msg,x,y,w,h,c,tc,highlight,dt = False,tegevus = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, highlight, (x, y, w, h))
        
        if click[0] == 1 and tegevus != None:
            tegevus()
    else:
        pygame.draw.rect(screen, c, (x, y, w, h))
    
    if dt == True:
        CreateText(msg, "Verdana", 30, x+(w/2)+1,y+(h/2)+1, BLACK)
    CreateText(msg, "Verdana", 30, x+(w/2) ,y+(h/2) ,tc)

def item(x,y,w,h,color,hcolor,p):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hcolor, (x, y, w, h))
        
        if click[0] == 1 and p != None:
            reset_target(p)
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))
        
def reset_target(t):
    global score
    score += targets[t]["Value"]
    targets[t]["Idle"] = True
    targets[t]["Location"] = [-100,-100]
    
pygame.init()
#screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)

def game_aim():
    AimTraining = True
    global targets
    global score

    while AimTraining:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        width, height = screen.get_size()
        #joonista taust
        screen.fill(WHITE)
        
        #implementeerida miinuspunkti lisamine möödavajutuse eest
        for target in targets:
            if targets[target]["Idle"]:
                #test väärtused, hiljem muuta
                targets[target]["Location"] = [random.randint(25, width - 50),-110]
                targets[target]["Idle"] = False
            else:
                targets[target]["Location"][1] += targets[target]["Speed"]
                x, y = targets[target]["Location"]
                w, h = targets[target]["Size"]
                item(x, y, w, h,targets[target]["Color"],targets[target]["HCOLOR"],target)
                if targets[target]["Location"][1] > height:
                    targets[target]["Location"] = [random.randint(25, width - 50),-50]
                    score -= 10
                
        
        
        #hiir
        mouse = pygame.mouse.get_pos()
        
        #item(20,20,100,50,YELLOW2,YELLOW,2)
        button("Back",50,height - 100,100,50,YELLOW2,WHITE,YELLOW,True)
        CreateText("Score: " + str(score), "Verdana", 24, 60,10 ,BLACK)
        
        pygame.display.flip()
        pygame.display.update()
game_aim()