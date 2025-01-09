# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field1  = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updateable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for unit in updateable:
            unit.update(dt)
        for asteroid in asteroids:
            if asteroid.check_for_collisions(player1):
                print("Game over!")
                exit()
            for shot in shots:
                if shot.check_for_collisions(asteroid):
                    shot.kill()
                    asteroid.split()
        pygame.Surface.fill(screen,color="black")
        for unit in drawable:
            unit.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()