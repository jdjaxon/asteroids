"""Module defining the Player class."""

import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
)


class Player(CircleShape):
    """Class for the Player"""
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


    def triangle(self):
        """Calculate points for player's triangle.

        Though the player's sprite is still a circle, this represents the player
        as a triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        """Draws the player to the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        """Rotate the player's Sprite."""
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            self.rotate(dt)
