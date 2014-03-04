__author__ = 'David'

import pygame


def keyDown(event, direction):
    """Update the direction when a key is pressed down.

    Args:
        event: The KEYDOWN event which was fired.
        direction: A list containing two values for the direction, x and y.
    """
    if event.key == pygame.K_UP:
        direction[1] = -5
    elif event.key == pygame.K_DOWN:
        direction[1] = 5
    elif event.key == pygame.K_RIGHT:
        direction[0] = 5
    elif event.key == pygame.K_LEFT:
        direction[0] = -5

def keyUp(event, direction):
    """Reset the direction when a key is lifted up.

    Args:
        event: The KEYUP event which was fired.
        direction: A list containing two values for the direction, x and y.
    """
    if (event.key == pygame.K_UP or
        event.key == pygame.K_DOWN):
        direction[1] = 0
    elif (event.key == pygame.K_RIGHT or
        event.key == pygame.K_LEFT):
        direction[0] = 0

def checkEdge(rect, screen, direction):
    """Check if the rectangle has hit the edge and reset the direction if it has.

    Args:
        rect: The rectangle which is being moved.
        screen: The screen which the rectangle is being moved on.
        direction: A list containing two values for the direction, x and y.
    """
    if rect.left <= 0 and direction[0] < 0:
        direction[0] = 0
    if rect.right >= screen.get_width() and direction[0] > 0:
        direction[0] = 0
    if rect.top <= 0 and direction[1] < 0:
        direction[1] = 0
    if rect.bottom >= screen.get_height() and direction[1] > 0:
        direction[1] = 0