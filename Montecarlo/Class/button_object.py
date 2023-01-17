import pygame as pg

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from Utilities.global_consts import COLOR_DRAW, COLOR_FILL
from Class.label_object import label_object as label

class button_object(label):

    def on_click(self, funct):
        mouse_pos = pg.mouse.get_pos()
                
        if self.rect.collidepoint(mouse_pos):
            funct()