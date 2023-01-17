import pygame as pg
pg.init()
import time as ti
import math as mh

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from Utilities.global_consts import COLOR_DRAW
from Class.movement_object import movement_object as movement
from Utilities.global_consts import MOONS_IN_PLANET, DISCOVERY_FACILITY
from random import random as rd, randrange as rr

class orbit_object(movement):
    follow = pg.Rect
    radius_orbit = 0
    time = 0
    dif_time = 0
    moons_number = 0
    moons_list = []
    gen = False
    discovery = ''

    def __init__(self, image: str, x: int, y: int, surface: pg.Surface, follow: pg.Rect, init_time: int, dif_time: float, radius_orbit: int) -> None:
        super().__init__(image, x, y, surface)
        self.follow = follow
        self.radius_orbit = radius_orbit
        self.time = init_time
        self.dif_time = dif_time

        rand = rd()

        for i in DISCOVERY_FACILITY:
            if rand >= i[1] and rand < i[2]:
                self.discovery = i[0]
                break

    def update(self):
        pg.draw.circle(self.surface_acting, COLOR_DRAW,self.follow.center,self.radius_orbit, 1)
        super().update()
        self.update_followers()

    def orbit(self):
        if self.follow != None:
            self.time += self.dif_time

            self.rect.centerx = (self.radius_orbit * mh.cos(self.time)) + self.follow.centerx
            self.rect.centery = (self.radius_orbit * mh.sin(self.time)) + self.follow.centery
            self.orbit_followers()

    def generate_follower(self):
        rand = rd()
        self.gen = True

        for i in MOONS_IN_PLANET:
            if rand >= i[1] and rand < i[2]:
                self.moons_number = i[0]
                break

        for i in range(int(self.moons_number)):
            rand2 = rr(1,4)
            
            follow_object = orbit_object(
                image=f'Resources/Images/Planets/00{rand2}.png', 
                x=0, 
                y=0, 
                surface=self.surface_acting,
                follow=self.rect,
                init_time= 45 * i,
                dif_time= (0.05*i) + (rd()/5),
                radius_orbit=int(30+(10*i))
                )

            self.moons_list.append(follow_object)

    def orbit_followers(self):
        if self.gen == True:
            for i in self.moons_list:
                i.orbit()
    
    def update_followers(self):
        if self.gen == True:
            for i in self.moons_list:
                i.update()