# Importing pygame and random and math
import pygame
import random
import random
import math

from pygame import mixer

# initializate pygame
pygame.init()

# window size
screen_with = 800
screen_height = 600

# size variable

size = (screen_with, screen_height)

# display screen
screen = pygame.display.set_mode(size)

# score font
score_font = pygame.font.Font("Plane Crash.ttf", 50)

#variable score
score = 0

#position text in screen
text_x = 10
text_y = 10

#game over font
go_x = 270  
go_y = 300
#condicion de una vez game over
go_condition = True


#player function
player_x = 370
player_y = 520
player_img = pygame.image.load("nave-espacial (1).png")
player_x_change = 0
def player(x,y):
    screen.blit(player_img,(x,y))

# enemy function
enemy_x = []
enemy_y = []
enemy_img = [] 
enemy_x_change = []
enemy_y_change = []
number_enemies = 8

for item in range(number_enemies):
    
    enemy_y
    enemy_img.append(pygame.image.load("ovni.png"))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)
def enemy(x,y, item):
    screen.blit(enemy_img[item],(x,y))

# misil function
misil_x = 370
misil_y = 455
misil_img = pygame.image.load("misil2.0.png")
misil_x_change = 0
misil_y_change = 5
misil_state = True
def misil(x,y):
    global misil_state
    misil_state = False
    screen.blit(misil_img,(x,y))

# colision
def is_colision (m_x, m_y, e_x, e_y):
    distance = math.sqrt((e_x - m_x)**2 + (e_y - m_y)**2)
    if distance < 27:
        return True
    else:
        return False
    
def game_over(x,y):
    global go_condition
    go_text = score_font.render("pal lobby",True,(123, 36, 28))
    # game over sound
    if go_condition :
        game_over_sound = mixer.Sound("./power-down-7103.wav")
        game_over_sound.play()
        go_condition = False
    screen.blit(go_text, (x,y))


def show_score(x,y):
    score_text = score_font.render("score: " + str(score),True,(255,0,0))
    screen.blit(score_text, (x,y))

#Title
pygame.display.set_caption("E.T Killer")

#Icon
icon = pygame.image.load("./misil.png")
pygame.display.set_icon(icon)

#background sounds
pygame.mixer.music.load("./bg.wav")
pygame.mixer.music.play(-1)

#misil sounds
mixer.music.load("./missile-blast-2-95177.wav")

# bg image
background = pygame.image.load("istockphoto-1478451948-1024x1024.jpg")

# game loop
running = True
clock = pygame.time.Clock()
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
            
            if event.key == pygame.K_SPACE and misil_state == True:                  
                misil_x = player_x
                misil(misil_x,misil_y)
                misil_sound = mixer.Sound("./missile-blast-2-95177.wav")
                misil_sound.play()
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
    
    for item in range(number_enemies ):
        
        if enemy_y[item] > 440:
            for j in range (number_enemies):
                enemy_y[j] = 2000 
            game_over(go_x,go_y)
            break




        colision = is_colision(misil_x, misil_y, enemy_x[item], enemy_y[item])
        if colision:
            misil_y = 480
            misil_state = True
            score += 50
            enemy_x[item] = random.randint(0, 735)
            enemy_y[item] = random.randint(50, 150)
        
        # blit of enemy
        enemy(enemy_x[item],enemy_y[item], item)


        # enemy movements
        enemy_x[item] += enemy_x_change[item]
        if enemy_x[item] <= 0:
            enemy_x_change[item] = 1
            enemy_y[item] += enemy_y_change[item]
        
        elif enemy_x[item] >= 736 :
            enemy_x_change[item] = -1
            enemy_y[item] + enemy_y_change[item]

    if misil_state == False:
        misil(misil_x, misil_y)
        misil_y -= misil_y_change

    if misil_y <= 0:
        misil_y = 480
        misil_state = True
    colision = is_colision(misil_x, misil_y, enemy_x[item], enemy_y[item])
    if colision:
        misil_y = 480
        misil_state = True
        enemy_x[item]  = random.randint(0, 735)
        enemy_y[item] = random.randint(50, 150)
    
    # misil movements
    
    
    # update the window
    #clock.tick(60)
    show_score(text_x, text_y)
    pygame.display.flip()
pygame.quit()