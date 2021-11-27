import math

import pygame

from src.Game.Logic.car import Car


class ComputerCar(Car):
    def __init__(self, max_velocity, rotation_velocity, start_position, image, path=[]):
        super().__init__(max_velocity, rotation_velocity, start_position, image)
        self.path = path
        self.current_point = 0
        self.velocity = max_velocity

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_velocity, abs(difference_in_angle))

        else:
            self.angle += min(self.rotation_velocity, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def reset(self):
        self.x, self.y = self.start_position
        self.current_point = 0
        self.angle = 0
        self.velocity = self.max_velocity
