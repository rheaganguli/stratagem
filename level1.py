
from button import button
import time

class level1(object):

    def __init__(self, win, pygame):
        self.pygame = pygame
        self.win = self.pygame.display.set_mode((1000,695))
        self.pygame.display.set_caption("LEVEL1")

        #contains original sized images
        self.quests = [self.pygame.image.load('q_1.png'), self.pygame.image.load('q_2.png'), self.pygame.image.load('q_3.png'), self.pygame.image.load('q_4.png'), self.pygame.image.load('q_5.png'), self.pygame.image.load('q_6.png'), self.pygame.image.load('q_7.png')]

        #will contain the resized images
        self.questions = []

        self.dummyQuests = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7']

        for question in self.quests:
            question = self.pygame.transform.scale(question, (500, 40))
            self.questions.append(question)

        self.bg = self.pygame.image.load('investigation.png')
        self.bgPicture = self.pygame.transform.scale(self.bg, (1000, 695))
        self.win.blit(self.bgPicture,(0,0))


                      
    def runInvestigation(self):
        questionAvailable = True
        for i in range(len(self.questions)):
            print(i)
            self.askQuestion(i)
            answer = self.checkForAnswer(i)
            if not answer:
                print("reducing i by one")
                i = i-1
                print(i)
            

    def askQuestion(self, questionNumber):
        self.win.fill((0,0,0))
        self.win.blit(self.bgPicture,(0,0))
        self.win.blit(self.questions[questionNumber], (250, 645))
            

    def checkForAnswer(self, questionNumber):
 #       userInput = input("Please enter the answer...")
         userInput = "a"
##        print("question Number" + str(questionNumber))
##        if questionNumber == 0:
##            if userInput == "a":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        elif questionNumber == 1:
##            if userInput == "b":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        elif questionNumber == 2:
##            if userInput == "a":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        elif questionNumber == 3:
##            if userInput == "a":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        elif questionNumber == 4:
##            if userInput == "a":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        elif questionNumber == 5:
##            if userInput == "a":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        elif questionNumber == 6:
##            if userInput == "a":
##                print(userInput)
##                return True
##            else:
##                print("say something")
##                return False
##        
##            
##     
##        
##        
##        
