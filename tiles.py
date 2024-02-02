import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, has_grass = False):
        super().__init__()
        if has_grass:
            img_path = 'graphics/level/tile_grass.png'
        else:
            img_path = 'graphics/level/tile.png'
        self.image = pygame.transform.scale(pygame.image.load(img_path).convert_alpha(), (size, size))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift