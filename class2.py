# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:17:17 2021

@author: Henry
"""

import pygame
from math import pi
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (214, 5, 255)
PINK = (253, 0, 204)
YELLOW = (255, 255, 0)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

rect_x =0
rect_y = 150
r = 1
shift = 1
done = False
clock = pygame.time.Clock()
while not done:
    
    screen.fill(PINK)
    rect_x = rect_x + 1
    pygame.draw.rect(screen, YELLOW, (rect_x, rect_y, 100, 200))
    pygame.draw.polygon(screen, BLACK, [(350, 100),(300, 150),(400,150)])
    
    
    r =  r + shift
    pygame.draw.circle(screen, YELLOW, (200, 150), r)
    
    if r > 200:
        shift = shift * -1
    if r < 1:
        shift = shift * -1
    
    
    #pygame.draw.rect(screen, YELLOW, (150, 0, 100, 100))
    #pygame.draw.circle(screen,GREEN ,(200, 150), 50)
    #pygame.draw.polygon(screen, BLUE, [(200, 200), (175,270), (225,270)])
    #pygame.draw.arc(screen, BLACK, (150, 410, 100, 150), pi, 2 * pi)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)
    pygame.display.flip()            
pygame.quit()












            