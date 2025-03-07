"""Asteroids clone using pygame."""


import pygame

import constants as ct


def main():
    """Runs main game loop"""
    screen = pygame.display.set_mode((ct.SCREEN_WIDTH, ct.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
