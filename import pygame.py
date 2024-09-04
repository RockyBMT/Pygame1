import pygame
import math

pygame.init()
screen = pygame.display.set_mode((854,480))
pygame.display.set_caption("python-game")
clock = pygame.time.Clock()
x=411
y=240
mRight = False
mLeft = False
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

running  = True
jump = False
jumpCount=10

while running:  
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mRight = True
            elif event.key == pygame.K_a:
                mLeft = True
            elif event.key == pygame.K_w and not jump:
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                mRight = False
            elif event.key == pygame.K_a:
                mLeft = False
    if mRight:
        x=x+5
    if mLeft:
        x=x-5
    if not jump:
        if y>=448:
            y=448
        else:
            y=y+8
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.2 * neg
            jumpCount -= 1
        if jumpCount == -10:
            jump = False
            jumpCount = 10

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [x, y, 32, 32])
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)