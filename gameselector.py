# Mängu valimise menüü - pygame
# Autorid: Mihkel Põldvere, Fredi Kaarel Kuuse
import pygame



#värvide muutujad
RED = (255,0,0)
GREEN = (0,255,0)
GREEN2 = (20,220,50)
BLUE = (0,0,255)
YELLOW = (255,255,0)
YELLOW2 = (220,220,30)
BLACK = (0,0,0)
WHITE = (255,255,255)

#teksti loomine
def CreateText(msg,font,fs,x,y,tc):
    Text = pygame.font.SysFont(font, fs)
    textSurf = Text.render(msg, True, tc)
    textRect = textSurf.get_rect()
    textRect.center = (x,y)
    screen.blit(textSurf, textRect)

#nupp
def button(msg,x,y,w,h,c,tc,highlight,dt = False,tegevus = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #kas kursor on objekti kohal
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, highlight, (x, y, w, h))
        
        #kutsu funktsioon, kui lisatud
        if click[0] == 1 and tegevus != None:
            #seoses menüü toimimisega võib vajada ümbertegemist
            tegevus()
    else:
        pygame.draw.rect(screen, c, (x, y, w, h))
    
    #teksti vari
    if dt == True:
        CreateText(msg, "Verdana", 30, x+(w/2)+1,y+(h/2)+1, BLACK)
    CreateText(msg, "Verdana", 30, x+(w/2) ,y+(h/2) ,tc)

#algne funktsioon mängu valimise nuppude jaoks
def gameselect(name,x,y,img = None, tegevus = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #kas kursor on objekti kohal
    if x+250 > mouse[0] > x and y+250 > mouse[1] > y:
        pygame.draw.rect(screen, (200,0,200), (x, y, 250, 250))
        
        #hiljem muuta
        if click[0] == 1 and tegevus != None:
            tegevus()
    else:
        pygame.draw.rect(screen, (220,20,220), (x, y, 250, 250))
    
    CreateText(name, "Verdana", 30, x+125 ,y-20 ,BLACK)
    if img == None:
        CreateText("Pilt", "Verdana", 30, x+125 ,y+125 ,WHITE)
        
        
pygame.init()
screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)

#põhifunktsioon
def GameSelector():
    GameSelector = True

    while GameSelector:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #ekraani laius ja kõrgus
        width, height = screen.get_size()
        
        
        #joonista taust
        screen.fill(WHITE)
        
        #hiir
        mouse = pygame.mouse.get_pos()
        
        #nupud
        gameselect("Game 1",width/2-300,height/2-125)
        gameselect("Game 2",width/2+50,height/2-125)
        button("Back",50,height - 100,100,50,YELLOW2,WHITE,YELLOW,True)
        
        #uuenda ekraanil toimuvat
        pygame.display.update()
GameSelector()