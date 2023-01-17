import pygame as pg
pg.init()
import time as ti
from random import randrange as rdr

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from Utilities.global_consts import COLOR_DRAW, SIZE, HEIGHT, WIDHT, COLOR_FILL, DISCOVERY_FACILITY, PLANETS_IN_SYSTEM, MOONS_IN_PLANET
from Class.center_object import center_object
from Class.button_object import button_object as button
from Class.orbit_object import orbit_object
from Class.label_object import label_object
from Class.graph_object import graph_object

screen = pg.display.set_mode(SIZE)

center = center_object(
    image='Montecarlo/Resources/Images/Stars/002.png', 
    x=WIDHT/2, 
    y=HEIGHT/2,  
    surface=screen
)

center.generate_follower()

def generate_moons(): 
        for i in center.planets_list:
            i.generate_follower()

generate_moons()

def gen():
    check_bars_planets(center.planets_number)

    for i in center.planets_list:
        i.rect.top = -1000
        i.rect.left = -1000
        check_bars_discovery(i.discovery)
        check_bars_moons(i.moons_number)
        del i

    center.planets_list.clear()
    
    center.generate_follower()
    
    for i in center.planets_list:
        i.generate_follower()

discovery_list = []

ind_discovery = label_object(
    surface=screen,
    text=f'Observatorio que descubre el planeta:',
    x=10,
    y=35,
    height=20,
    widht=150,
    font='Arial',
    size=12,
    align='L'
    )

def update_discoverys():
    for i in discovery_list:
        i.update()

def get_discovery():
    j = 0

    for i in discovery_list:
            i.rect.top = -1000
            i.rect.left = -1000
            i.x = -1000
            i.x = -1000
            i.text_image_rect.top = -1000
            i.text_image_rect.left = -1000
            del i

    discovery_list.clear()

    for i in center.planets_list:
        disc = i.discovery

        discovery = label_object(
            surface=screen,
            text=f'Planeta-{j}: {disc}',
            x=10,
            y=(25 * j) + 70,
            height=20,
            widht=150,
            font='Arial',
            size=12,
            align='L'
        )

        discovery_list.append(discovery)

        j += 1

generate_new = button(
    surface=screen,
    text='Generar Nuevo',
    x=10,
    y=10,
    height=20,
    widht=50,
    font='Arial',
    size=12,
    align='L'
)

acel = button(
    surface=screen,
    text='>',
    x=426,
    y=10,
    height=20,
    widht=50,
    font='Arial',
    size=12,
    align='L'
)

def facel():
    if limitcel >= 30:
        limitcel -= 5
    else:
        limitcel = 0

speed = label_object(
    surface=screen,
    text='Velocidad del tiempo',
    x=280,
    y=10,
    height=20,
    widht=50,
    font=None,
    align='C',
    size=20
)

deacel = button(
    surface=screen,
    text='<',
    x=260,
    y=10,
    height=20,
    widht=50,
    font='Arial',
    size=12,
    align='L'
)

def fdeacel():
    if limitcel <= 200:
        limitcel += 5
    else:
        limitcel = 200

to_menu = button(
    surface=screen,
    text='Ir al menu principal',
    x=120,
    y=10,
    height=20,
    widht=50,
    font='Arial',
    size=12,
    align='L'
)

def menu():
    pass

graph_discoverys = graph_object(
    bar_widht=10,
    x=320,
    y=600,
    separation=5,
    labelsep=22,
    labelpos=60,
    labelwidht=50,
    font_size=20,
    font=None,
    title='Observatorios',
    surface=screen
)

graph_planets = graph_object(
    bar_widht=10,
    x=640,
    y=600,
    separation=5,
    labelsep=22,
    labelpos=60,
    labelwidht=50,
    font_size=20,
    font=None,
    title='Planetas',
    surface=screen
)

graph_moons = graph_object(
    bar_widht=10,
    x=900,
    y=600,
    separation=5,
    labelsep=22,
    labelpos=60,
    labelwidht=50,
    font_size=20,
    font=None,
    title='Lunas',
    surface=screen
)

dic_discoverys = {}
dic_planets = {}
dic_moons = {}

def get_bars():
    for i in range(5):
        dic = {DISCOVERY_FACILITY[i][0]: 0}
        dic_discoverys.update(dic)

    for i in PLANETS_IN_SYSTEM:
        dic = {str(i[0]): 0}
        dic_planets.update(dic)

    for i in MOONS_IN_PLANET:
        dic = {str(i[0]): 0}
        dic_moons.update(dic)

get_bars()

def check_bars_discovery(var):
    for key in dic_discoverys.keys():
        try:
            if key == var:
                dic_discoverys[key] += 1
        except:
            pass

def check_bars_planets(var):
    for key in dic_planets.keys():
        if int(float(key)) == var:
            dic_planets[key] += 1

def check_bars_moons(var):
    for key in dic_planets.keys():
        if int(float(key)) == var:
            dic_moons[key] += 1
   
observatory = pg.image.load('Montecarlo/Resources/Images/observatory.png')
observatory_rect = observatory.get_rect()
observatory_rect.top = -50


while True:
    center.orbit_followers()
    generate_new.on_click(gen)

    c += 1

    if c >= 100:
        c=0
        gen()

    to_menu.on_click(menu)
    acel.on_click(facel)
    deacel.on_click(fdeacel)
    get_discovery()
    graph_discoverys.set_bars(**dic_discoverys)
    graph_planets.set_bars(**dic_planets)
    graph_moons.set_bars(**dic_moons)

    screen.fill(COLOR_FILL)

    center.update()
    center.update_followers()
    screen.blit(observatory, observatory_rect)
    generate_new.update()
    to_menu.update()
    speed.update()
    acel.update()
    deacel.update()
    ind_discovery.update()
    update_discoverys()
    graph_discoverys.update()
    graph_planets.update()

    pg.display.flip()