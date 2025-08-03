import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        split_1_velocity = self.velocity.rotate(random_angle)
        split_2_velocity = self.velocity.rotate(-random_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid1.velocity = 1.2 * split_1_velocity
        asteroid2.velocity = 1.2 * split_2_velocity
