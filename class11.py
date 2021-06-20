# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:02:43 2021

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

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

class Segment (pygame.sprite.Sprite):
    def __init__(self, x, y, color, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y



segment_x = 200
segment_y = 200

segment_margin = 5
segment_w = 25
segment_h = 25
segmetList = []
segmentGroup = pygame.sprite.Group()        
for i in range(3):
    segment_x = segment_x - segment_w - segment_margin 
    segment = Segment(segment_x, segment_y, BLACK, segment_w, segment_h)
    segmentGroup.add(segment)
    segmetList.append(segment)    
        
x_change = 1
y_change = 0

done = False
clock = pygame.time.Clock()
while not done:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -1
                x_change = 0
            if event.key == pygame.K_DOWN:
                y_change = 1
                x_change = 0    
            if event.key == pygame.K_LEFT:
                y_change = 0
                x_change = -1
            if event.key == pygame.K_RIGHT:
                y_change = 0
                x_change = 1
    if len(segmetList) > 0:
        popSegment = segmetList.pop()
        segmentGroup.remove(popSegment)
    
    x = segmetList[0].rect.x + (segment_w + segment_margin) * x_change
    y = segmetList[0].rect.y + (segment_h + segment_margin) * y_change
    segmentNew = Segment(x, y, BLACK, segment_w, segment_h)
    segmetList.insert(0, segmentNew)
    segmentGroup.add(segmentNew)
    
    
    segmentGroup.draw(screen)
    
    
    
    clock.tick(10)
    pygame.display.flip()            
pygame.quit()  