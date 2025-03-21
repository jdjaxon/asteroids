"""Module defining the Player class."""

import pygame

from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    SHOT_RADIUS,
)


class Player(CircleShape):
    """Class for the Player"""
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0


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


    # pylint: disable=no-member
    # pylint is unable to detect some of pygame's constants.
    # It may be because they are set dynamically.
    def update(self, dt):
        """Update the player's position and rotation."""
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        # Rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # Rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)
        # Move forward
        if keys[pygame.K_w]:
            self.move(dt)
        # Move backward
        if keys[pygame.K_s]:
            self.move(-dt)
        # Shoot
        if keys[pygame.K_SPACE]:
            self.shoot()


    def move(self, dt):
        """Move the player forward and backward."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        """Fires Shot projectiles"""
        if self.shot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
