__author__ = 'David'

import constants
import pygame
import random


BLOCK_PATH = 'images/block.png'


class Block:

    sprite = pygame.image.load(BLOCK_PATH)
    pygame.font.init()
    font = pygame.font.SysFont('helvetica', 40, bold=True)

    def __init__(self, row, column):
        # TODO Set all the needed information for my block .
        pass

    def move(self, row, column):
        # TODO Move the rectangle to the new grid position.
        pass

    def merge(self, other_block):
        # TODO Merge another block into this one if it's the same value.
        # Merge should return true or false depending on whether the merge was successful.
        pass

    def draw(self, screen):
        # Draw the background of the block.
        screen.blit(self.sprite, self.rect)

        # Draw the number
        number = self.font.render(str(self.value), 1, (119, 110, 101))
        number_rect = number.get_rect()
        number_rect.center = self.rect.center
        screen.blit(number, number_rect)

    def calculate_center_(self, row, column):
        # TODO Calculate x and y values on the screen based off of the grid position.
        pass

