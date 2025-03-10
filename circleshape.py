"""Module for Circle game Sprites"""

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """Class for Circle game Sprites"""
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Draw the Sprite to the screen. Will be overridden by sub-classes"""
        pass

    def update(self, dt):
        """Update the Sprite. Will be overridden by sub-classes"""
        pass


    def detect_collision(self, other):
        """Detect collisions between CircleShape Sprites.

        Returns True if collision is detected; returns False otherwise.
        """
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
