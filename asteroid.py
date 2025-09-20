from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        child_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2

