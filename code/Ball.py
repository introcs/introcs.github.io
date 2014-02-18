__author__ = 'David'

import pygame

pygame.init()
clock = pygame.time.Clock()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("images/ball.png")
ballrect = ball.get_rect()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()

  clock.tick(60)