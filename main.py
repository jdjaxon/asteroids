"""Asteroids clone using pygame."""

import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player
from shot import Shot


def main():
    """Runs main game loop"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            # pylint: disable=no-member
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for obj in asteroids:
            if obj.detect_collision(player):
                print("Game over!")
                sys.exit(0)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        # Setting frame rate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
