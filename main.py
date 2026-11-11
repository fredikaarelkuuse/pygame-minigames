import pygame
from Peamenüü import peamenüü
from gameselector import GameSelector

pygame.init()

state = 0
while state != -1:
    if state == 0:
        if peamenüü() != None:
            state = peamenüü()
    elif state == 1:
        if GameSelector() != None:
            state = GameSelector()
pygame.quit()