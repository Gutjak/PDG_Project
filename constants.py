import pygame, random
pygame.init()


#Define a tile
TILE = 32

#Map variables
MAP_WIDTH = 31
MAP_HEIGHT = 31

#Game size
GAME_WIDTH = TILE*MAP_WIDTH
GAME_HEIGHT = TILE*MAP_HEIGHT


#Color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_GREEN = (4, 183, 16)
COLOR_OLIVE = (0, 64, 0)
COLOR_RED = (208, 18, 18)

#Game colors
COLOR_DEFAULT_BG = COLOR_OLIVE

#Game text
TEXT_DEFAULT = pygame.font.SysFont('Arial', 30)

#Sprites
S_PLAYER = pygame.image.load('data/man.png')
S_WALL = pygame.image.load('data/wall.png')
S_FLOOR = pygame.image.load('data/floor.jpeg')
S_DRAGON = pygame.image.load('data/dragon.png')
S_DOOR = pygame.image.load('data/door.png')
S_DOOR2 = pygame.image.load('data/door-2.png')
S_KEY = pygame.image.load('data/gold-key.png')
S_KNIGHT = pygame.image.load('data/knight.png')
S_OPENSIGN = pygame.image.load('data/open-sign.png')