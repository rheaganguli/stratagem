
from button import button

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


                      
    def present(self):
        self.win.blit(self.bgPicture,(0,0))

        self.win.blit(self.questions[0], (250, 645))
        self.win.blit(self.questions[1], (250, 645))
        self.win.blit(self.questions[2], (250, 645))
        self.win.blit(self.questions[3], (250, 645))
        self.win.blit(self.questions[4], (250, 645))
        self.win.blit(self.questions[5], (250, 645))
        self.win.blit(self.questions[6], (250, 645))

        self.askQuestion(0)
        self.askQuestion(1)
        self.askQuestion(2)
        self.askQuestion(3)
        self.askQuestion(4)
        self.askQuestion(5)
        self.askQuestion(6)
##
##    def askQuestion(self, questionNumber):
##        #ask the question from the list
##        #and blit it here
##        print(self.dummyQuests[questionNumber])
##        ansInput = 'a'
## #       ansInput = input("Make your Choice! ")
##        self.checkForAnswer(questionNumber, ansInput)
##            
##
##    def checkForAnswer(self, questionNumber, ansChoice):
##        if ansChoice == 'a':
##            print(ansChoice)
##        else:
##            print("Have a good time in jail ")

class Question:
    def __init_-(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "b"),
]

def run_investigation(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print(score)

        
        
