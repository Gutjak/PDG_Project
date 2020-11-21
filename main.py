import pygame
import sys
import constants
import random
import pytest
import math
import time

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

#start the dragon and chase the player
def dist(a,b):
    return math.sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def make_instructions(path):
    ins = []
    for i in range(len(path)-1):
        ins.append((path[i+1][0] - path[i][0], path[i+1][1] - path[i][1]))
    ins.reverse()
    return ins

def a_star(start, goal):
    open_set = {start : dist(start, goal)} # this is a dict
    came_from = {} # Dict. camefrom(n) is the node before the shortest known  path to n
    g_score = {} #Dict. g_score(n) cost of the shortest path to n.
    g_score[start] = 0

    while(open_set):
        current = min(open_set, key = open_set.get) #pick the node in open_set with the lowest f_score
        open_set.pop(current)
        
        print(current)

        x, y = current

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbour in [c for c in [(x-1,y),
                                      (x+1,y),
                                      (x,y-1),
                                      (x,y+1)] if not new_map[c[0]][c[1]].block_path]:
            
            tentative_g_score = g_score[current] +1

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]: #shorter path
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                open_set[neighbour] = g_score[neighbour] + dist(neighbour, goal)

    return None

def make_path():
    pass


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
    max_shortcuts = 0

    #below 11 tile is to few tiles to makes a decent maze with shortcuts
    if constants.MAP_WIDTH > 11:
        max_shortcuts = int(constants.MAP_WIDTH // 2)

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

    #draw the dragon
    DRAGON.draw()

    #Add text
    SURFACE_MAIN.blit(textsurface,(0,0))

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

myfont = pygame.font.SysFont('Arial', 30)
textsurface = myfont.render('Beware of the Dragon', False, (0, 0, 0))

def enemy_move():

    path = a_star((DRAGON.x, DRAGON.y), (PLAYER.x, PLAYER.y))
    print("Path", path)

    ins = make_instructions(path)

    print("INS:", ins)
    print("ACT:", end="")

    
    x,y = ins.pop()
    print("(" + str(x) + "," + str(y) + "), ", end="")
    DRAGON.move(x,y)

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
                enemy_move()
                
            draw_game()

            pygame.display.update()

    pygame.quit()


def game_initialize():

    global SURFACE_MAIN, GAME_MAP, PLAYER, DRAGON

    #Initialize the pygame
    pygame.init()
    pygame.font.init()

    #Create the screen
    SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )

    GAME_MAP = map_create()

    PLAYER = Obj_Actor(1, 1, constants.S_PLAYER)
    DRAGON = Obj_Actor(constants.MAP_WIDTH-2, constants.MAP_HEIGHT-2, constants.S_DRAGON)




#Main
if __name__ == "__main__":
    game_initialize()
    game_loop()