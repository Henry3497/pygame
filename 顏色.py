# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:17:17 2021

@author: Henry
"""

import pygame
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (214, 5, 255)
PINK = (253, 0, 204)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
while not done:
    screen.fill(PINK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()            
pygame.quit()            