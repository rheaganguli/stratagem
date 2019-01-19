import turtle
import math
import random
import os
import sys
from game_constants import const



wn = turtle.Screen()
wn.bgcolor(const.COLOR_WHITE)
wn.addshape("investigation.gif")
wn.update()
wn.setup(const.DIM_1000,const.DIM_1000)
wn.tracer(0)

questions = []

CURR_NUMB = 0
Y_OFFSET = 0
SPACE = 24
instructionsShown = False 

def filled_rectangle(t, l, w):
    t.begin_fill()
    for i in range(2):
            t.right(90)
            t.forward(l)
            t.right(90)
            t.forward(w)
    t.end_fill()

#covers previous question in order to paste new one over it
class cleanCoverup(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(const.SHAPE_SQUARE)
        self.color(const.COLOR_WHITE)
        self.penup()
        self.goto(x, y)
       
    def destroy(self):
        self.goto(const.DIM_2000, const.DIM_2000)
        self.hideturtle()

class picTurt(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.y = y
        self.x = x
        self.shape("investigation.gif")
        self.penup()
        self.goto(self.x, self.y)
        self.speed(0)

#Function which draws on the text that is displayed during the program
class textTurt(turtle.Turtle):
    def __init__(self, text, x, y):
        turtle.Turtle.__init__(self)
        self.y = y
        self.x = x
        self.text = text
        self.penup()
        self.goto(self.x, self.y)
        self.color(const.COLOR_BLACK)
        self.speed(0)


for i in range(len(const.LEVEL1_QUESTIONS)):
    quest = const.LEVEL1_QUESTIONS[i]
    question = textTurt(quest, const.POS_MIN_150, const.POS_MIN_320)
    questions.append(question)


def printToPlayer(textTurtle):
    print("printToPlayer")
    cover = cleanCoverup(const.POS_500, const.POS_MIN_210)
    filled_rectangle(cover, const.DIM_1000, const.DIM_1000)
    textTurtle.write(textTurtle.text, move=False, align=const.LEFT, font=(const.FONT, 16, const.TEXT_TYPE))


def showInstructions():
    print("moveToNext")
    textTurtle = textTurt(const.LEVEL1_INSTRUCTIONS, const.POS_MIN_350, const.POS_MIN_150)
    printToPlayer(textTurtle)
    instructionsShown = True
    
def LoadQuestions():
    cover = cleanCoverup(const.POS_500, const.POS_500)
    filled_rectangle(cover, const.DIM_1000,const.DIM_1000)
    pic = picTurt(const.POS_0, const.POS_0)
    wn.update()
    askQuestion(CURR_NUMB)

def showPubInfo():
    textTurtle = textTurt(const.PUB_INFO, const.POS_MIN_490, const.POS_350)
    printToPlayer(textTurtle)
    
showPubInfo()

def checkForAnswer(questionNumber):
    answer = turtle.textinput("Enter Your Answer Here: ", "Answer Question Number " + str(CURR_NUMB+1) + " Here")

    if answer == None:
        return False

    userInput = answer.lower()
    if questionNumber == 0:
        if userInput == "c":
            print(userInput)
            return True
        else:
            return False
    elif questionNumber == 1:
        if userInput == "b":
            print(userInput)
            return True
        else:
            return False
    elif questionNumber == 2:
        if userInput == "b":
            print(userInput)
            return True
        else:
            return False
    elif questionNumber == 3:
        if userInput == "a":
            print(userInput)
            return True
        else:
            return False
    elif questionNumber == 4:
        if userInput == "c":
            print(userInput)
            return True
        else:
            return False
    elif questionNumber == 5:
        if userInput == "c":
            print(userInput)
            return True
        else:
            return False
    elif questionNumber == 6:
        if userInput == "b":
            print(userInput)
            return True
        else:
            return False

def askQuestion(numb):
    global CURR_NUMB
    printToPlayer(questions[numb])

    correct = checkForAnswer(numb)

    if numb > 5:
        const.CURRENT_LEVEL = const.CURRENT_LEVEL + 1

    if correct:
        textTurtle = textTurt("Excellent Work", const.POS_MIN_150, const.POS_MIN_350)   
        printToPlayer(textTurtle)
        numb = numb + 1
        CURR_NUMB = CURR_NUMB + 1
        askQuestion(numb)
    else:
        textTurtle = textTurt("You're definitely going to jail", const.POS_MIN_150, const.POS_MIN_350)
        printToPlayer(textTurtle)
        sys.exit("Player Lost")

showInstructions()

turtle.listen()
turtle.onkey(LoadQuestions, const.KEY_RIGHT)
turtle.mainloop()
        
 
    
    
