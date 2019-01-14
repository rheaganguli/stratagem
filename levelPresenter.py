import pygame
from button import button
import os



#Class for the level menu
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
        
        levelPresenter.buttonList.append(self.levelOneBtn)
        levelPresenter.buttonList.append(self.levelTwoBtn)
        levelPresenter.buttonList.append(self.levelThreeBtn)
        levelPresenter.buttonList.append(self.levelFourBtn)
        
        print("level has been loaded")

#This function is responsible for matching the x & y co-ordinates of the mouse click to those of the button
    def checkIfClicked(self, x, y):
        for button in levelPresenter.buttonList:
            if button.clicked((x,y)):
                return(button)

#Takes the user to the respective screen depending on which button has been clicked
    def handleBtnClick(self, button):
        if button == self.levelOneBtn:
            print("LEVEL 1")
            import level1
        elif button == self.levelTwoBtn:
            print("LEVEL 2")
            os.system("python3 server.py")
            os.system('python3 maze.py')
        elif button == self.levelThreeBtn:
            print("LEVEL 3")
            os.system("python3 level1.py")
        elif button == self.levelFourBtn:
            print("LEVEL 4")
            os.system("python3 level4.py")
    
        
