__author__ = 'David'

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
            if event.key == pygame.K_RIGHT:
                pacrect = pacrect.move([5, 0])
            elif event.key == pygame.K_LEFT:
                pacrect = pacrect.move([-5, 0])
            elif event.key == pygame.K_DOWN:
                pacrect = pacrect.move([0, 5])
            elif event.key == pygame.K_UP:
                pacrect = pacrect.move([0, -5])

    screen.fill(black)
    screen.blit(pac, pacrect)
    pygame.display.flip()

    clock.tick(60)