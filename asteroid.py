"""Module for asteroids."""

import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    """Class for asteroid sprites"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        """Draw object to screen."""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        """Update position."""
        self.position += self.velocity * dt
