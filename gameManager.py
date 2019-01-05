import pygame
pygame.mixer.init

from menuPresenter import menuPresenter 

pygame.init()
win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Stratagem")


class gameManager(object):
    def __init__(self, pygame, win):
        self.pygame = pygame
        self.win = win
        self.menuHandler = None
        self.currentScreen = None
        self.levelPresenterActive = False
        self.levelPresenter = None

    def run(self):
        self.menuHandler.present()
        
        run = True

        while run:
            self.pygame.time.delay(30)

            for event in self.pygame.event.get():
                if event.type == self.pygame.MOUSEBUTTONDOWN:
                    x, y = self.pygame.mouse.get_pos()

                    if self.levelPresenterActive:
                        btnClicked = self.levelPresenter.checkIfClicked(x,y)
                        print(btnClicked)
                        btnClick = self.levelPresenter.handleBtnClick(btnClicked)
                    else:
                        btnClicked = self.menuHandler.checkIfClicked(x,y)
                        print(btnClicked)
                        btnClick = self.menuHandler.handleBtnClick(btnClicked)
                elif event.type == self.pygame.QUIT:
                    run = False
            
                
        ##    win.fill((0, 0, 0))

            self.pygame.display.update()


        self.pygame.quit()


gameManager = gameManager(pygame, win)

menuHandler = menuPresenter(pygame, win, gameManager)
gameManager.menuHandler = menuHandler

gameManager.run()
