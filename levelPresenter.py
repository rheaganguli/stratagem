import pygame
from button import button
from level1 import level1
import os



class levelPresenter(object):

    buttonList = []
    
    def __init__(self, pygame, win, gameManager):
        self.pygame = pygame
        self.win = win
        w, h = pygame.display.get_surface().get_size()
        print('something')
        self.x_center = w/2
        self.y_center = h/2
        self.gameManager = gameManager
        self.levelOneBtn = None
        self.levelTwoBtn = None
        self.levelThreeBtn = None
        self.levelFourBtn = None 
        self.levelFiveBtn = None 
        
        
    def present(self):
        self.win.fill((0,0,0))
        self.levelOneBtn = button(self.pygame, self.win, (255,153,51), (self.x_center - (100/2)), (self.y_center - 200), 100, 50, "Level 1", 13)
        self.levelOneBtn.draw()
        self.levelTwoBtn = button(self.pygame, self.win, (255,100,175), (self.x_center - (100/2)), (self.y_center - 100), 100, 50, "Level 2", 13)
        self.levelTwoBtn.draw()
        self.levelThreeBtn = button(self.pygame, self.win, (255,123,231), (self.x_center - (100/2)), (self.y_center), 100, 50, "Level 3", 13)
        self.levelThreeBtn.draw()
        self.levelFourBtn = button(self.pygame, self.win, (255,90,185), (self.x_center - (100/2)), (self.y_center + 100), 100, 50, "Level 4",13)
        self.levelFourBtn.draw()
        self.levelFiveBtn = button(self.pygame, self.win, (255,12,94), (self.x_center - (100/2)), (self.y_center + 200), 100, 50, "Level 5",13)
        self.levelFiveBtn.draw()
        levelPresenter.buttonList.append(self.levelOneBtn)
        levelPresenter.buttonList.append(self.levelTwoBtn)
        levelPresenter.buttonList.append(self.levelThreeBtn)
        levelPresenter.buttonList.append(self.levelFourBtn)
        levelPresenter.buttonList.append(self.levelFiveBtn)
        print("level has been loaded")


    def checkIfClicked(self, x, y):
        for button in levelPresenter.buttonList:
            if button.clicked((x,y)):
                return(button)


    def handleBtnClick(self, button):
        if button == self.levelOneBtn:
            print("LEVEL 1")
            levelOne = level1(self.win, self.pygame)
            levelOne.runInvestigation()
        elif button == self.levelTwoBtn:
            print("LEVEL 2")
            os.system('python maze.py')
        elif button == self.levelThreeBtn:
            print("LEVEL 3")
        elif button == self.levelFourBtn:
            print("LEVEL 4")
        elif button == self.levelFiveBtn:
            print("LEVEL 5")

            
    
