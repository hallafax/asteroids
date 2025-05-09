import pygame
from constants import *
from player import Player
from shot import Shot   
from asteroid import Asteroid
from asteroid_field import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        #iterate thru the event cue looking for events
        for event in pygame.event.get():
            #if quit event happens return out of main()
            if event.type == pygame.QUIT:
                return
            
        #color the screen black    
        screen.fill("black")

        #update groups
        updatable.update(dt)

        #draw group
        for thing in drawable:
            thing.draw(screen)


        #check for collisions with player
        for thing in asteroids:
            if thing.collide(player):
                print("Game Over!")
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()

        #update display
        pygame.display.flip()

        #update clock
        dt = clock.tick() / 1000 
        clock.tick(144)
    
if __name__ == "__main__":
    main()

