# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:43:05 2021

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

class Brick (pygame.sprite.Sprite):
    def __init__(self, srx, sry, speedx, speedy, w, h, color):
        super().__init__()
        self.image = pygame.Surface([w, h], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        
        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()
        self.rect.x = srx
        self.rect.y = sry
        
        self.dx = speedx
        self.dy = speedy

    def update(self):
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

ball = Ball(100, 100, 20, 20, 10, GREEN)
panel = Brick(300, 400, 0, 0, 100, 20, BLUE)


brickGroup = pygame.sprite.Group()

for j in range(5):
    for i in range(10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        brickGroup.add(Brick(70 * i, 30 * j, 0, 0, 70, 30, (r, g, b)))

score = 0
gameover = False



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
    
    if ball.rect.y >= 500:
        gameover = True
        
    if gameover == True:
        font = pygame.font.Font(None, 100)
        text = font.render("Gameover", True, BLACK)
        screen.blit(text, (160, 250))
    
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    panel.rect.x = mouse_x
    
    ball.update()
    ball.draw(screen)
    panel.draw(screen)
    
    brickGroup.draw(screen)    
    
    
    collideList = pygame.sprite.spritecollide(ball, brickGroup, True)
    
    if len(collideList) > 0 or (pygame.sprite.collide_rect(panel, ball)):
        ball.dx = ball.dx * (-1) 
        ball.dy = ball.dy * (-1)
    
    
    
    
    
    
    for collide in collideList:
        score = score + 1
    
    
    clock.tick(10)
    pygame.display.flip()            
pygame.quit()            





