import pygame as pg

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from Utilities.global_consts import COLOR_DRAW, COLOR_FILL
from Class.label_object import label_object

class graph_object():

    def __init__(self, bar_widht: int, x: int, y: int, separation: int, labelsep: int, labelpos: int, labelwidht: int, font_size: int, font, title: int, surface: pg.Surface) -> None:
        self.x = x
        self.y = y
        self.suface_acting = surface
        self.bar_widht = bar_widht
        self.separation = separation
        self.labelsep = labelsep
        self.font = font
        self.font_size = font_size
        self.labelpos = labelpos
        self.labelwidht = labelwidht
        self.title = title

    def set_bars(self,**params):
        self.bars = params

    def update(self):
        i = 0  

        label_title = label_object(
            surface=self.suface_acting,
            text= self.title,
            x=self.x,
            y=self.y + self.labelsep * 2 + 5,
            height=self.labelsep,
            widht=self.bar_widht,
            font=None,
            align='C',
            size=self.font_size
            )   

        label_title.update()

        sum = 0

        for j in self.bars.values():
            sum += j

        for key, value in self.bars.items():

            if sum != 0:porc = round((value*100)/sum,2)
            else: porc = 0

            pg.draw.rect(self.suface_acting, COLOR_DRAW, pg.Rect(self.x + (self.bar_widht + self.separation) * i, self.y-int(porc)*1.5, self.bar_widht, int(porc)*1.5))
            
            label_bars = label_object(
                surface=self.suface_acting,
                text=key,
                x=self.x - self.labelpos,
                y=self.y - self.labelsep*(i+1),
                height=self.labelsep,
                widht=self.labelwidht,
                font=None,
                align='R',
                size=self.font_size
            )

            label_inds = label_object(
                surface=self.suface_acting,
                text=key,
                x=self.x + (self.bar_widht + self.separation) * i,
                y=self.y + self.labelsep,
                height=self.labelsep,
                widht=self.bar_widht,
                font=None,
                align='C',
                size=self.font_size
            )

            label_bars.set_text(f'{i+1}-{key}={value} | {porc}%')
            label_bars.update()
            label_inds.set_text(f'{i+1}')
            label_inds.update()
            
            i += 1

