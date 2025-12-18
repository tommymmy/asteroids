import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
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
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            ast1_vector = self.velocity.rotate(random_angle)
            ast2_vector = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.velocity = ast1_vector * 1.2
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2.velocity = ast2_vector * 1.2


            #below currently doesnt spawn - cannot important asteroidfield due to error
            #pygame.draw.circle(screen, "white", self.position, (self.radius / 2), LINE_WIDTH)


               # def spawn(self, radius, position, velocity):
                #    asteroid = Asteroid(position.x, position.y, radius)
                #    asteroid.velocity = velocity