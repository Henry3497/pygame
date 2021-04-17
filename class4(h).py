# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:56:18 2021

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

picture = pygame.image.load("太空.jfif")
picture = pygame.transform.scale(picture, size)
picture.convert()

ship = pygame.image.load("去背.png")
ship = pygame.transform.scale(ship,(100, 170))
ship.convert()
shootSound = pygame.mixer.Sound("射擊音效.ogg")

ship_x = 300
ship_y = 400

done = False
clock = pygame.time.Clock()
while not done:
    screen.fill(BLACK)
    screen.blit(picture, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                print("K_SPACE PRESS")  
                shootSound.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                print("K_LEFT PRESS") 
                ship_x = ship_x - 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                print("K_RIGHT PRESS") 
                ship_x = ship_x + 5
        if event.type == pygame.MOUSEBUTTONDOWN:
             pos = pygame.mouse.get_pos()
             print(pos[0])
             print(pos[1])
             ship_x = pos[0]
             ship_y = pos[1]
             shootSound.play()
    screen.blit(ship,(ship_x,ship_y))
    clock.tick(100)
    pygame.display.flip()            
pygame.quit()    


    
    
    
    
    
    
    
    
    
    
 


        