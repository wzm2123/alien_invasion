# 作者：王子明
import pygame

class Picture():

    def __init__(self,back_picture,screen):
        self.screen = screen
        self.back_picture = back_picture
        self.image = pygame.image.load('images/picture.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left
        self.rect.right = self.screen_rect.right

    def blitme(self):
        self.screen.blit(self.image, self.rect)