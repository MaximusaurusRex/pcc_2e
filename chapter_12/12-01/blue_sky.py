import sys
import pygame


class BlueSky:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 1000))
        self.bg_color = (0, 128, 255)
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


bsky = BlueSky()
bsky.run_game()
