__author__ = 'David'

import block
import constants
import pygame
import random


def handle_quit(event):
    if event.type == pygame.QUIT:
        quit()


def handle_add_block(event, blocks):
    if event.type == constants.ADD_BLOCK_EVENT:
        # Turn off the timer.
        pygame.time.set_timer(constants.ADD_BLOCK_EVENT, 0)
        add_block(blocks)


def handle_arrows(event):
    direction = None
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            direction = constants.UP
        elif event.key == pygame.K_DOWN:
            direction = constants.DOWN
        elif event.key == pygame.K_RIGHT:
            direction = constants.RIGHT
        elif event.key == pygame.K_LEFT:
            direction = constants.LEFT

    return direction


def add_block(blocks):
    # If all the blocks are full, quit the game.
    if all(blocks):
        quit()

    # Find a random empty block.
    rand = random.randint(0, len(blocks) - 1)
    while blocks[rand]:
        rand += 1
        rand %= 16

    # Create a new block at that position.
    blocks[rand] = block.Block(int(rand % 4), int(rand / 4))


def move_single_block(blocks, old_position, new_position):
    # Copy the block, update it's position, and reset the old spot.
    blocks[new_position] = blocks[old_position]
    blocks[new_position].move(int(new_position % 4), int(new_position / 4))
    blocks[old_position] = None


def move_blocks(blocks, direction):
    # Create a modifier to reverse counting order if needed
    order_modifier = 1
    list_order = sorted
    if direction == constants.DOWN or direction == constants.RIGHT:
        order_modifier = -1
        list_order = reversed

    horizontal = True
    if direction == constants.UP or direction == constants.DOWN:
        horizontal = False

    # This flag will tell us if a movement occurred. We should only add a new block if movement occurred.
    movement = False

    # Iterate over all the lines starting at the far end of the direction of movement.
    for line in range(4):
        spot_increment = 4
        if horizontal:
            line *= 4
            spot_increment = 1
        empty_position = None
        previous_filled = None
        # Within a line, iterate over the spots.
        for spot in list_order(range(line, line + (spot_increment * 4), spot_increment)):
            # Set the empty position to the first spot.
            if empty_position is None:
                empty_position = spot

            # If there's a blank position before this spot, move the block.
            if blocks[spot]:
                if previous_filled is not None and blocks[previous_filled].merge(blocks[spot]):
                        blocks[spot] = None
                        movement = True
                else:
                    if (order_modifier * empty_position) < (order_modifier * spot):
                        move_single_block(blocks, spot, empty_position)
                        movement = True

                    # The empty is now the last filled spot.
                    previous_filled = empty_position

                    # Update the empty position to the next free slot.
                    empty_position += spot_increment * order_modifier

    if movement:
        # Kick off a timer to add a block.
        pygame.time.set_timer(constants.ADD_BLOCK_EVENT, 200)


def main():
    pygame.init()  # Initialize pygame.
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(constants.SIZE)

    blocks = [None]*16  # Create an array with 16 empty spots.
    add_block(blocks)  # Add two blocks to start the game.
    add_block(blocks)

    while 1:
        for event in pygame.event.get():
            handle_quit(event)  # Handle quiting the game.
            handle_add_block(event, blocks)  # Handle the custom event to add a block
            direction = handle_arrows(event)
            if direction:
                move_blocks(blocks, direction)

        screen.fill(constants.BACKGROUND)
        # Draw all of the blocks.
        for b in blocks:
            if b:
                b.draw(screen)

        pygame.display.flip()
        clock.tick(constants.REFRESH_RATE)


if __name__ == '__main__':
    main()