# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:51:31 2021

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
RED = (255, 0, 0)
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

font = pygame.font.Font(None, 50)


ship_x = 300
ship_y = 400
    
ball_x = x = random.randint(0, 700)
ball_y = -100
fires = []

fireCount = 100
for i in range(fireCount):
    position = []
    x = random.randint(0, 700)
    y = random.randint(-500, 0)
    position.append(x)
    position.append(y)
    fires.append(position)
score = 0
done = False
clock = pygame.time.Clock()
timeTick = pygame.time.get_ticks()
gameTime = 0
while not done:
    gameTime = (pygame.time.get_ticks() - timeTick)/ 1000
    
    screen.fill(BLACK)
    screen.blit(picture, (0,0))
    if pygame.key.get_pressed()[pygame.K_LEFT]  != 0:
        ship_x = ship_x - 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]  != 0:
        ship_x = ship_x + 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                print("K_SPACE PRESS")  
                shootSound.play()
                ball_x = ship_x + int(100 / 2)
                ball_y = ship_y
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
    ######################################################
    for i in range(fireCount): 
        if fires[i][0] <= ball_x and  fires[i][0] + 10 >= ball_x:
            if fires[i][1] <= ball_y and fires[i][1] +10 >= ball_y:
                score = score + 1
    
    ###################################################################
    screen.blit(ship,(ship_x,ship_y))
    
    for i in range(fireCount):
        pygame.draw.circle(screen, RED, (fires[i][0], fires[i][1]), 9)
        
        fires[i][1] = fires[i][1] + 5
        
        if fires[i][1] > 500:
            fires[i][1] = random.randint(-500,0)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 9)      
    if ball_y > -100:
        ball_y = ball_y - 5
    
    
    
    
    
    
    screen.blit(ship,(ship_x,ship_y))
    text = font.render("score:" + str(score), True, YELLOW)
    screen.blit(text, (10, 10))
    
    text = font.render("time:" + str(gameTime), True, YELLOW)
    screen.blit(text, (10, 50))
    clock.tick(37)
    pygame.display.flip()            
pygame.quit()    


    
    
    
    
    
    
    
    
    
    
 


        