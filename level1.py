import turtle
import math
import random
import os
import sys


wn = turtle.Screen()

questions = []

instToShow = "Katy is an aspiring journalist in New York who lives with boyfriend Rick Parker. \n One day she receives an anonymous tip regarding a drug deal in Providence (her home town). \nKaty & Rick spoke about the case and Rick expresses his reservations \nagainst the case as he has prior experience with illegal activities and knows that they can be dangerous.\n\nNonetheless, he was supportive of her decision and they said goodbye. \nImmediately, she travels to Providence where she reunites with her childhood friends \nEthan, Cosima & Tristan \n(a credible detective in the area).\n\nKaty investigates the case further whilst in Providence, spending time with her friends. \nFor Cosima’s 25th birthday party, Rick flies down and they are reunited. During the party, \nRick & Katy are seen having a heated argument when Katy storms off and leaves the party.\n\nThe next morning, Katy is found dead at home. Rick is called in for questioning by Tristan \nwhere he then admits to having the fight regarding her involvement in this dangerous case. \nTristan then tells Rick that he has one week before trial to prove his innocence.\n\n\n Use this information to answer the questions.\n\n Click the right key when you are ready."

listOfQuests = [
    "What is your relationship with Katy Manning? \n (A):My sister \n (B):My childhood friend \n (C):My girlfriend",
    "Why were you in Providence? \n (A):Visiting My Family \n (B):Attending Katy’s friend Cosima’s birthday party \n (C):High School Reunion",
    "What was the argument about last night? \n (A):Meeting my parents for Christmas \n (B):Her story that she's working on \n (C):She saw me talking to another girl",
    "Why were you not supportive of her work?\n (A):My experience with illegal activities proves it dangerous \n (B):Took a lot of time away from our relationship \n (C):She wanted me to move to Providence",
    "What case was she working on whilst in Providence? \n (A):An investigation within local authorities \n (B):An investigation about a potential murder \n (C):An investigation about a drug cartel",
    "Where were you the night she was killed? \n (A):At home with my sister \n (B):At a restaurant with my friend Steve \n (C):At Cosima’s house helping her clean up after the party",
    "Were you responsible for the death of Katy Manning?\n (A):Yes \n (B): No \n (C): I don't know"
    ]

currentNumb = 0
y_offset = 0
space = 24
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
        self.color("black")
        self.speed(0)


for i in range(len(listOfQuests)):
    quest = listOfQuests[i]
    question = textTurt(quest, -150, -320)
    questions.append(question)



def printToPlayer(textTurtle):
    print("printToPlayer")
    cover = cleanCoverup(500, -210)
    filled_rectangle(cover, 1000, 1000)
    textTurtle.write(textTurtle.text, move=False, align="left", font=("Comic Sans MS", 16, "normal"))


def showInstructions():
    print("moveToNext")
    textTurtle = textTurt(instToShow, -350, -150)
    printToPlayer(textTurtle)
    instructionsShown = True
    

def LoadQuestions():
    cover = cleanCoverup(500, 500)
    filled_rectangle(cover, 1000, 1000)
    pic = picTurt(0, 0)
    wn.update()
    askQuestion(currentNumb)

def showPubInfo():
    textTurtle = textTurt("STRATEGEM \n23/07/2019", -490, 350)
    printToPlayer(textTurtle)
    
showPubInfo()

def checkForAnswer(questionNumber):
    answer = turtle.textinput("Enter Your Answer Here: ", "Answer Question Number " + str(currentNumb+1) + " Here")

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

    printToPlayer(questions[numb])

    correct = checkForAnswer(numb)

    if correct:
        textTurtle = textTurt("Excellent Work", -150, -350)
        printToPlayer(textTurtle)
        numb = numb + 1
        askQuestion(numb)
    else:
        textTurtle = textTurt("You're definitely going to jail", -150, -350)
        printToPlayer(textTurtle)
        sys.exit("Player Lost")

def main():
    wn.bgcolor("white")
    wn.addshape("investigation.gif")
    wn.update()
    wn.setup(1000,1000)
    wn.tracer(0)
    showInstructions()
    turtle.listen()
    turtle.onkey(LoadQuestions, "Right")



if __name__ == "__main__":
    main()
    wn.mainloop()
        
 
    
    
