import pygame
from boss_menu import Bossmenu


class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.boss_menu = Bossmenu()

    def launch(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

    def draw(self):
        self.boss_menu.draw_blocks(self.screen)
        pygame.display.flip()


main = Main()
main.launch()
