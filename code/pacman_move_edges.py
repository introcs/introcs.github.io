__author__ = 'David'

import movement
import pygame


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
            movement.keyDown(event, direction)
        elif event.type == pygame.KEYUP:
            movement.keyUp(event, direction)

    movement.checkEdge(pacrect, screen, direction)
    pacrect = pacrect.move(direction)

    screen.fill(black)
    screen.blit(pac, pacrect)
    pygame.display.flip()

    clock.tick(60)