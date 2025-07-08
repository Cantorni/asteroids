import pygame as p
from constants import *

def main():
    p.init()
    
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                return
            
        screen.fill((0,0,0))
        p.display.flip()

if __name__ == "__main__":
    main()
    
