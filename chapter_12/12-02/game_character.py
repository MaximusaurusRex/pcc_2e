import pygame


class Character:

    def __init__(self, bsky_main):
        self.screen = bsky_main.screen
        self.screen_rect = bsky_main.screen.get_rect()
        self.image = pygame.image.load('chapter_12/12-02/char.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
