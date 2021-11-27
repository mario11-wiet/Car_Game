import pygame


def scale_image(img, factory):
    size = round(img.get_width() * factory), round(img.get_height() * factory)
    return pygame.transform.scale(img, size)


def blit_rotate_centre(window, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    window.blit(rotated_image, new_rect.topleft)


def blit_text_center(window, font, text):
    render = font.render(text, 1, (200, 200, 200))
    window.blit(render, (window.get_width() / 2 - render.get_width() /
                         2, window.get_height() / 2 - render.get_height() / 2))
