import pygame
pygame.init()


#Define a tile
TILE = 32

#Map variables
MAP_WIDTH = 30
MAP_HEIGHT = 24

#Game size
GAME_WIDTH = TILE*MAP_WIDTH
GAME_HEIGHT = TILE*MAP_HEIGHT

#Room



#Color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_OLIVE = (0, 64, 0)

#Game colors
COLOR_DEFAULT_BG = COLOR_OLIVE

#Sprites
S_PLAYER = pygame.image.load('data/man.png')
S_WALL = pygame.image.load('data/wall.png')
S_FLOOR = pygame.image.load('data/floor.jpeg')