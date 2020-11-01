import pygame, random
pygame.init()


#Define a tile
TILE = 32

#Map variables
MAP_WIDTH = 31
MAP_HEIGHT = 25

#Game size
GAME_WIDTH = TILE*MAP_WIDTH
GAME_HEIGHT = TILE*MAP_HEIGHT

#Room
#MAX_ROOMS = 5
#ROOM_COORD_X_MIN = 0
#ROOM_COORD_X_MAX = GAME_WIDTH-5
#ROOM_COORD_Y_MIN = 0
#ROOM_COORD_Y_MAX = GAME_WIDTH-5
#ROOM_SIZE_X_MIN = 3
#ROOM_SIZE_X_MAX = 5
#ROOM_SIZE_Y_MIN = 3
#ROOM_SIZE_Y_MAX = 5
#ROOM_COORD_X = random.randint(0, GAME_WIDTH-6)
#ROOM_COORD_Y = random.randint(0, GAME_HEIGHT-6)
#ROOM_SIZE_X = random.randint(TILE*2, TILE*5)
#ROOM_SIZE_Y = random.randint(TILE*2, TILE*5)


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
S_DRAGON = pygame.image.load('data/dragon.png')
S_DOOR = pygame.image.load('data/door.png')
S_DOOR2 = pygame.image.load('data/door-2.png')
S_KEY = pygame.image.load('data/gold-key.png')
S_KNIGHT = pygame.image.load('data/knight.png')
S_OPENSIGN = pygame.image.load('data/open-sign.png')