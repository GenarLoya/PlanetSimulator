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
    text='Genaro Loya Dour',
    x=(WIDHT/2)-150,
    y=100,
    height=40,
    widht=300,
    font=None,
    align='C',
    size=30
    )

label2 = label_object(
    surface=screen,
    text='20610188',
    x=(WIDHT/2)-150,
    y=150,
    height=40,
    widht=300,
    font=None,
    align='C',
    size=30
    )

label3 = label_object(
    surface=screen,
    text='Jose Raul Lopez Arzaga',
    x=(WIDHT/2)-150,
    y=200,
    height=40,
    widht=300,
    font=None,
    align='C',
    size=30
    )

label4 = label_object(
    surface=screen,
    text='20710276',
    x=(WIDHT/2)-150,
    y=250,
    height=45,
    widht=300,
    font=None,
    align='C',
    size=30
    )
    
def back():
    pass
    
back_button = button(
    surface=screen,
    text='Volver',
    x=WIDHT/2 - 75,
    y=350,
    height=40,
    widht=150,
    font=None,
    align='C',
    size=40
    ) 

def void():
    while True:
        ti.sleep(0.08)

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()


        back_button.on_click(back)

        screen.fill(COLOR_FILL)

        label1.update()
        label2.update()
        label3.update()
        label4.update()
        back_button.update()

        pg.display.flip()

void()