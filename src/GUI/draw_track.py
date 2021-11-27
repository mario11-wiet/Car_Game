import src.GUI.image_load as images
import src.GUI.convert_object as convert
import src.settings as settings
import pygame


class GameDrawer:
    def __init__(self, window):
        self.window = window
        self.images = [(images.GRASS, (0, 0)), (images.TRACK, (0, 0)), (images.FINISH, images.FINISH_POSITION),
                       (images.TRACK_BORDER, (0, 0))]

    def draw_track(self, car_player, car_computer, game_info):
        for img, position in self.images:
            self.window.blit(img, position)

        level_text = images.MAIN_FONT.render(
            f"Level {game_info.level}", 1, (255, 255, 255))
        self.window.blit(level_text, (8, settings.WINDOW_HEIGHT - level_text.get_height() - 90))

        time_text = images.MAIN_FONT.render(
            f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
        self.window.blit(time_text, (8, settings.WINDOW_HEIGHT - time_text.get_height() - 50))

        vel_text = images.MAIN_FONT.render(
            f"Vel: {round(car_player.velocity, 1)}px/s", 1, (255, 255, 255))
        self.window.blit(vel_text, (8, settings.WINDOW_HEIGHT - vel_text.get_height() - 10))

        self.draw_car(car_player)
        self.draw_car(car_computer)
        # self.draw_points(car_computer)
        pygame.display.update()

    def draw_car(self, car):
        convert.blit_rotate_centre(self.window, car.img, (car.x, car.y), car.angle)

    def draw_points(self, car_computer):
        for points in car_computer.path:
            pygame.draw.circle(self.window, (255, 0, 0), points, 5)
