"""Asteroids clone using pygame."""


import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player


def main():
    """Runs main game loop"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            # pylint: disable=no-member
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
