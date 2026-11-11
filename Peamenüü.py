# Peamenüü - pygame
# Autorid: Fredi Kaarel Kuuse, Mihkel Põldvere 
import pygame
import sys
from gameselector import GameSelector
pygame.init()

#RGB värvikoodid
valge = (255, 255, 255)
tumesinine = (0, 0, 139)
roheline = (0, 255, 0)
punane = (255, 0, 0)
sinine = (0, 0, 255)
hall = (128, 128, 128)

#Ekraani suurust saab muuta ja enamik objektid muutuvad sellega koos
ekraan = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
pygame.display.set_caption("Peamenüü")

def mänguvalik(): #Siit saab liikuda järgmisele lehele
    GameSelector() #Hetkel ajutine, tulemus jäi katsetamise käigus. Nupud ei täida veel oma funktsioone
    """
    print("Hello world!")
    pygame.display.set_caption("Vali mäng!") 
    while True:
        for juhtum in pygame.event.get():
            if juhtum.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ekraan.fill(valge)
        pygame.display.update()
    """

def valikud(): #Siia lisanduvad valikud / sätted, kui me nendeni jõuame
    pygame.display.set_caption("Sätted")
    while True:
        for juhtum in pygame.event.get():
            if juhtum.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ekraan.fill(hall) #Ajutiselt muutub ekraan lihtsalt halliks
        pygame.display.update()

def peamenüü(): #Peamenüü funktsioon, mis sisaldab põhilist tsüklit
    while True:
        ekraan.fill(tumesinine)
        hiire_pos = pygame.mouse.get_pos() #Võtab hiire positsiooni
        laius, pikkus = ekraan.get_size() #Võtab ekraani mõõtmed

        #Fondi suurus ei tööta veel dünaamiliselt
        font = pygame.font.SysFont("Calibri", 80)

        nupu_laius = laius * 0.4 #Ühe nupu laius on 40% ekraanist
        nupu_pikkus = pikkus * 0.2 #Ühe nupu pikkus on 20% ekraanist
        nupu_x = laius / 2 - nupu_laius / 2 #Nupu keskele saamiseks vajalikud arvutused
        nupu_y = pikkus / 3 / 2 - nupu_pikkus / 2 #Üks nupp peab paiknema iga ekraanikolmandiku peal

        #Nuppude ristkülikute salvestamine muutujatele. Vajadusel ka asukoha arvutused
        mängi_nupp = pygame.Rect(nupu_x, nupu_y, nupu_laius, nupu_pikkus) 
        valikud_nupp = pygame.Rect(nupu_x, nupu_y + pikkus / 3, nupu_laius, nupu_pikkus)
        välju_nupp = pygame.Rect(nupu_x, nupu_y + pikkus / 3 * 2, nupu_laius, nupu_pikkus)
        
        #Nuppude ekraanile kuvamine. Kui hiire positsioon on nupu peal, siis nupu värv muutub
        pygame.draw.rect(ekraan, roheline if mängi_nupp.collidepoint(hiire_pos) else hall, mängi_nupp)
        pygame.draw.rect(ekraan, sinine if valikud_nupp.collidepoint(hiire_pos) else hall, valikud_nupp)
        pygame.draw.rect(ekraan, punane if välju_nupp.collidepoint(hiire_pos) else hall, välju_nupp)
        
        #Tekstide defineerimine
        mängi_tekst = font.render("Mängi", True, valge)
        valikud_tekst = font.render("Valikud", True, valge)
        välju_tekst = font.render("Välju", True, valge)
        
        #Paneb tekstiplokkide keskpunktiks nuppude keskpunktid ja salvestab muutujatetele.
        #Seda on üpris keeruline lugeda ning tekst ei ole perfektselt keskel, seega tuleb ümber teha ja lihtsustada
        mängi_kesk = mängi_tekst.get_rect(center = (laius / 2, pikkus / 3 / 2))
        valikud_kesk = valikud_tekst.get_rect(center = (laius / 2, pikkus / 3 / 2 * 3)) 
        välju_kesk = välju_tekst.get_rect(center = (laius / 2, pikkus / 3 / 2 * 5))
        
        #Kirjutab vastava teksti vastavasse punkti
        ekraan.blit(mängi_tekst, mängi_kesk)
        ekraan.blit(valikud_tekst, valikud_kesk)
        ekraan.blit(välju_tekst, välju_kesk)
        
        #Kasutaja sisendid
        for juhtum in pygame.event.get():
            if juhtum.type == pygame.QUIT: #Menüü sulgub, kui see ristist kinni panna
                pygame.quit()
                sys.exit()
            if juhtum.type == pygame.MOUSEBUTTONDOWN: #Tuvastab hiireklõpse. Peab muutma, et tuvastaks ainult vasakut
                if mängi_nupp.collidepoint(hiire_pos): #Peab avama mänguvaliku menüü 
                    #mänguvalik() #Tuleb üle vaadata hiljem
                    return 1
                if valikud_nupp.collidepoint(hiire_pos): #Peab avama sätted
                    valikud()
                if välju_nupp.collidepoint(hiire_pos): #Peaks sulgema mängu
                    return -1 #return on alles jäänud lehtede vaheliste funktsioonide katsetamisest. Nupp ei tööta hetkel
                    pygame.quit() 
                    sys.exit()

        pygame.display.update() #Värskendab ekraani

peamenüü() #Peamenüü põhifunktsioon