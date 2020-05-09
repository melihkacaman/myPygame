import pygame
BLACK = (0,0,0)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)


        pygame.draw.rect(self.image,color,[0,0,width,height])

        self.rect = self.image.get_rect()

    def moveUp(self, pixel):
        self.rect.y  = self.rect.y - pixel

        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixel):
        self.rect.y = self.rect.y + pixel

        if self.rect.y > 400:
            self.rect.y = 400
