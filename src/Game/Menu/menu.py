import pygame
import src.GUI.image_load as images
import src.GUI.draw_track as draw_track
import src.Game.Logic.computer as computer
import src.Game.Logic.player as player
import src.Game.Logic.finish as finish
from src.settings import COMPUTER_PATH


class Menu:
    def __init__(self, window):
        self.window = window
        self.draw = draw_track.GameDrawer(window)
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.player_car = player.PlayerCar(5, 5, (200, 200), images.RED_CAR)
        self.computer_car = computer.ComputerCar(2, 2, (170, 200), images.GREEN_CAR, COMPUTER_PATH)
        self.finish = finish.Finish(self.player_car, self.computer_car)

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pos = pygame.mouse.get_pos()
                #     self.computer_car.path.append(pos)
            self.player_car.action()
            self.computer_car.move()
            self.finish.handle_collision()
        # print(self.computer_car.path)

    def update_screen(self):
        self.draw.draw_track(self.player_car, self.computer_car)
