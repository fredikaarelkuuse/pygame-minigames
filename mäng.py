# Mäng 2 – Pygame
# Autorid: Fredi Kaarel Kuuse, Mihkel Põldvere
import pygame
import sys
import random

helekollane = (255, 255, 224) #Defineerin RGB koodiga kasutatavad värvused
roheline = (0, 255, 0)
punane = (255, 0, 0)
sinine = (0, 0, 255)

kukkumine, kukkumiskiirus, kiirendus, energia  = True, 0, 0, 3 #Baasväärtused, mida ma kasutasin mängija ülesse ja alla liigutamiseks

ekraan = pygame.display.set_mode((960, 540)) #Objektide suurus vastavalt ekraani suurusele pole veel lisatud, aga on plaanis
laius, pikkus = ekraan.get_size()
pygame.display.set_caption("Mäng 2")

FPS = pygame.time.Clock() #Määran funktsiooni, mis tagab mängukiiruse ühtluse

#Takistused on mitmekihilises hulgas, kus esimene pool on takistuse andmed ja teine pool nendes paikneva augu ehk värava andmed
#Plaanin teha takistused vähem seaduspäraseks
takistused = [[[laius, 0, 50, pikkus], [laius, random.randint(pikkus*0.2, pikkus*0.8), 50, 100]],
              [[laius*0.5, 0, 50, pikkus], [laius*0.5, random.randint(pikkus*0.2, pikkus*0.8), 50, 100]],
              [[laius*0.75, 0, 50, pikkus], [laius*0.75, random.randint(pikkus*0.2, pikkus*0.8), 50, 100]]]

#Tsoonid on paaris järjendid, kus üks on mängijale ohtlik ja teine tagab turvalisuse
#Neid kirjutatakse pidevalt üle
tsoonid =[[0, 0], [0, 0], [0, 0]]

def takistuse_pos(takistus): #See funktsioon tegeleb takistuste ja väravate liigutamisega
    if takistus[0] <= -50: #Kui takistus on täielikult ekraanilt lahkunud jõuab ta uuesti paremale (teeb ringe)
        takistus[0] = laius
    else:
        takistus[0] -= 2 #Takistuse x koordinaat väheneb ehk takistus läheneb mängijale
    return(takistus)

def kaotus(): #Kutsutakse välja kui mängija kaotab ja "jäätab" ekraani. Hiljem peaks olema võimalik näha skoori ja uuesti alustada
    while True:
        for sündmus in pygame.event.get():
            if sündmus.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
while True: #Põhitsükkel
    ekraan.fill(helekollane)

    #Mängija positsiooniga seotud arvutused, mida võiks eraldi funktsiooni liigutada
    if kukkumine:
        kiirendus += 0.1
        kukkumiskiirus -= kiirendus
    else:
        kukkumiskiirus += energia
        energia -= 0.1 #Energia kahaneb ehk hoog on algul kiirem
        if energia <= 0:
            kukkumine = True
            kiirendus, energia = 0, 3

    #Käib läbi iga takistuse ja selle värava andmed
    for el in takistused:
        takistus = takistuse_pos(el[0])
        värav = takistuse_pos(el[1]) #Väravat saab samuti takistuse_pos funktsiooniga arvutada
        
        pygame.draw.rect(ekraan, sinine, (takistus))
        pygame.draw.rect(ekraan, helekollane, (värav))

        #Määratakse muutujatele ristkülikud, et hiljem kontrollida, kas mängija neid puudutab
        ohutsoon = (pygame.Rect((takistus))) 
        turvatsoon = (pygame.Rect((värav[0], värav[1] + 20, värav[2], värav[3] - 40))) #Tuleb arvestada mängija suurusega

        #Ristkülikud salvestatakse paaridena järjendisse. Paare on täpselt sama palju kui takistusi
        tsoonid[takistused.index(el)][0] = ohutsoon
        tsoonid[takistused.index(el)][1] = turvatsoon

    #Mängija ristküliku määramine. Siin lisatakse liikumise tulemus
    mängija = pygame.Rect(laius/5, pikkus/2 - kukkumiskiirus, 20, 20)
    pygame.draw.rect(ekraan, roheline, (mängija))

    #Paari kaupa (oht ja turvaline) kontrollitakse, kas mängija on nendega ühenduses
    for paar in tsoonid: 
        if mängija.colliderect(paar[0]) and not mängija.colliderect(paar[1]): #Kui mängija on ohus, aga pole väravas, siis ta kaotab
            pygame.draw.rect(ekraan, punane, (paar[0])) #Näidatakse kokkupõrke põhjustanud takistust
            pygame.draw.rect(ekraan, roheline, (mängija))
            pygame.display.flip()
            kaotus()

    if mängija[1] < 0 or mängija[1] > pikkus - 20: #Kui mängija on ekraanilt väljas, siis ta kaotab
        pygame.draw.rect(ekraan, punane, (mängija))
        pygame.display.flip()
        kaotus()

    #Sündmuste kontroll
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if sündmus.type == pygame.KEYDOWN:
            if sündmus.key == pygame.K_SPACE: #Klahvivajutus annab kohe energiat, et lubada kiiremaid manöövreid
                energia = 3
                kukkumiskiirus += energia
                kukkumine = False #Mängija enam ei kuku
                
    pygame.display.flip() #Värskendab ekraani
    FPS.tick(60) #60 kaadrit sekundis