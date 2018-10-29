import pygame
from button import button

class menuPresenter(object):

    buttonList = []
    
    def __init__(self, pygame, win):
        print("Menu presenter started")
        self.pygame = pygame
        self.win = win
        w, h = pygame.display.get_surface().get_size()
        print(w,h)
        self.x_center = w/2
        self.y_center = h/2
        self.playBtn = None
        self.optionsBtn = None
        self.exitBtn = None

    def present(self):
       self.playBtn = button(self.pygame, self.win, (0,0,255), (self.x_center - (200/2)), (self.y_center - (75/2 + 50 + 32.5)), 200, 75, "Play Game")
       self.playBtn.draw()
       self.optionsBtn = button(self.pygame, self.win, (255,255,0), (self.x_center - (150/2)) , (self.y_center - (50/2)) , 150, 50, "Options")
       self.optionsBtn.draw()
       self.exitBtn = button(self.pygame, self.win, (0,255,0), (self.x_center - (100/2)), (self.y_center - (50/2 - 50 - 25)), 100, 50, "Exit Game")
       self.exitBtn.draw()
       menuPresenter.buttonList.append(self.playBtn)
       menuPresenter.buttonList.append(self.optionsBtn)
       menuPresenter.buttonList.append(self.exitBtn)

    def checkIfClicked(self, x, y):
        for button in menuPresenter.buttonList:
            if button.clicked((x,y)):
                return(button)

    def handleBtnClick(self, button):
        if button == self.playBtn:
            print("Game is ready to be played")
        elif button == self.optionsBtn:
            print("Here are the various options")
        elif button == self.exitBtn:
            print("You have exited the game")
        
    


