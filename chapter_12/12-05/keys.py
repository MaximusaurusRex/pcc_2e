import sys
import pygame


class KeysGame:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Keys")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

    def _check_events(self):
        # Respond to keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_a:
            print(event.key)
        elif event.key == pygame.K_s:
            print(event.key)
        elif event.key == pygame.K_d:
            print(event.key)
        elif event.key == pygame.K_f:
            print(event.key)
        elif event.key == pygame.K_g:
            print(event.key)


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = KeysGame()
    ai.run_game()
