import turtle
import math
import random
import os
import sys

wn = turtle.Screen()
wn.bgcolor("black")
wn.update()
wn.setup(1000,700)
wn.tracer(0)

questions = []

instToShow = "Katy is an aspiring journalist in New York lives with boyfriend Rick Parker. \n One day receives an anonymous tip regarding a drug deal in Providence (her home town). \n Travels to Providence, meets her childhood friends Ethan, Cosima & Tristan \n(a credible detective in the area). Katy & Rick spoke about the case and Rick has reservations \nagainst the case as he has an idea of the cartels operating in Providence. Nonetheless, \nhe was supportive of her decision and they said goodbye. \n\nShe investigates the case further whilst in Providence, spending time with her friends. \nFor Cosima’s 25th birthday party, Rick flies down and they are reunited. During the party, \nRick & Katy are seen having a heated argument when Katy storms off and leaves the party.\n\nThe next morning, Katy is found dead at home. Rick is called in for questioning by Tristan \nwhere he then admits to having the fight regarding her involvement in this dangerous case. \nTristan then tells Rick that he has one week before trial to prove his innocence.\n"

def filled_rectangle(t, l, w):
    t.begin_fill()
    for i in range(2):
            t.right(90)
            t.forward(l)
            t.right(90)
            t.forward(w)
    t.end_fill()

class cleanCoverup(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.goto(500, -210)
       
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()    

class textTurt(turtle.Turtle):
    def __init__(self, text):
        turtle.Turtle.__init__(self)
        self.y = -150
        self.x = -350
        self.text = text
        self.penup()
        self.goto(self.x, self.y)
        self.color("white")
        self.speed(0)


#Function which draws on the text that is displayed during the program
def printToPlayer(textTurtle):
    print("printToPlayer")
    cover = cleanCoverup()
    filled_rectangle(cover, 1000, 1000)

    textTurtle.write(textTurtle.text, move=False, align="left", font=("Comic Sans MS", 16, "normal"))

def loadLevel():
    print("Loading level 1")
    os.system("python level1.py")








turtle.listen()
turtle.onkey(loadLevel, "Left")

wn.mainloop()

    
        
 
    
    
