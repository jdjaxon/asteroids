"""Module for asteroids."""

import random
import pygame

from circleshape import CircleShape
from constants import (
    ASTEROID_MAX_SPLIT_ANGLE,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MIN_SPLIT_ANGLE,
    ASTEROID_SPEED_MULTIPLIER,
)


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


    def split(self):
        """Splits asteroids into smaller asteroids when shot.

        If the asteroid is already at the minimum size, remove the asteroid
        without splitting.
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = (
            pygame.math.Vector2.rotate(self.velocity, angle) * ASTEROID_SPEED_MULTIPLIER
        )
        asteroid2.velocity = (
            pygame.math.Vector2.rotate(self.velocity, -angle) * ASTEROID_SPEED_MULTIPLIER
        )
