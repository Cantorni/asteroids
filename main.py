import pygame as p
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    p.init()
    
    updatable = p.sprite.Group()
    drawable = p.sprite.Group()
    asteroids = p.sprite.Group()
    shots = p.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    asteroid_field = AsteroidField()
    player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = p.time.Clock()
    dt = 0
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        updatable.update(dt)
        for element in asteroids:
            if element.check_collision(player_1):
                print("Game over!")
                sys.exit()
        screen.fill((0,0,0))
        for element in drawable:
            element.draw(screen)
        p.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    
