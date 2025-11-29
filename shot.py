import pygame
from circleshape import CircleShape
from player import *
from constants import *

class Shot(CircleShape):
    def __init__(self, player_position, player_rotation):
        super().__init__(player_position, player_rotation, SHOT_RADIUS)
        self.rotation = player_rotation
        self.radius = SHOT_RADIUS
        for group in self.containers:
            group.add(self)
            
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)