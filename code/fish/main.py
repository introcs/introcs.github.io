__author__ = 'David'

import constants
import fish
import pygame
import random


def handle_quit(event):
    if event.type == pygame.QUIT:
        quit()


def handle_arrows(event, speed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed[0] = -3
        elif event.key == pygame.K_RIGHT:
            speed[0] = 3
        elif event.key == pygame.K_UP:
            speed[1] = -3
        elif event.key == pygame.K_DOWN:
            speed[1] = 3
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            speed[0] = 0
        elif event.key == pygame.K_RIGHT:
            speed[0] = 0
        elif event.key == pygame.K_UP:
            speed[1] = 0
        elif event.key == pygame.K_DOWN:
            speed[1] = 0

    return speed


def check_collisions(player_fish, other_fishes)
    # Check for collisions between the player and other sprites.
    collisions = pygame.sprite.spritecollide(player_fish, other_fishes, True)

    for c in collisions:
        if not player_fish.hit_fish(c):
            player_fish.kill()


def add_fishes(other_fishes, all_fishes):
    # Check if there are enough fishes and add some if needed.
    while len(other_fishes) < 5:
        size = random.randint(1, 30)
        direction = random.choice((constants.LEFT, constants.RIGHT))
        if direction == constants.RIGHT:
            x = 0
        else:
            x = constants.WIDTH
        y = random.randint(20, 580)

        f = fish.Fish(x, y, size, direction)
        other_fishes.add(f)


def check_win(player_fish):
    return player_fish.size > 50


def check_loss(player_fish):
    return not player_fish.alive()


def display_message(message, screen):
    pygame.font.init()
    font = pygame.font.SysFont('helvetica', 40, bold=True)
    message_surface = font.render(message, 1, (119, 110, 101))
    message_rect = message_surface.get_rect()
    message_rect.center = screen.get_rect().center
    screen.blit(message_surface, message_rect)


def main():
    pygame.init()  # Initialize pygame.
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(constants.SIZE)
    speed = [0, 0]
    loss = False
    win = False

    all_fishes = pygame.sprite.Group()
    other_fishes = pygame.sprite.Group()

    player_fish = fish.Fish(constants.WIDTH / 2, constants.HEIGHT / 2, 3, constants.RIGHT)
    all_fishes.add(player_fish)

    while not loss and not win:
        for event in pygame.event.get():
            handle_quit(event)  # Handle quiting the game.
            speed = handle_arrows(event, speed)
            if speed:
                player_fish.move(speed)

        # Check for player collisions.
        check_collisions(player_fish, other_fishes)
        # Add new fishes.
        add_fishes(other_fishes, all_fishes)

        # Check for wins or loses.
        win = check_win(player_fish)
        loss = check_loss(player_fish)

        # Update all the fishes positions and statuses.
        all_fishes.update(screen)

        screen.fill(constants.BACKGROUND)
        # Draw all of the blocks.
        all_fishes.draw(screen)

        pygame.display.flip()
        clock.tick(constants.REFRESH_RATE)

    if win:
        message = "Congrats! You've destroyed the ecosystem!"
    else:
        message = "You lose. Too bad."

    display_message(message, screen)
    pygame.display.flip()
    clock.tick(constants.REFRESH_RATE)

    pygame.time.wait(3000)


if __name__ == '__main__':
    main()