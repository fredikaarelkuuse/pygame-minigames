# Mäng 2 – Pygame
# Autorid: Fredi Kaarel Kuuse, Mihkel Põldvere
import pygame
import sys
import random

pygame.init()

helekollane = (255, 255, 224) #Defineerin RGB koodiga hetkel kasutatavad värvused
roheline = (0, 255, 0)
punane = (255, 0, 0)
sinine = (0, 0, 255)

ekraan = pygame.display.set_mode((960, 540)) #Objektide suurus vastavalt ekraani suurusele pole veel lisatud, aga on plaanis
laius, pikkus = ekraan.get_size()
pygame.display.set_caption("Mäng 2")

FPS = pygame.time.Clock() #Määran funktsiooni, mis tagab mängukiiruse ühtluse

#Mängija liikumise sõnastik, kus olemas võtmed ja baasväärtused
mängija_liikumine = {'kukkumine': True, 'nihe': 0, 'kiirendus': 0, 'energia': 3} 

#Takistused on mitmekihilises hulgas, kus esimene pool on takistuse andmed ja teine pool nendes paikneva augu ehk värava andmed
#Plaan on teha takistused vähem seaduspäraseks
takistused = [[[laius, 0, 50, pikkus], [laius, random.uniform(pikkus*0.2, pikkus*0.8), 50, 100]],
              [[laius*0.5, 0, 50, pikkus], [laius*0.5, random.uniform(pikkus*0.2, pikkus*0.8), 50, 100]],
              [[laius*0.75, 0, 50, pikkus], [laius*0.75, random.uniform(pikkus*0.2, pikkus*0.8), 50, 100]],
              [[laius*1.25, 0, 50, pikkus], [laius*1.25, random.uniform(pikkus*0.2, pikkus*0.8), 50, 100]]]

#Tsoonid on paaris järjendid, kus üks on mängijale ohtlik ja teine tagab turvalisuse. Neid kirjutatakse pidevalt üle
tsoonid =[[0, 0], [0, 0], [0, 0], [0, 0]]

def takistuse_pos(t): #See funktsioon tegeleb takistuste liigutamisega
    if t[0] <= -50: #Kui takistus on täielikult ekraanilt lahkunud jõuab ta uuesti paremale (teeb ringe)
        t[0] = laius
    else:
        t[0] -= 2 #Takistuse x koordinaat väheneb ehk takistus läheneb mängijale
    return(t)

def värava_pos(v): #See funktsioon liigutab väravaid nagu takistusi. Lipu lisamisel saaks teoorias kasutada ka takistus_pos funktsiooni
    if v[0] <= -50:
        v[0] = laius
        v[1] = random.uniform(pikkus*0.2, pikkus*0.8) 
    else:
        v[0] -= 2
    return v

def mängija_pos(m): #See funktsioon muudab mängija liikumiseks vajalikke väärtusi muutes sõnastiku võtmete väärtusi
    if m['kukkumine']:
        m['kiirendus'] += 0.1
        m['nihe'] -= m['kiirendus']
    else:
        m['nihe'] += m['energia']
        m['energia'] -= 0.1 #Energia kahaneb ehk hoog on algul kiirem
        if m['energia'] <= 0:
            m['kukkumine'] = True
            m['kiirendus'] = 0
    return m
        
def kaotus(): #Kutsutakse välja kui mängija kaotab ja "jäätab" ekraani. Hiljem peaks olema võimalik näha skoori ja uuesti alustada
    while True:
        for sündmus in pygame.event.get():
            if sündmus.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        FPS.tick(60) #60 kaadrit sekundis
                
while True: #Põhitsükkel
    ekraan.fill(helekollane)

    #Käib läbi iga takistuse ja selle värava andmed
    for el in takistused:
        takistus = takistuse_pos(el[0])
        värav = värava_pos(el[1])
        
        pygame.draw.rect(ekraan, sinine, (takistus))
        pygame.draw.rect(ekraan, helekollane, (värav))

        #Määratakse muutujatele ristkülikud, et hiljem kontrollida, kas mängija neid puudutab
        ohutsoon = (pygame.Rect((takistus))) 
        turvatsoon = (pygame.Rect((värav[0], värav[1] + 20, värav[2], värav[3] - 40))) #Tuleb arvestada mängija suurusega

        #Ristkülikud salvestatakse paaridena järjendisse. Paare on täpselt sama palju kui takistusi ehk võetakse takistuse index
        tsoonid[takistused.index(el)][0] = ohutsoon
        tsoonid[takistused.index(el)][1] = turvatsoon

    mängija_liikumine = mängija_pos(mängija_liikumine) #Sõnastik mängija_liikumine võtmete väärtusi muudetakse funktsiooniga

    #Siin lisatakse mängija y koordinaadile eelnevast funktsioonist (mängija_pos) määratud nihe.
    mängija = pygame.Rect(laius/5, pikkus/2 - mängija_liikumine['nihe'], 20, 20) #Mängija ristküliku määramine.
    pygame.draw.rect(ekraan, roheline, (mängija))

    #Paari kaupa (oht ja turvaline) kontrollitakse, kas mängija on nendega ühenduses
    for paar in tsoonid: 
        if mängija.colliderect(paar[0]) and not mängija.colliderect(paar[1]): #Kui mängija on ohus, aga pole väravas, siis ta kaotab
            pygame.draw.rect(ekraan, punane, (paar[0])) #Näidatakse kokkupõrke põhjustanud takistust
            paar[1][1] -= 20 #Eemaldan mängija suurusega arvestamise, sest turvatsoon on tegelikult väiksem, kui visuaalselt paistab
            paar[1][3] += 40
            pygame.draw.rect(ekraan, helekollane, (paar[1])) #Kokkupõrke takistusse joonistatakse värav
            pygame.draw.rect(ekraan, roheline, (mängija)) #Mängija joonistakse kõige peale
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
            if sündmus.key == pygame.K_SPACE: 
                mängija_liikumine['energia'] = 3 #Klahvivajutus annab kohe energiat, et lubada kiiremaid manöövreid
                mängija_liikumine['nihe'] += mängija_liikumine['energia']
                mängija_liikumine['kukkumine'] = False #Mängija enam ei kuku
                
    pygame.display.flip() #Värskendab ekraani
    FPS.tick(60) #60 kaadrit sekundis