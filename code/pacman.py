__author__ = 'David'

import pygame

def keydown(event, direction):
    if event.key == pygame.K_UP:
        direction[1] = -5
    elif event.key == pygame.K_DOWN:
        direction[1] = 5
    elif event.key == pygame.K_RIGHT:
        direction[0] = 5
    elif event.key == pygame.K_LEFT:
        direction[0] = -5

def keyup(event, direction):
    if (event.key == pygame.K_UP or
        event.key == pygame.K_DOWN):
        direction[1] = 0
    elif (event.key == pygame.K_RIGHT or
        event.key == pygame.K_LEFT):
        direction[0] = 0

pygame.init()
clock = pygame.time.Clock()

size = width, height = 320, 240
direction = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

pac = pygame.image.load("../images/pacman.png")
pacrect = pac.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, direction)
        elif event.type == pygame.KEYUP:
            keyup(event, direction)

    pacrect = pacrect.move(direction)

    screen.fill(black)
    screen.blit(pac, pacrect)
    pygame.display.flip()

    clock.tick(60)