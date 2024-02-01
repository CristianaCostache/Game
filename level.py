import pygame
from tiles import Tile
from settings import *
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                has_grass = True
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == "x":
                    try:
                        if level_map[row_index - 1][col_index] == "x":
                            has_grass = False
                    except:
                        pass
                    tile = Tile((x, y), tile_size, has_grass)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < left_limit and direction_x < 0:
            self.world_shift = speed
            player.speed = 0
        elif player_x > right_limit and direction_x > 0:
            self.world_shift = -speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = speed

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        if player.rect.y < 0:
            player.rect.y = 0
            player.direction.y = 0

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def game_over(self):
        return self.player.sprite.is_out_of_world()

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x() 

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
    