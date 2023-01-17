#Esto es para agregar la path principal del proyecto y poder incluir modulos en carpetas de jerarquia anterior

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

#########################################################

#from logging import basicConfig, info, INFO
#basicConfig(level=INFO, format='[%(levelname)] (%(threadname)-s) %(message)')

import pygame as pg
import math as mh
from random import random as rd, randrange as rr
from Utilities.global_consts import PLANETS_IN_SYSTEM, DISCOVERY_FACILITY, WIDHT, HEIGHT, SIZE
from Class.movement_object import movement_object as mov
from Class.orbit_object import orbit_object

class center_object(mov):
    planets_number = 0
    planets_list = []
    gen = False
    
    def __init__(self, image: str, x: int, y: int, surface: pg.Surface) -> None:
        super().__init__(image, x, y, surface)

    def update(self):
        super().update()
        self.update_followers()

    def generate_follower(self):
        rand = rd()
        self.gen = True

        for i in PLANETS_IN_SYSTEM:
            if rand >= i[1] and rand < i[2]:
                self.planets_number = i[0]
                break

        for i in range(int(self.planets_number)):
            rand2 = rr(1,8)
            
            follow_object = orbit_object(
                image=f'Resources/Images/Planets/00{rand2}.png', 
                x=0, 
                y=0, 
                surface=self.surface_acting,
                follow=self.rect,
                init_time= 45 * i,
                dif_time= (0.08*i) + (rd()/5),
                radius_orbit=int(120+(60*i))
                )

            self.planets_list.append(follow_object)

    def orbit_followers(self):
        if self.gen == True:
            for i in self.planets_list:
                i.orbit()
    
    def update_followers(self):
        if self.gen == True:
            for i in self.planets_list:
                i.update()
