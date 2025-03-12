"""Module for Shot class"""

import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """Class for Shot"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        """Draw object to screen."""
        pygame.draw.circle(screen, "white", self.position, 2)


    def update(self, dt):
        """Update position."""
        self.position += self.velocity * dt
