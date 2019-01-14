import turtle
import math
import random
import os
import sys

wn = turtle.Screen()
wn.bgcolor("white")
wn.bgpic('l4.gif')
wn.update()
wn.setup(700,1000)
wn.tracer(0)

instToShow = "Assuming O = 4, find the numeric value which corresponds to 'HEART'"

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
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
       
    def destroy(self):
        self.goto(2000,2000)
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
        self.color("black")
        self.hideturtle()
        self.speed(0)

def printToPlayer(textTurtle):
    print("printToPlayer")
    cover = cleanCoverup(500, -210)
    filled_rectangle(cover, 1000, 1000)
    textTurtle.write(textTurtle.text, move=False, align="left", font=("Comic Sans MS", 16, "normal"))

def showPubInfo():
    textTurtle = textTurt("STRATEGEM \n23/07/2019", -330, 350)
    printToPlayer(textTurtle)
    
showPubInfo()

def showInstructions():
    print("moveToNext")
    textTurtle = textTurt(instToShow, -250, 150)
    printToPlayer(textTurtle)
    wn.update()
    instructionsShown = True


showInstructions()

while not answerFound:
    answer = turtle.textinput("Enter Your Answer Here ", "Enter the PIN code for the phone")
    if answer == "10368":
        answerFound = True
        break
    elif answer == None:
        break





    
        
