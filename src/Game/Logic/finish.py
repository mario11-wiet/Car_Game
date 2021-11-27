import pygame.time
import src.GUI.image_load as images
import src.GUI.convert_object as convert


class Finish:
    def __init__(self, player_car, computer_car):
        self.player_car = player_car
        self.computer_car = computer_car

    def handle_collision(self, window, game_info):
        computer_finish_point_collide = self.computer_car.collide(images.FINISH_MASK, *images.FINISH_POSITION)
        if computer_finish_point_collide is not None:
            self.finish_game(window, game_info, "You lost!")

        player_finish_point_collide = self.player_car.collide(images.FINISH_MASK, *images.FINISH_POSITION)
        if player_finish_point_collide is not None:
            if player_finish_point_collide[1] == 0:
                self.player_car.bounce()
            else:
                game_info.next_level()
                self.player_car.reset()
                self.computer_car.next_level(game_info.level)

    def finish_game(self, window, game_info, text):
        convert.blit_text_center(window, images.MAIN_FONT, text)
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        self.player_car.reset()
        self.computer_car.reset()
