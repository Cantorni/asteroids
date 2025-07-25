import circleshape as c
import pygame as p
import constants
from shot import Shot

class Player(c.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = p.Vector2(0, 1).rotate(self.rotation)
        right = p.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        p.draw.polygon(screen,(255,255,255),self.triangle(),2)
    
    def update(self, dt):
        self.timer -= dt
        keys = p.key.get_pressed()
        
        
        if keys[p.K_w] or keys[p.K_UP]:
            self.move(dt)
        if keys[p.K_s] or keys[p.K_DOWN]:
            self.move(dt*-1)

        if keys[p.K_a] or keys[p.K_RIGHT]:
            self.rotate(dt)
        if keys[p.K_d] or keys[p.K_LEFT]:
            self.rotate(dt*-1)
        if keys[p.K_SPACE]:
            self.shoot(dt)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = p.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self,dt):
        
        if self.timer <= 0:
            shot = Shot(self.position.x,self.position.y,constants.SHOT_RADIUS)
            shot.velocity = p.Vector2(0, 1)
            shot.velocity.rotate(self.rotation)
            forward = p.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * constants.PLAYER_SHOOT_SPEED
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
