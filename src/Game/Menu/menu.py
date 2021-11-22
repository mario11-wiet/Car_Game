import pygame
import src.GUI.image_load as image
import src.GUI.draw_track as draw_track


class Menu:
    def __init__(self, window):
        self.window = window
        self.draw = draw_track.GameDrawer(window)
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.update_screen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update_screen(self):
        self.draw.draw()
