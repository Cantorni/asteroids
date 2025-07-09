import pygame as p
from constants import *
import player 

def main():
    p.init()
    player_1 = player.player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = p.time.Clock()
    dt = 0
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        player_1.update(dt)
        screen.fill((0,0,0))
        player_1.draw(screen)
        p.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    
