import pygame
from constants import *

infinite_while = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while infinite_while == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("BLACK")
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
