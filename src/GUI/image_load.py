import os
import pygame
from src.settings import ASSETS_FOLDER, WINDOW_WIDTH, WINDOW_HEIGHT
from src.GUI.scale_image import scale_image

GRASS = pygame.image.load(os.path.join(ASSETS_FOLDER, 'grass.jpg'))
GRASS = scale_image(GRASS, max(WINDOW_WIDTH / GRASS.get_width(), WINDOW_HEIGHT/GRASS.get_height()))
GREEN_CAR = scale_image(pygame.image.load(os.path.join(ASSETS_FOLDER, 'green-car.png')), 0.5)
GREY_CAR = scale_image(pygame.image.load(os.path.join(ASSETS_FOLDER, 'grey-car.png')),0.5)
PURPLE_CAR = scale_image(pygame.image.load(os.path.join(ASSETS_FOLDER, 'purple-car.png')), 0.5)
RED_CAR = scale_image(pygame.image.load(os.path.join(ASSETS_FOLDER, 'red-car.png')), 0.5)
WHITE_CAR = scale_image(pygame.image.load(os.path.join(ASSETS_FOLDER, 'white-car.png')), 0.5)
TRACK = pygame.image.load(os.path.join(ASSETS_FOLDER, 'track.png'))
TRACK_BORDER = pygame.image.load(os.path.join(ASSETS_FOLDER, 'track-border.png'))
FINISH = pygame.image.load(os.path.join(ASSETS_FOLDER, 'finish.png'))
