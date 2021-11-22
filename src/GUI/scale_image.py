import pygame


def scale_image(img, factory):
    size = round(img.get_width() * factory), round(img.get_height() * factory)
    return pygame.transform.scale(img, size)
