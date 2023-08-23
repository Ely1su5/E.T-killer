# Importing pygame and random
import pygame
import random
import random

# initializate pygame
pygame.init()

# window size
screen_with = 800
screen_height = 600

# size variable

size = (screen_with, screen_height)

# display screen
screen = pygame.display.set_mode(size)

#player function
player_x = 370
player_y = 520
player_img = pygame.image.load("nave-espacial (1).png")
player_x_change = 0
def player(x,y):
    screen.blit(player_img,(x,y))

# enemy function
enemy_x = random.randint(0,736)
enemy_y = random.randint(50,150)
enemy_img = pygame.image.load("ovni.png")
enemy_x_change = 0.2
enemy_y_change = 20
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

# misil function
misil_x = 370
misil_y = 455
misil_img = pygame.image.load("misil2.0.png")
misil_x_change = 0
misil_y_change = 0.1
misil_state = True
def misil(x,y):
    global misil_state
    misil_state = False
    screen.blit(misil_img,(x,y))

#Title
pygame.display.set_caption("E.T Killer")

#Icon
icon = pygame.image.load("./misil.png")
pygame.display.set_icon(icon)

# bg image
background = pygame.image.load("istockphoto-1478451948-1024x1024.jpg")

# game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5

            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            
            if event.key == pygame.K_SPACE:                  
                misil(player_x,misil_y)
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_change = -0

            if event.key == pygame.K_RIGHT:
                player_x_change = 0
                
                
        
        
        
    # blit of the background
    screen.blit(background, (0,0))

    # PLATER MOVEMENTS
    player_x += player_x_change
    
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    
    # blit of the player
    player(player_x,player_y)

    # blit of enemy
    enemy(enemy_x,enemy_y)


    # enemy movements
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    
    elif enemy_x >= 736 :
        enemy_x_change = -0.3
        enemy_y + enemy_y_change

    if misil_state == False:
        misil(player_x, misil_y)
        print(11)
        misil_y -= misil_y_change
    
    # misil movements
    
    
    # update the window
    pygame.display.flip()
pygame.quit()