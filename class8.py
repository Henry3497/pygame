# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:39:20 2021

@author: Henry
"""
import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
pygame.init()
screen = pygame.display.set_mode([700, 400])
block_sprites_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


for i in range(100):
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randrange(700)
    block.rect.y = random.randrange(400)
    block_sprites_list.add(block)
    all_sprites_list.add(block)
    
for i in range(1):
    player = Block(RED, 27, 17)
    player.rect.x = random.randrange(700)
    player.rect.y = random.randrange(400)
    all_sprites_list.add(player)





font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 100)

score = 0
play = True
clock = pygame.time.Clock()
startTime = pygame.time.get_ticks()
gameTime = 0
end = False
while play:
    if gameTime < 10:
        gameTime = (pygame.time.get_ticks() - startTime) / 1000
    
    else:
        end = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
     
    (m_x, m_y) = pygame.mouse.get_pos()
    player.rect.x = m_x
    player.rect.y = m_y
        
    ##########################################################
    
    
    
    if end == False:
        hit_list = pygame.sprite.spritecollide(player, block_sprites_list, True)          
        for block in hit_list:
            score = score + 1
            print(score)
   
    
    ############################################################
    screen.fill(WHITE)
    
    
    
    all_sprites_list.draw(screen)
    text = font.render("score:" + str(score), True, YELLOW)
    text2 = font.render("time:" + str(gameTime), True, YELLOW)
    screen.blit(text, (10, 10))
    screen.blit(text2, (10, 30))
    
    if end:
        text = font2.render("game over " + " you get " + str(score) + "point", True, BLACK)
        screen.blit(text, (5 0, 250))   
    
    
    
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()    
        
        
        
        
        
        
        
    