import src.GUI.image_load as image
import pygame


class GameDrawer:
    def __init__(self, window):
        self.windom = window
        self.images = [(image.GRASS, (0, 0)), (image.TRACK, (0, 0))]

    def draw(self):
        for img, position in self.images:
            self.windom.blit(img, position)
