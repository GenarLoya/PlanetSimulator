import pygame as pg
pg.init()
import time as ti
from random import randrange as rdr

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from Utilities.global_consts import COLOR_DRAW, SIZE, HEIGHT, WIDHT, COLOR_FILL
from Class.center_object import center_object
from Class.button_object import button_object as button
from Class.orbit_object import orbit_object
from Class.label_object import label_object
from Class.graph_object import graph_object

screen = pg.display.set_mode(SIZE)

label1 = label_object(
    surface=screen,
    text='SYSTEM SIMULATOR',
    x=(WIDHT/2)-150,
    y=100,
    height=40,
    widht=300,
    font=None,
    size=30
    )

label2 = label_object(
    surface=screen,
    text='Cargando...',
    x=(WIDHT/2)-150,
    y=150,
    height=40,
    widht=300,
    font=None,
    size=30
    )

label3 = label_object(
    surface=screen,
    text='0%',
    x=(WIDHT/2)-50,
    y=400,
    height=40,
    widht=100,
    font=None,
    size=30
    )

def void():
    i = 0

    while True:
        ti.sleep(0.1)

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

        label3.set_text(f'{i}%')
        
        screen.fill(COLOR_FILL)

        if i >= 100:
            pg.draw.rect(screen, COLOR_DRAW,pg.Rect((WIDHT/2)-250,300,500,50))
        else:
            i += 5
            pg.draw.rect(screen, COLOR_DRAW,pg.Rect((WIDHT/2)-250,300,i*5,50))
            label3.set_text(f'{i}%')
        
        
        label1.update()
        label2.update()
        label3.update()

        pg.display.flip()

void()