import pygame
import src.GUI.image_load as images
import src.GUI.draw_track as draw_track
import src.Game.Logic.computer as computer
import src.Game.Logic.player as player
import src.Game.Logic.finish as finish
import src.GUI.convert_object as convert
import src.Game.Logic.game_info as info
from src.settings import COMPUTER_PATH


class Menu:
    def __init__(self, window):
        self.window = window
        self.draw = draw_track.GameDrawer(window)
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.player_car = player.PlayerCar(4, 5, (200, 200), images.WHITE_CAR)
        self.computer_car = computer.ComputerCar(1.5, 4, (170, 200), images.GREY_CAR, COMPUTER_PATH)
        self.finish = finish.Finish(self.player_car, self.computer_car)
        self.game_info = info.GameInfo()

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.update_screen()

            while not self.game_info.started:
                convert.blit_text_center(self.window, images.MAIN_FONT,
                                         f"Press any key to start level {self.game_info.level}!")
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if event.type == pygame.KEYDOWN:
                        self.game_info.start_level()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pos = pygame.mouse.get_pos()
                #     self.computer_car.path.append(pos)
            self.player_car.action()
            self.computer_car.move()
            self.finish.handle_collision(self.window, self.game_info)

            if self.game_info.game_finished():
                self.finish.finish_game(self.window, self.game_info, "You win this game!")
        # print(self.computer_car.path)

    def update_screen(self):
        self.draw.draw_track(self.player_car, self.computer_car, self.game_info)
