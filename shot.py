import circleshape as c
import constants as constants
import pygame as p

class Shot(c.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):

        p.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):

        self.move(dt)
  
    def move(self, dt):
        self.position += (self.velocity * dt)
