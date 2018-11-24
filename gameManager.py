import pygame
pygame.mixer.init

from menuPresenter import menuPresenter 

pygame.init()
win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Stratagem")

menuHandler = menuPresenter(pygame, win)
currentScreen = menuHandler

menuHandler.present()

run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            btnClicked = menuHandler.checkIfClicked(x,y)
            print(btnClicked)
            btnClick = menuHandler.handleBtnClick(btnClicked)
        elif event.type == pygame.QUIT:
            run = False
    
  
    
        
        
##    win.fill((0, 0, 0))

    pygame.display.update()


pygame.quit()
