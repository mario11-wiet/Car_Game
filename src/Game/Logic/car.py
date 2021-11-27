import math

import pygame
import src.GUI.image_load as images


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

        finish_point_collide = self.collide(images.FINISH_MASK, *images.FINISH_POSITION)
        if finish_point_collide is not None:
            if finish_point_collide[1] == 0:
                self.bounce()
            else:
                self.reset()
                print("finish")
