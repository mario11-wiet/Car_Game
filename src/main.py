import pygame
import settings
from Game.Menu.menu import Menu

def main():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    pygame.display.set_caption('CAR GAME')
    menu = Menu(window)
    menu.start()
    pygame.quit()


if __name__ == '__main__':
    main()

