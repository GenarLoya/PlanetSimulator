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

center1 = center_object(
    image='Montecarlo/Resources/Images/Stars/002.png', 
    x=300, 
    y=100,  
    surface=screen
)

planet1 = orbit_object(
    image='Montecarlo/Resources/Images/Planets/004.png', 
    x=0, 
    y=0, 
    surface=screen,
    follow=center1.rect,
    init_time= 45,
    dif_time= 0.18,
    radius_orbit=120
)

planet11 = orbit_object(
    image='Montecarlo/Resources/Images/Planets/005.png', 
    x=0, 
    y=0, 
    surface=screen,
    follow=center1.rect,
    init_time= 270,
    dif_time= 0.15,
    radius_orbit=170
)

center2 = center_object(
    image='Montecarlo/Resources/Images/Stars/001.png', 
    x=1000, 
    y=400,  
    surface=screen
)

planet2 = orbit_object(
    image='Montecarlo/Resources/Images/Planets/003.png', 
    x=0, 
    y=0, 
    surface=screen,
    follow=center2.rect,
    init_time= 120,
    dif_time= 0.08,
    radius_orbit=120
)

planet22 = orbit_object(
    image='Montecarlo/Resources/Images/Planets/005.png', 
    x=0, 
    y=0, 
    surface=screen,
    follow=center2.rect,
    init_time= 120,
    dif_time= 0.2,
    radius_orbit=180
)

center3 = center_object(
    image='Montecarlo/Resources/Images/Stars/002.png', 
    x=500, 
    y=500,  
    surface=screen
)

planet3 = orbit_object(
    image='Montecarlo/Resources/Images/Planets/006.png', 
    x=0, 
    y=0, 
    surface=screen,
    follow=center3.rect,
    init_time= 90,
    dif_time= 0.17,
    radius_orbit=120
)

planet33 = orbit_object(
    image='Montecarlo/Resources/Images/Planets/007.png', 
    x=0, 
    y=0, 
    surface=screen,
    follow=center3.rect,
    init_time= 90,
    dif_time= 0.2,
    radius_orbit=190
)

def start():
        pass
    
start_button = button(
    surface=screen,
    text='INICIAR',
    x=WIDHT/2 - 75,
    y=200,
    height=45,
    widht=150,
    font=None,
    align='C',
    size=40
    )

def credits():
    pass
    
credits_button = button(
    surface=screen,
    text='Creditos',
    x=WIDHT/2 - 75,
    y=260,
    height=45,
    widht=150,
    font=None,
    align='C',
    size=40
    )

def quit():
    pass
    
quit_button = button(
    surface=screen,
    text='Salir',
    x=WIDHT/2 - 75,
    y=320,
    height=50,
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


        credits_button.on_click(credits)
        start_button.on_click(start)
        quit_button.on_click(quit)
        planet1.orbit()
        planet2.orbit()
        planet3.orbit()
        planet11.orbit()
        planet22.orbit()
        planet33.orbit()

        screen.fill(COLOR_FILL)
        
        center1.update()
        center2.update()
        center3.update()
        planet1.update()
        planet2.update()
        planet3.update()
        planet11.update()
        planet22.update()
        planet33.update()

        credits_button.update()
        start_button.update()
        quit_button.update()

        pg.display.flip()

void()   
    