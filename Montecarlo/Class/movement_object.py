#Esto es para agregar la path principal del proyecto y poder incluir modulos en carpetas de jerarquia anterior

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

#########################################################

#from logging import basicConfig, info, INFO
#basicConfig(level=INFO, format='[%(levelname)] (%(threadname)-s) %(message)')

from threading import Thread
import pygame as pg
pg.init()
import math as mh
import time as ti
from random import random as rd

class movement_object:
    object = pg.image.load(dir + '/Resources/Images/Planets/001.png')
    rect = object.get_rect()
    surface_acting = pg.Surface
    move_phase = 0

    def __init__(self, image: str, x: int, y: int, surface: pg.Surface) -> None:
        self.object = pg.image.load(dir + '/' + image)
        self.rect = self.object.get_rect()
        
        self.rect.right = x
        self.rect.top = y

        self.surface_acting = surface

    def update(self):
        self.surface_acting.blit(self.object, self.rect)

    def move_on_path(self, *vec: dict) -> None:
        
        if self.move_phase <= len(vec)-1:
            path = vec[self.move_phase]

            if path[2] == 0:
                if path[3] >= self.rect.top:
                    self.rect.top += path[1]
                    if path[3] <= self.rect.top:
                        self.move_phase += 1
                elif path[3] <= self.rect.top:
                    self.rect.top -= path[1]
                    if path[3] >= self.rect.top:
                        self.move_phase += 1

            if path[3] == 0:
                if path[2] >= self.rect.right:
                    self.rect.right += path[0]
                    if path[2] <= self.rect.right:
                        self.move_phase += 1
                elif path[2] <= self.rect.right:
                    self.rect.right -= path[0]
                    if path[2] >= self.rect.right:
                        self.move_phase += 1


#   size = width, height = 320, 240
# speed = [1, 1]
# black = 0, 0, 0

# screen = pg.display.set_mode(size)

# new_client = movement_object(
#     image='Montecarlo/Resources/Images/000.gif', 
#     x=100, 
#     y=150, 
#     surface=screen)

# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT: sys.exit()
    
#     ti.sleep(0.25)
#     new_client.move_on_path((5,0,130,0), (0,5,0,50), (5,0,100,0), (0,5,0,150))
#     #th = Thread(target=new_client.move_on_path, args=((1,0,6), (1,3,5)))

#     #screen.fill(black)
#     screen.blit(new_client.object, new_client.rect)
#     pg.display.flip()      