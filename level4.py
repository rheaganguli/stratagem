import turtle
import math
import random
import os
import sys
from game_constants import const

wn = turtle.Screen()
wn.bgcolor(const.COLOR_WHITE)
wn.bgpic('l4.gif')
wn.update()
wn.setup(const.DIM_700,const.DIM_1000)
wn.tracer(0)

instructionsShown = False 
answerFound = False

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
        self.goto(const.DIM_2000,const.DIM_2000)
        self.hideturtle()

class picTurt(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.y = y
        self.x = x
        self.shape("l4.gif")
        self.penup()
        self.goto(self.x, self.y)
        self.speed(0)
        
class textTurt(turtle.Turtle):
    def __init__(self, text, x, y):
        turtle.Turtle.__init__(self)
        self.y = y
        self.x = x
        self.text = text
        self.penup()
        self.goto(self.x, self.y)
        self.color(const.COLOR_BLACK)
        self.hideturtle()
        self.speed(0)

def printToPlayer(textTurtle):
    print("printToPlayer")
    cover = cleanCoverup(const.POS_500, const.POS_MIN_210)
    filled_rectangle(cover, const.DIM_1000, const.DIM_1000)
    textTurtle.write(textTurtle.text, move=False, align=const.LEFT, font=(const.FONT, 16, const.TEXT_TYPE))

def showPubInfo():
    textTurtle = textTurt(const.PUB_INFO, const.POS_MIN_330, const.POS_350)
    printToPlayer(textTurtle)
    
showPubInfo()

def showInstructions():
    print("moveToNext")
    textTurtle = textTurt(const.LEVEL4_INSTRUCTIONS, const.POS_MIN_250, const.POS_MIN_150)
    printToPlayer(textTurtle)
    wn.update()
    instructionsShown = True

showInstructions()

while not answerFound:
    answer = turtle.textinput("Enter Your Answer Here ", "Enter the PIN code for the phone")
    if answer == const.LEVEL4_ANSWER:
        answerFound = True
        break
    elif answer == None:
        break





    
        
