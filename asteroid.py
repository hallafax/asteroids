import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            diverge = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(diverge)
            velocity2 = self.velocity.rotate(-diverge)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = velocity1 * 1.5
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2.velocity = velocity2 * 1.5
