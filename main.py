
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =  pygame.sprite.Group()

    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Checking for collisions between the player and asteroids
        for asteroid in asteroids:
             if player.check_collision(asteroid):
                  print("Game Over!")
                  return

        screen.fill((0,0,0))

        for obj in drawable:
             obj.draw(screen)

        # lets update the display
        pygame.display.flip()
        # then lets update the clock
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
        main()
