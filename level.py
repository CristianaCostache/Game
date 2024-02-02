import pygame
from tiles import Tile
from settings import *
from player import Player
from coin import Coin

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.font_end = pygame.font.Font(None, 150)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coins = pygame.sprite.Group()

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
                
                if cell == 'B':
                    coin = Coin((x, y), coin_size)
                    self.coins.add(coin)

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

        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                self.score += 1
                sprite.kill()
    
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
        if (len(self.coins) == 0):
            self.print_final_message()
            return True

        return self.player.sprite.is_out_of_world()

    def update_score(self):
        score = self.score
        score_text = self.font.render(f'Score {score}', True, (255, 255, 255))
        self.display_surface.blit(score_text, (30, 30))

        coin_score_sprite = pygame.sprite.GroupSingle()
        coin_score_sprite.add(Coin((140, 25), 32))
        coin_score_sprite.draw(self.display_surface)

    def print_final_message(self):
        final_message = self.font_end.render(f'You win', True, (255, 255, 255))
        final_message_rect = final_message.get_rect(center=(screen_width / 2, screen_height / 2))
        self.display_surface.blit(final_message, final_message_rect)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.scroll_x() 

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        self.update_score()
    