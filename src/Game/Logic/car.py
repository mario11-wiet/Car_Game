import math

import pygame


class Car:
    def __init__(self, max_velocity, rotation_velocity, start_position, image):
        self.start_position = start_position
        self.x, self.y = self.start_position
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

    def move_backward(self):
        self.velocity = max(self.velocity - self.acceleration, -self.max_velocity / 2.0)
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

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        point = mask.overlap(car_mask, offset)
        return point

    def reset(self):
        self.x, self.y = self.start_position
        self.angle = 0
        self.velocity = 0


