import pygame, sys

#Initialize the pygame
pygame.init()

#Create the screen
size = [800, 600]
screen = pygame.display.set_mode((size))

# Add Title and Icon to window
pygame.display.set_caption("PDG Project")
icon = pygame.image.load('brick.png')
pygame.display.set_icon(icon)

#Player
player_img = pygame.image.load('man.png')
player_coords = [256, 256]


def player(player_coords):
    screen.blit(player_img, (player_coords))


#Game Loop
running = True
while running:
 
    screen.fill((0, 64, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        #check keystrokes to move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_coords[0] += -32
                print("left")
            if event.key == pygame.K_RIGHT:
                player_coords[0] += 32
                print("right")
            if event.key == pygame.K_UP:
                player_coords[1] += -32
                print("up")
            if event.key == pygame.K_DOWN:
                player_coords[1] += 32
                print("down")
                          
    player(player_coords)
    # set borders for player
    if player_coords[0] < 0:
        player_coords[0] = 0
    elif player_coords[0] > size[0]-32:
        player_coords[0] = size[0]-32
    elif player_coords[1] < 0:
        player_coords[1] = 0
    elif player_coords[1] > size[1]-32:
        player_coords[1] = size[1]-32
    
    pygame.display.update()


#Main
if __name__ == "__main__":
    pass