import pygame
import sys
import constants
import random


# Add Title and Icon to window
pygame.display.set_caption("PDG Project")
icon = pygame.image.load('data/maze.png')
pygame.display.set_icon(icon)


#Define parameters for tiles
class Tile:
    def __init__(self, block_path, visited):
        self.block_path = block_path
        self.visited = visited;

#Define upper left corner and size of room
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

#Define and control Sprite
class Obj_Actor:
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
        new_map[xa][min(ya,yb)+1].visited = True
    else:
        new_map[min(xa,xb)+1][ya].block_path = False
        new_map[min(xa,xb)+1][ya].visited = True

    """
    Takes coordinates from the nodes it stands on and unvisited node it wants to go to.
    First it compares x direction from both nodes if equal. If False, y direction must be equal.
    wichever direction is equal, carve the tile in the other direction between the two nodes.
    Ex from 1,3 to 3,3. y is equal. Must carve in x direction. Chose the smallest of 1 and 3. Add 1 to result. Carve 2,3 
    """

def carve_maze(coords):
    global new_map
   
    x,y = coords   
    
    #Recursive depth-first search
    #Given a current node as a parameter
        #Coords set to (1,1) from the start

    #Mark the current node as visited
    new_map[x][y].visited = True

    #Define neighbours
    neighbours = [node for node in [(x-2, y), 
                                    (x+2, y), 
                                    (x, y+2), 
                                    (x, y-2)] if node[0] > 0 and node[0] < constants.MAP_WIDTH-1 
                                    and node[1] > 0 and node[1] < constants.MAP_HEIGHT-1] #Don't go outside

    print(f"node: {coords} Neighbours: {neighbours}") #Show the work
    random.shuffle(neighbours)

    #While the current node has any unvisited neighbour nodes
    for neighbour in neighbours:
        #Choose one of the unvisited neighbours
        if (new_map[neighbour[0]][neighbour[1]].visited == False):
            #Remove the wall between the current node and the chosen node
            remove_wall(coords, neighbour)
            #Invoke the routine recursively for a chosen node
            carve_maze(neighbour)

def create_maze():
    pointer = create_grid()
    carve_maze((1,1))
    shortcuts()

def shortcuts():
    global new_map
    #Number of shortcuts is modular compared to the width of board
    max_shortcuts = int(constants.MAP_WIDTH // 3)

    s = 0
    while s < max_shortcuts:
        x = random.randrange(2, constants.MAP_WIDTH-1, 2)
        y = random.randrange(2, constants.MAP_HEIGHT-1, 2)
        if new_map[x][y].visited == False:
            nb = [node for node in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]]
            #check it is on a line. Not in a corner or end piece.
            if ((new_map[nb[0][0]][nb[0][1]].visited == False and new_map[nb[1][0]][nb[1][1]].visited == False \
                and new_map[nb[2][0]][nb[2][1]].visited == True and new_map[nb[3][0]][nb[3][1]].visited == True) \
                or (new_map[nb[0][0]][nb[0][1]].visited == True and new_map[nb[1][0]][nb[1][1]].visited == True \
                and new_map[nb[2][0]][nb[2][1]].visited == False and new_map[nb[3][0]][nb[3][1]].visited == False)):
                new_map[x][y].block_path = False
                new_map[x][y].visited = True
                print(f"Shortcut at {x},{y}")
                s += 1            

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

    new_map = [[ Tile(True, False) 
                for y in range(0, constants.MAP_HEIGHT)] 
               for x in range(0, constants.MAP_WIDTH)]

    create_maze()

    #room1 = Rect(1, 2, 10, 10)
    #room2 = Rect(10, 10, 10, 12)
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

    # draw the dragon
    DRAGON.draw()


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
                running = False
                break
            
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

    pygame.quit()


def game_initialize():

    global SURFACE_MAIN, GAME_MAP, PLAYER, DRAGON

    #Initialize the pygame
    pygame.init()

    #Create the screen
    SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )

    GAME_MAP = map_create()

    PLAYER = Obj_Actor(1, 1, constants.S_PLAYER)
    DRAGON = Obj_Actor(constants.MAP_WIDTH-2, constants.MAP_HEIGHT-2, constants.S_DRAGON)




#Main
if __name__ == "__main__":
    game_initialize()
    game_loop()