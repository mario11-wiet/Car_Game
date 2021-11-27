import pygame

from src.Game.Logic.car import Car
import src.GUI.image_load as images


class PlayerCar(Car):
    def __init__(self, max_velocity, rotation_velocity, start_position, image):
        super().__init__(max_velocity, rotation_velocity, start_position, image)

    def bounce(self):
        self.velocity = -self.velocity
        self.move()

    def action(self):
        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_a]:
            self.rotate(left=True)
        if keys[pygame.K_d]:
            self.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            self.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.move_backward()
        if not moved:
            self.reduce_speed()
        if self.collide(images.TRACK_BORDER_MASK) is not None:
            self.bounce()
