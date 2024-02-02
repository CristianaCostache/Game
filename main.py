import pygame, sys
from settings import *
from level import Level
from coin import Coin

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(LEVEL_MAP, screen)
bg_image = pygame.transform.scale(pygame.image.load('graphics/level/background.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_music = pygame.mixer.music.load("sounds/music.ogg")

pygame.mixer.music.play(-1)

while not level.game_over():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.blit(bg_image, (0, 0))
	level.run()
	level.game_over()

	pygame.display.update()
	clock.tick(60)

pygame.time.delay(3000)