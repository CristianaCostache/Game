import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('graphics/level/coin.png').convert_alpha(), (size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.counter = 1
        self.time_update = 0

    def update(self, x_shift):
        self.rect.x += x_shift
        
        if pygame.time.get_ticks() - self.time_update >= 120:
            self.time_update = pygame.time.get_ticks()
            if self.counter < 5:
                mult = 1
            else:
                mult = -1
            self.rect.y += mult * 2
            self.counter = (self.counter + 1) % 10

        # if self.counter % 60 == 0:
        #     self.rect.y += 1
        #     # flipped_image = pygame.transform.flip(self.image, True, False)
        #     # self.image = flipped_image
        #     if self.counter == 60:
        #         self.counter = 1
        # self.counter += 1

