# Importing pygame
import pygame

# initializate pygame
pygame.init()

# window size
screen_with = 800
screen_height = 600

# size variable

size = (screen_with, screen_height)

# display screen
screen = pygame.display.set_mode(size)

#Title
pygame.display.set_caption("E.T Killer")

#Icon
icon = pygame.image.load("./misil.png")
pygame.display.set_icon(icon)

# game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
























