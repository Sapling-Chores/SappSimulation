import sys
import pygame
from pygame.locals import*
import math



pygame.init()
screenWidth = 1200
screenHeight = 600

Screen = pygame.display.set_mode((screenWidth, screenHeight))
icon = pygame.image.load("pythongame1logo.png")

pygame.display.set_icon(icon)
background = pygame.image.load("backgroundPygame1.png")

normalFish2 = pygame.image.load("fish2.png")
normalFish3 = pygame.image.load("tuna.png")

fastfish1 = pygame.image.load("clown-fish.png")

rectWidth = 50
rectHeight = 50
rectX = 0
rectY = screenHeight - rectHeight
rectXspeed , rectYspeed = 60, 80


gravity = .5
jumpState = False

e = 0.5
# v^2 = u^2 + 2gh
while True:
    dt  = pygame.time.Clock().tick(60) / 16
    Screen.fill((0, 0, 0))
    Screen.fill((0, 0, 0, ))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rectXspeed = -10
            if event.key == pygame.K_d:
                rectXspeed = 10
            if event.key == pygame.K_SPACE and not jumpState:                
                rectYspeed  = -9.8
                jumpState = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                rectXspeed = 0
            if event.key == pygame.K_d:
                rectXspeed = 0
    try: 
      pointerPos = pygame.mouse.get_pos()
      print(pointerPos)
      rectX += rectXspeed
      rectYspeed += gravity 
      rectY += rectYspeed
      
      if rectX<0 and rectXspeed < 0: 
          rectXspeed =  rectXspeed = 0 
          rect
      elif rectX> screenWidth - rectWidth : rectXspeed =   rectXspeed = 0
      if rectY >= screenHeight - rectHeight and rectYspeed != 0: 
          rectYspeed = (0 - rectYspeed) 
      elif rectY <= 0 and rectYspeed != 0:
          rectYspeed = (0 - rectYspeed)
      if jumpState == True and rectY >= screenHeight - rectHeight - 5 :
          jumpState = False
      if rectY >= screenHeight - rectHeight and rectYspeed <= 0.1: 
          rectY = screenHeight - rectHeight
          
      rect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
      collide = rect.collidepoint(pointerPos)
      if collide:        
       pygame.draw.rect(Screen, (200, 0, 200), rect, 25, 2)
      else: pygame.draw.rect(Screen, (250, 250, 0), rect, 25, 30)
    except : pass
      
    pygame.display.update()
            
      