import pygame as pg

import sys
from os.path import dirname, abspath

dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from Utilities.global_consts import COLOR_DRAW, COLOR_FILL

class label_object:
    surface_acting = pg.Surface
    size = widht, height = 0,0
    color = COLOR_DRAW
    font = pg.font.Font
    rect = pg.Rect
    text_image = pg.font.Font
    text_image_rect = pg.Rect
    text = ''

    def __init__(self, surface: pg.Surface, text: str, x: int, y: int, height: int, widht: int, font, size: int, align: str) -> None:
        self.surface_acting = surface
        self.widht, self.height = height, widht
        self.font = pg.font.SysFont(font, size)
        self.align = align
        self.x = x
        self.y = y

        self.rect = pg.Rect(x, y, widht, height)
        
        self.text = text
        self.read_text(text)

    def read_text(self, text: str):
        if self.align == 'C':
            self.text_image = self.font.render(str(text), False, COLOR_FILL, None)
            self.text_image_rect = self.text_image.get_rect()
            self.rect.width = self.text_image.get_width() + 10
            self.text_image_rect.center = self.rect.center
        elif self.align == 'L':
            self.text_image = self.font.render(str(text), False, (0,0,100), None)
            self.text_image_rect = self.text_image.get_rect()
            self.text_image_rect.right = self.x + self.text_image.get_width() + 5
            self.text_image_rect.top = self.y + 5
        elif self.align == 'R':
            self.text_image = self.font.render(str(text), False, (0,0,100), None)
            self.text_image_rect = self.text_image.get_rect()
            self.text_image_rect.left = self.x - self.text_image.get_width() + self.widht - 5
            self.text_image_rect.top = self.y + 5

    def set_text(self, text: str):
        self.text = text
        self.read_text(text)

    def update(self):
        if self.align == 'L': 
            self.rect.width = self.text_image.get_width() + 10

        if self.align == 'R': 
            self.rect.width = self.text_image.get_width() + 10
            self.rect.right = self.x + 20

        self.surface_acting.fill(COLOR_DRAW, self.rect)
        self.surface_acting.blit(self.text_image, self.text_image_rect)
        