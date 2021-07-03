# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 14:40:55 2021

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
RED = (255, 0, 0)

pygame.init()
circle = 16
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")
done = False
circle_x = 350
circle_y = 250
clock = pygame.time.Clock()

screen.fill(PINK)
while not done:
    pygame.draw.circle(screen,GREEN ,(200, 150), 50)
    
    

    pygame.draw.circle(screen, WHITE, (200, 150), 10)

     
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

clock.tick(100)
pygame.display.flip()            
pygame.quit()    