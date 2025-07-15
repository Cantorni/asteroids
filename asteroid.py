import pygame as p
import circleshape as c
import constants
import random

class Asteroid(c.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):

        p.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):

        self.move(dt)
  
    def move(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            a_1 = Asteroid(self.position.x,self.position.y,new_radius)
            a_2 = Asteroid(self.position.x,self.position.y,new_radius)
            a_1.velocity = vector_1*1.2
            a_2.velocity = vector_2*1.2