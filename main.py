import pygame
import sys
import constants
import random


# Add Title and Icon to window
pygame.display.set_caption("PDG Project")
icon = pygame.image.load('data/brick.png')
pygame.display.set_icon(icon)


#Define parameters for tiles
class TILE:
    def __init__(self, block_path, visited):
        self.block_path = block_path
        self.visited = visited;

#Define upper left corner and size of room
class RECT:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

#Define and control Sprite
class OBJ_ACTOR:
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

def create_grid():
    
    pointer = []
    for x in range(1, constants.MAP_WIDTH, 2):
        for y in range(1, constants.MAP_HEIGHT, 2):
            new_map[x][y].block_path = False
            pointer.append((x, y))

    return pointer

def remove_wall(coords_from, coords_to):
        xa, ya = coords_from
        xb, yb = coords_to
        
        if xa == xb:
            new_map[xa][min(ya,yb)+1].block_path = False
        else:
            new_map[min(xa,xb)+1][ya].block_path = False

def carve_maze(coords):
    global new_map
   
    x,y = coords   
    
    #Given a current cell as a parameter
        #Coords set to (1,1) from the start

    #Mark the current cell as visited
    new_map[x][y].visited = True

    #Define neighbours
    neighbours = [cell for cell in [(x-2, y), 
                                    (x+2, y), 
                                    (x, y+2), 
                                    (x, y-2)] if cell[0] > 0 and cell[0] < constants.MAP_WIDTH-1 and cell[1] > 0 and cell[1] < constants.MAP_HEIGHT-1] #Don't go outside

     #neighbours = [cell for cell in [(x, y-2), #Look north
     #                                (x, y+2), #Look south
     #                                (x+2, y), #Look east
     #                                (x-2, y)] #Look west
     #                                if cell[0] > 0 and cell[0] < constants.GAME_WIDTH-1
     #                                and cell[1] > 0 and cell[1] < constants.GAME_HEIGHT-1] #Don't go outside
    random.shuffle(neighbours)

    #While the current cell has any unvisited neighbour cells
    for neighbour in neighbours:
        #Choose one of the unvisited neighbours
        if (new_map[neighbour[0]][neighbour[1]].visited == False):
            #Remove the wall between the current cell and the chosen cell
            remove_wall(coords, neighbour)
            #Invoke the routine recursively for a chosen cell
            carve_maze(neighbour)

def create_maze():
    pointer = create_grid()
    carve_maze((1,1))

#Map with rooms
def create_room(room):
    global new_map

    #Room carving. +1 makes sure there are walls surounding the room
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            new_map[x][y].block_path = False
            new_map[x][y].visited = True



def map_create():
    global new_map

    new_map = [[ tile(True, False) 
                for y in range(0, constants.MAP_HEIGHT)] 
               for x in range(0, constants.MAP_WIDTH)]

    create_maze()

    #room1 = rect(1, 2, 10, 10)
    #room2 = rect(10, 10, 10, 12)
    #create_room(room1)
    #create_room(room2)

    return new_map

def draw_game():
    global SURFACE_MAIN

    #Clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #draw the map
    draw_map(GAME_MAP)

    #draw the character
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

    PLAYER = obj_Actor(1, 1, constants.S_PLAYER)




#Main
if __name__ == "__main__":
    game_initialize()
    game_loop()