import src.GUI.image_load as image
import src.GUI.convert_image as convert
import pygame


class GameDrawer:
    def __init__(self, window):
        self.window = window
        self.images = [(image.GRASS, (0, 0)), (image.TRACK, (0, 0)), (image.FINISH, image.FINISH_POSITION),
                       (image.TRACK_BORDER, (0, 0))]

    def draw_track(self, car):
        for img, position in self.images:
            self.window.blit(img, position)

        self.draw_car(car)
        pygame.display.update()

    def draw_car(self, car):
        convert.blit_rotate_centre(self.window, car.img, (car.x, car.y), car.angle)
