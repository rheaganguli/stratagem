#Menu Presenter imports the button object from the button file
from button import button
from levelPresenter import levelPresenter

#The Menu Presenter object is responsible for the 'Main Menu'
class menuPresenter(object):
    
    buttonList = []
    
    def __init__(self, pygame, win, gameManager):
        print("Menu presenter started") 
        self.pygame = pygame
        self.win = win
        self.gameManager = gameManager
        w, h = pygame.display.get_surface().get_size()
   #     self.buttonSound = pygame.mixer.Sound('ricochet.wav')
        print(w,h)
        self.x_center = w/2
        self.y_center = h/2
        self.playBtn = None
        self.optionsBtn = None
        self.exitBtn = None

#The 'present' function draws each of the buttons for the various options 
    def present(self):
       print("Menu Pesenter Present")
       self.win.fill((0,0,0))
       self.playBtn = button(self.pygame, self.win, (255,51,51), (self.x_center - (200/2)), (self.y_center - (75/2 + 50 + 32.5)), 200, 75, "Play Game", 20)
       self.playBtn.draw()
       self.instructionsBtn = button(self.pygame, self.win, (255,153,51), (self.x_center - (150/2)) , (self.y_center - (50/2)) , 150, 50, "Instructions", 16)
       self.instructionsBtn.draw()
       self.exitBtn = button(self.pygame, self.win, (255,153,51), (self.x_center - (100/2)), (self.y_center - (50/2 - 50 - 25)), 100, 50, "Exit Game", 12)
       self.exitBtn.draw()
       menuPresenter.buttonList.append(self.playBtn)
       menuPresenter.buttonList.append(self.optionsBtn)
       menuPresenter.buttonList.append(self.exitBtn)

#This function is a check to see whether any of the buttons have been clicked"
    def checkIfClicked(self, x, y):
        for button in menuPresenter.buttonList:
            if button.clicked((x,y)):
                return(button)

#This function is responsilbe for handling what happens when the button is clicked
    def handleBtnClick(self, button):
        if button == self.playBtn:
            print("Game is ready to be played")
 #           self.buttonSound.play()
            levelHandler = levelPresenter(self.pygame, self.win, self.gameManager)
            levelHandler.present()
            self.gameManager.levelPresenterActive = True
            self.gameManager.levelPresenter = levelHandler
        elif button == self.instructionsBtn:
            print("Here are the instructions for the game")
            self.buttonSound.play()
        elif button == self.exitBtn:
            print("You have exited the game")
            self.buttonSound.play()
        
    

