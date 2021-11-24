import math

import pygame
import src.GUI.image_load as images


class Car:
    def __init__(self, max_velocity, rotation_velocity, start_position, image):
        self.x, self.y = start_position
        self.img = image
        self.velocity = 0
        self.angle = 0
        self.max_velocity = max_velocity
        self.rotation_velocity = rotation_velocity
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_velocity
        elif right:
            self.angle -= self.rotation_velocity

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration, self.max_velocity)
        self.move()

    def reduce_speed(self):
        self.velocity = max(self.velocity - self.acceleration / 2, 0)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity

        self.y -= vertical
        self.x -= horizontal


class PlayerCar(Car):
    def __init__(self,max_velocity, rotation_velocity, start_position, image):
        super().__init__(max_velocity, rotation_velocity, start_position, image)

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
        if not moved:
            self.reduce_speed()
