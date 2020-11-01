import pygame, sys, random
import constants


# Add Title and Icon to window
pygame.display.set_caption("PDG Project")
icon = pygame.image.load('data/brick.png')
pygame.display.set_icon(icon)


#Define parameters for tiles
class tile:
    def __init__(self, block_path):
        self.block_path = block_path

#Define upper left corner and size of room
class rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h


#Define and control Sprite
class obj_Actor:
    def __init__(self, x, y, sprite):
        self.x = x #map adress
        self.y = y #map adress
        self.sprite = sprite

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x*constants.TILE, self.y*constants.TILE))

    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy

#Map with rooms
def create_room(room):
    global new_map

    #Room carving. +1 makes sure there are walls surounding the room
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            new_map[x][y].block_path = False

def place_room():
    pass

def map_create():
    global new_map

    new_map = [[ tile(True) 
                for y in range(0, constants.MAP_HEIGHT)] 
               for x in range(0, constants.MAP_WIDTH) ]

    room1 = rect(0, 0, 14, 16)
    room2 = rect(10, 10, 10, 12)
    create_room(room1)
    create_room(room2)

    return new_map

def draw_game():
    global SURFACE_MAIN

    #Clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #draw the map
    draw_map(GAME_MAP)

    # draw the character
    PLAYER.draw()

    #Update the display
    pygame.display.flip()

def draw_map(map_to_draw):
    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                #Draw wall
                SURFACE_MAIN.blit(constants.S_WALL, (x*constants.TILE, y*constants.TILE))
            
            else:
                #Draw floor
                SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.TILE, y*constants.TILE))



def game_loop():
    
    #Game Loop
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #check keystrokes to move player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    PLAYER.move(-1, 0)
                    print("left")
                if event.key == pygame.K_RIGHT:
                    PLAYER.move(1, 0)
                    print("right")
                if event.key == pygame.K_UP:
                    PLAYER.move(0, -1)
                    print("up")
                if event.key == pygame.K_DOWN:
                    PLAYER.move(0, 1)
                    print("down")  
    
        draw_game()

        pygame.display.update()



def game_initialize():

    global SURFACE_MAIN, GAME_MAP, PLAYER

    #Initialize the pygame
    pygame.init()

    #Create the screen
    SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )

    GAME_MAP = map_create()

    PLAYER = obj_Actor(3, 4, constants.S_PLAYER)




#Main
if __name__ == "__main__":
    game_initialize()
    game_loop()