__author__ = 'David'

import constants
import pygame


IMAGE_PATH = 'images/fish.png'
BASE_IMAGE_SIZE = 10


class Fish():

    default_image = pygame.image.load(IMAGE_PATH)

    def __init__(self, x_position, y_position, size, direction):
        # TODO, I can't figure out why this doesn't work...
        pygame.sprite.Sprite.__init__(self)

        # Set the initial state.
        self.size = size
        self.direction = direction
        self.speed = [direction * 2, 0]

        # Load the images.
        self.image = self.default_image
        self.rect = self.image.get_rect()

        self.rect.center = (x_position, y_position)

        # Set the initial size and direction.
        self.resize_image_()

        # The default image is pointing left, so flip if necessary.
        if direction == constants.RIGHT:
            self.image = pygame.transform.flip(self.image, True, False)

    def move(self, speed):
        # Check if the new speed is changing direction and flip the fish if necessary.
        if self.speed[0] * self.direction < 0:
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)

        self.speed = speed

    def hit_fish(self, other):
        if self.size >= other.size:
            # Update the size.
            self.size += other.size / 2
            self.resize_image_()
            return True
        return False

    def update(self, screen):
        # Move the sprite.
        self.rect = self.rect.move(self.speed)

        # If the sprite is off the screen, kill it.
        if screen.get_rect().collidelist([self.rect]) < 0:
            # TODO Hmm, I should probably do something here...

    def resize_image_(self):
        # Resize the image.
        new_width = (self.size * 3 + BASE_IMAGE_SIZE) * 2
        new_height = self.size * 3 + BASE_IMAGE_SIZE
        self.image = pygame.transform.scale(self.default_image, (new_width, new_height))

        # Retrieve the new rectangle, maintaining the center
        previous_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = previous_center