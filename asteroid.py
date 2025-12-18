import pygame
from circleshape import CircleShape
from constants import *

import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        for group in self.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()

            #return
        else:
            angle = random.uniform(20, 50)
            #below currently doesnt spawn - cannot important asteroidfield due to error
            asteroid = Asteroid(self.x, self.y, (self.radius / 2))


               # def spawn(self, radius, position, velocity):
                #    asteroid = Asteroid(position.x, position.y, radius)
                #    asteroid.velocity = velocity