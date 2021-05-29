# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:34:45 2021

@author: Henry
"""
import pygame
import random
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (214, 5, 255)
PINK = (253, 0, 204)
pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self, srx, sry, speedx, speedy, radium, color):
        self.image = pygame.Surface([radium * 2, radium * 2], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()


        pygame.draw.circle(self.image, color, (radium, radium), radium)
        self.rect = self.image.get_rect()
        self.rect.x = srx
        self.rect.y = sry
        self.dx = speedx
        self.dy = speedy
        
    def update(self):
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.dx = (-1) * self.dx
        
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.dy = (-1) * self.dy
        
        
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

ball = Ball(100, 100, 20, 20, 10, GREEN)
ball2 = Ball(600, 400, -30, -10, 20, BLUE)

done = False
clock = pygame.time.Clock()
while not done:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if pygame.sprite.collide_rect(ball, ball2):
        ball.dx = ball.dx * (-1)
        ball.dy = ball.dy * (-1)
        ball2.dx = ball.dx * (-1)
        ball2.dy = ball.dy * (-1)
    
    ball.update()
    ball2.update()
    ball.draw(screen)
    ball2.draw(screen)
    
    clock.tick(10)
    pygame.display.flip()            
pygame.quit()            
