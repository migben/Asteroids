import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS



class Shot(CircleShape):
    def __init__(self, x, y, velocity, groups):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        for group in groups:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)


    def update(self, dt):
        self.position += self.velocity * dt
