import pygame

from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x_pos = SCREEN_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2
    player = Player(x_pos, y_pos)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")

        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
