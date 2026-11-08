import pygame
import sys
pygame.init()

valge = (255, 255, 255)
tumesinine = (0, 0, 139)
roheline = (0, 255, 0)
punane = (255, 0, 0)
sinine = (0, 0, 255)
hall = (128, 128, 128)

ekraan = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
pygame.display.set_caption("Peamenüü")

def mänguvalik(): #siit järgmisele lehele
    print("Hello world!")
    pygame.display.set_caption("Vali mäng!") 
    while True:
        for juhtum in pygame.event.get():
            if juhtum.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ekraan.fill(valge)
        pygame.display.update()

def valikud(): #valikud siia
    pygame.display.set_caption("Sätted")
    while True:
        for juhtum in pygame.event.get():
            if juhtum.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ekraan.fill(hall)
        pygame.display.update()

def peamenüü():
    while True:
        ekraan.fill(tumesinine)
        hiire_pos = pygame.mouse.get_pos()
        laius, pikkus = ekraan.get_size()

        #fondi suurus ei tööta veel dünaamiliselt
        font = pygame.font.SysFont("Calibri", 80)

        nupu_laius = laius * 0.4
        nupu_pikkus = pikkus * 0.2
        nupu_x = laius / 2 - nupu_laius / 2
        nupu_y = pikkus / 3 / 2 - nupu_pikkus / 2

        mängi_nupp = pygame.Rect(nupu_x, nupu_y, nupu_laius, nupu_pikkus)
        valikud_nupp = pygame.Rect(nupu_x, nupu_y + pikkus / 3, nupu_laius, nupu_pikkus)
        välju_nupp = pygame.Rect(nupu_x, nupu_y + pikkus / 3 * 2, nupu_laius, nupu_pikkus)

        pygame.draw.rect(ekraan, roheline if mängi_nupp.collidepoint(hiire_pos) else hall, mängi_nupp)
        pygame.draw.rect(ekraan, sinine if valikud_nupp.collidepoint(hiire_pos) else hall, valikud_nupp)
        pygame.draw.rect(ekraan, punane if välju_nupp.collidepoint(hiire_pos) else hall, välju_nupp)

        mängi_tekst = font.render("Mängi", True, valge)
        valikud_tekst = font.render("Valikud", True, valge)
        välju_tekst = font.render("Välju", True, valge)

        mängi_kesk = mängi_tekst.get_rect(center = (laius / 2, pikkus / 3 / 2))
        valikud_kesk = valikud_tekst.get_rect(center = (laius / 2, pikkus / 3 / 2 * 3)) 
        välju_kesk = välju_tekst.get_rect(center = (laius / 2, pikkus / 3 / 2 * 5))

        ekraan.blit(mängi_tekst, mängi_kesk)
        ekraan.blit(valikud_tekst, valikud_kesk)
        ekraan.blit(välju_tekst, välju_kesk)

        for juhtum in pygame.event.get():
            if juhtum.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # see tuvastab praegu igat vajutust (M2 ja scroll wheel ka)
            if juhtum.type == pygame.MOUSEBUTTONDOWN:
                if mängi_nupp.collidepoint(hiire_pos):
                    mänguvalik()
                if valikud_nupp.collidepoint(hiire_pos):
                    valikud()
                if välju_nupp.collidepoint(hiire_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

peamenüü()