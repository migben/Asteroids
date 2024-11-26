import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity or pygame.Vector2(0,0)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        if self.radius <= ASTEROID_MIN_RADIUS:
            print(f"An Asteroid at {self.position} is too small and will be destroyed!")
            self.kill()
            return


        # Calculate the radius for new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # generating the random angle for splitting
        random_angle = random.uniform(20, 50)

        # create the first asteroid with scaled velocity
        first_velocity = self.velocity.rotate(random_angle) * 1.2
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius, first_velocity)

        second_velocity = self.velocity.rotate(-random_angle)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius, second_velocity)


        for group in self.groups():
            group.add(first_asteroid)
            group.add(second_asteroid)

        # remove the original asteroid
        print(f"Asteroid at {self.position} has split into two smaller asteroids!")
        self.kill()
