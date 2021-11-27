import src.GUI.image_load as images


class Finish:
    def __init__(self, player_car, computer_car):
        self.player_car = player_car
        self.computer_car = computer_car

    def handle_collision(self):
        computer_finish_point_collide = self.computer_car.collide(images.FINISH_MASK, *images.FINISH_POSITION)
        if computer_finish_point_collide is not None:
            self.player_car.reset()
            self.computer_car.reset()

        player_finish_point_collide = self.player_car.collide(images.FINISH_MASK, *images.FINISH_POSITION)
        if player_finish_point_collide is not None:
            if player_finish_point_collide[1] == 0:
                self.player_car.bounce()
            else:
                self.player_car.reset()
                self.computer_car.reset()
                print("finish")
