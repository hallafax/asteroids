import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        #iterate thru the event cue looking for events
        for event in pygame.event.get():
            #if quit event happens return out of main()
            if event.type == pygame.QUIT:
                return
            
        #color the screen black    
        screen.fill("black")
        #update display
        pygame.display.flip()

        #update clock
        dt = clock.tick() / 1000 
        clock.tick(60)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()

