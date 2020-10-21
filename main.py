import pygame, sys
import constants


# Add Title and Icon to window
pygame.display.set_caption("PDG Project")
icon = pygame.image.load('data/brick.png')
pygame.display.set_icon(icon)


#Structs
class struct_Tile:
    def __init__(self, block_path):
        self.block_path = block_path

#Objects
class obj_Actor:
    def __init__(self, x, y, sprite):
        self.x = x #map adress
        self.y = y #map adress
        self.sprite = sprite

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x*constants.CELL_WIDTH, self.y*constants.CELL_HEIGHT))

    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy

#Map with list comprehension
def map_create():
    new_map = [[ struct_Tile(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH) ]

    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

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
                SURFACE_MAIN.blit(constants.S_WALL, (x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT))
            
            else:
                #Draw floor
                SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT))



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

    PLAYER = obj_Actor(0, 0, constants.S_PLAYER)




#Main
if __name__ == "__main__":
    game_initialize()
    game_loop()