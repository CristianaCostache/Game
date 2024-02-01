import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
bg_image = pygame.transform.scale(pygame.image.load('graphics/level/background.png').convert_alpha(), (screen_width, screen_height))


while not level.game_over():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.blit(bg_image, (0, 0))
	level.run()

	pygame.display.update()
	clock.tick(60)