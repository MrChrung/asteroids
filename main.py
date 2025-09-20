import pygame
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, shots, drawable)

    #Set FPS
    clock = pygame.time.Clock()
    dt = 0

    #instantiate player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()


        screen.fill("black")
        for object in drawable:
            object.draw(screen)

        # render changes at 60 FPS
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
