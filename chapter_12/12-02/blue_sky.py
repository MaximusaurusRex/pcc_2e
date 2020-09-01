import sys
import pygame
from game_character import Character


class BlueSky:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((500, 500))
        self.bg_color = (0, 128, 255)
        pygame.display.set_caption("Blue Sky")
        self.char = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.char.blitme()

            pygame.display.flip()


bsky = BlueSky()
bsky.run_game()
