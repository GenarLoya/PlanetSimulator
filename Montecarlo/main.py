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

if __name__ == '__main__':   

    screen = pg.display.set_mode(SIZE)
    clock=pg.time.Clock()
    
    class mode:
        mode = 3
        c = 0
        limitcel = 100
        charge = 0
        graph_counter = 0

    mod = mode
    #0 = menu
    #1 = creditos
    #2 = simulacion
    #3 = simulacion

    #MENU########################################################################################

    center1 = center_object(
        image= '/Resources/Images/Stars/002.png', 
        x=300, 
        y=100,  
        surface=screen
    )

    planet1 = orbit_object(
        image= '/Resources/Images/Planets/004.png', 
        x=0, 
        y=0, 
        surface=screen,
        follow=center1.rect,
        init_time= 45,
        dif_time= 0.18,
        radius_orbit=120
    )

    planet11 = orbit_object(
        image= '/Resources/Images/Planets/005.png', 
        x=0, 
        y=0, 
        surface=screen,
        follow=center1.rect,
        init_time= 270,
        dif_time= 0.15,
        radius_orbit=170
    )

    center2 = center_object(
        image= '/Resources/Images/Stars/001.png', 
        x=1000, 
        y=400,  
        surface=screen
    )

    planet2 = orbit_object(
        image= '/Resources/Images/Planets/003.png', 
        x=0, 
        y=0, 
        surface=screen,
        follow=center2.rect,
        init_time= 120,
        dif_time= 0.08,
        radius_orbit=120
    )

    planet22 = orbit_object(
        image= '/Resources/Images/Planets/005.png', 
        x=0, 
        y=0, 
        surface=screen,
        follow=center2.rect,
        init_time= 120,
        dif_time= 0.2,
        radius_orbit=180
    )

    center3 = center_object(
        image= '/Resources/Images/Stars/002.png', 
        x=500, 
        y=500,  
        surface=screen
    )

    planet3 = orbit_object(
        image= '/Resources/Images/Planets/006.png', 
        x=0, 
        y=0, 
        surface=screen,
        follow=center3.rect,
        init_time= 90,
        dif_time= 0.17,
        radius_orbit=120
    )

    planet33 = orbit_object(
        image= '/Resources/Images/Planets/007.png', 
        x=0, 
        y=0, 
        surface=screen,
        follow=center3.rect,
        init_time= 90,
        dif_time= 0.2,
        radius_orbit=190
    )

    def start():
        mod.mode = 2
        
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
        mod.mode = 1
        
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

    #Creditos####################################################################################

    labeln1 = label_object(
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

    labeln2 = label_object(
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

    labeln3 = label_object(
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

    labeln4 = label_object(
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
        mod.mode = 0
        
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

    #Simulacion##################################################################################
    
    center = center_object(
        image= '/Resources/Images/Stars/002.png', 
        x=900, 
        y=200,  
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
        if mod.limitcel >= 30:
            mod.limitcel -= 5
        else:
            mod.limitcel = 0

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
        if mod.limitcel <= 200:
            mod.limitcel += 5
        else:
            mod.limitcel = 200

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
        mod.mode = 0

    to_graph = button(
        surface=screen,
        text = 'Cambiar grafica',
        x=120,
        y=HEIGHT - 20,
        height=20,
        widht=50,
        font='Arial',
        size=12,
        align='C'
    )

    def other_graph():
        
        if mod.graph_counter == 2:
            mod.graph_counter  = 0
        else: mod.graph_counter += 1

    graph_discoverys = graph_object(
        bar_widht=10,
        x=400,
        y=550,
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
        x=400,
        y=550,
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
        x=400,
        y=550,
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
        for key in dic_moons.keys():
            if int(float(key)) == var:
                dic_moons[key] += 1
        
    observatory = pg.image.load(dir + '/Montecarlo/Resources/Images/observatory.png')
    observatory_rect = observatory.get_rect()
    observatory_rect.top = -50

    monitor = pg.image.load(dir + '/Montecarlo/Resources/Images/monitor.png')
    monitor_rect = observatory.get_rect()
    monitor_rect.top = 350
    monitor_rect.left = 0

#Carga#########################################################################################

    label1 = label_object(
        surface=screen,
        text='SYSTEM SIMULATOR',
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
        text='Cargando...',
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
        text='0%',
        x=(WIDHT/2)-50,
        y=400,
        height=40,
        widht=100,
        font=None,
        align='C',
        size=30
    )

#Bucle principal####################################################################################

    while True:

        clock.tick(10)

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if mod.mode == 0:
                    credits_button.on_click(credits)
                    start_button.on_click(start)
                    quit_button.on_click(quit)
                elif mod.mode == 1:
                    back_button.on_click(back)
                elif mod.mode == 2:
                    generate_new.on_click(gen)
                    to_menu.on_click(menu)
                    acel.on_click(facel)
                    deacel.on_click(fdeacel)
                    to_graph.on_click(other_graph)
                
        if mod.mode == 0:

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

        elif mod.mode == 1:
            
            planet1.orbit()
            planet2.orbit()
            planet3.orbit()
            planet11.orbit()
            planet22.orbit()
            planet33.orbit()
            
            screen.fill(COLOR_FILL)
            
            planet1.update()
            planet2.update()
            planet3.update()
            planet11.update()
            planet22.update()
            planet33.update()
            labeln1.update()
            labeln2.update()
            labeln3.update()
            labeln4.update()
            back_button.update()
        
        elif mod.mode == 2:

            center.orbit_followers()

            mod.c += 1

            if mod.c >= mod.limitcel:
                mod.c=0
                gen()

            
            get_discovery()
            graph_discoverys.set_bars(**dic_discoverys)
            graph_planets.set_bars(**dic_planets)
            graph_moons.set_bars(**dic_moons)

            screen.fill(COLOR_FILL)

            center.update()
            center.update_followers()
            screen.blit(observatory, observatory_rect)
            screen.blit(monitor, monitor_rect)
            generate_new.update()
            to_menu.update()
            speed.update()
            acel.update()
            deacel.update()
            to_graph.update()
            ind_discovery.update()
            update_discoverys()
            if mod.graph_counter == 0:graph_discoverys.update()
            elif mod.graph_counter == 1:graph_planets.update()
            elif mod.graph_counter == 2:graph_moons.update()

        elif mod.mode == 3:
            ti.sleep(0.1)
            
            screen.fill(COLOR_FILL)

            if mod.charge >= 100:
                pg.draw.rect(screen, COLOR_DRAW,pg.Rect((WIDHT/2)-250,300,500,50))
                label3.set_text(f'100%')
                ti.sleep(0.5)
                mod.mode = 0
            else:
                mod.charge += 5
                pg.draw.rect(screen, COLOR_DRAW,pg.Rect((WIDHT/2)-250,300,mod.charge*5,50))
                label3.set_text(f'{mod.charge}%')
            
            planet1.update()
            planet2.update()
            planet3.update()
            planet11.update()
            planet22.update()
            planet33.update()
            label1.update()
            label2.update()
            label3.update()

        pg.display.flip() 

          
        
