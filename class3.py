# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:39:44 2021

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
YELLOW = (255, 255, 0)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")
circle_x = 350
circle_y = 100
rect_x =  300
rect_y = 200
count = 100
color = WHITE
circle_list = []
for i in range(0, count):
    point = []
    circle_x = random.randint(20,680)
    circle_y = random.randint(-700, 0)
    point.append(circle_x)
    point.append(circle_y)
    print(point[1])
    print(point[0])
    circle_list.append(point)

done = False
clock = pygame.time.Clock()
while not done:
    #r = random.randint(0, 255)
    #g = random.randint(0, 255)
    #b = random.randint(0, 255)
   
    #color = (r, g, b)
    
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                print("K_UP PRESS") 
                rect_y = rect_y - 5
            if event.key == pygame.K_DOWN :
                print("K_DOWN PRESS") 
                rect_y =rect_y + 5
            if event.key == pygame.K_LEFT :
                print("K_LEFT PRESS") 
                rect_x = rect_x - 5
            if event.key == pygame.K_RIGHT :
                print("K_RIGHT PRESS") 
                rect_x = rect_x + 5
            if event.key == pygame.K_SPACE :
                print("K_SPACE PRESS")  
        if event.type == pygame.MOUSEBUTTONDOWN:
             pos = pygame.mouse.get_pos()
             print(pos[0])
             print(pos[1])
             rect_x = pos[0]
             rect_y = pos[1]
             
             color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
             
             
             
    pygame.draw.rect(screen, YELLOW, [rect_x, rect_y, 100, 100])
    circle_y = circle_y + 10
    if circle_y > 700:
        circle_y = 0
    
    
    
    for i in range (0, count):
        x = circle_list[i][0]
        y = circle_list[i][1]
        y = y + 1
        circle_list[i][1] = circle_list[i][1] + 1
        pygame.draw.circle(screen, color, (x , y), 10)
        
        
    clock.tick(100)
    pygame.display.flip()            
pygame.quit()    


    
    
    
    
    
    
    
    
    
    
 


        