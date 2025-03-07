"""Module defining the Player class."""

from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape)
    """Class for the Player"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)

