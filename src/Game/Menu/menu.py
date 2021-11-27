import pygame
import src.GUI.image_load as images
import src.GUI.draw_track as draw_track
import src.Game.Logic.car as car


class Menu:
    def __init__(self, window):
        self.window = window
        self.draw = draw_track.GameDrawer(window)
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.player_car = car.PlayerCar(5, 5, (180, 200), images.RED_CAR)

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player_car.action()

    def update_screen(self):
        self.draw.draw_track(self.player_car)
