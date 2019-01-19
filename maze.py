import turtle
import math
import random
import os
from network import Network
from game_constants import const

wn = turtle.Screen()
wn.bgcolor((0,0,0))
wn.setup(const.DIM_700,const.DIM_900)
wn.tracer(0)

instructionsShown = False 
levels = [""]
shadows = [""]

treasures = []
clues = []
texts = []
enemies = []
shadows = []
#add maze to mazes list


walls = []   

LEVEL2_IMAGES = ["R2.gif", "L6.gif", "R2E.gif", "L5E.gif"]
LEVEL2_CLUEPICS = ["R2.gif", "L6.gif", "R2E.gif", "L5E.gif", "R2.gif"]
LEVEL2_INSTRUCTIONS = "Hidden Maze: Together you must try and find and solve the 5 clues.\nThe clues are scattered around the maze\nHowever, the maze is hidden. Use the arrow keys to move. \nHit 'Enter' when you are ready to begin."

clues_found = []

#X's represent the walls of the maze, P,Q represents player other letters represents the clues
LEVEL2_MAZE = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX          XXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"XR      XX  XXXX       XX",
"XXXXXX  XX  XXXH       XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XX                XXXXXXX",
"XXXXXXXXXXXX     XXXXXA X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXE          XXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XXG         XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

LEVEL2_SHADOWS = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

LEVEL2_CLUE1 = "1. What can fly without wings?"
LEVEL2_CLUE2 = "2. I begin the instruments that open doors, yet I lie in the middle of the sky?"
LEVEL2_CLUE3 = "3. Time when dreams come true?"
LEVEL2_CLUE4 = "4. I form in an instant but I last a lifetime"
LEVEL2_CLUE5 = "5. I am your most powerful weapon; I come before your eyes."

levels.append(LEVEL2_MAZE)


for image in LEVEL2_IMAGES:
    turtle.register_shape(image)

#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(const.SHAPE_SQUARE)
        self.color(const.COLOR_WHITE)
        self.penup()
        self.speed(0)
        self.hideturtle()

    def show(self):
        self.showturtle()

#Creates the squares over the maze so that the maze is hidden from the gamers
class shadowPen(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(const.SHAPE_SQUARE)
        self.color(const.COLOR_RED)
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(const.DIM_2000,const.DIM_2000)
        self.hideturtle()

class Player(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("R2.gif")
        self.color(const.COLOR_BLUE)
        self.penup()
        self.speed(0)
        self.gold = 0
        self.x = x
        self.y = y
        self.hideturtle()

    def show(self):
        self.showturtle()

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("L6.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

 
    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        
        self.shape("R2.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
#Checks to see whether player has collided with a wall of the maze
    def is_collision(self, other):
        a = self.xcor() -other.xcor()
        b = self.ycor() -other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:
            return True
        else:
            return False

class Clue(turtle.Turtle):
    def __init__(self, x, y, clue, y_offset, index):
        turtle.Turtle.__init__(self)
        self.shape(const.SHAPE_CIRCLE)
        self.color(const.COLOR_GREEN)
        self.penup()
        self.speed(0)
        self.index = index
        self.text = clue
        self.y_offset = y_offset
        self.goto(x, y)

    def destroy(self):
        self.goto(const.DIM_2000,const.DIM_2000)
        self.hideturtle()

class textTurt(turtle.Turtle):
    def __init__(self, text, x, y):
        turtle.Turtle.__init__(self)
        self.y = y
        self.x = x
        self.text = text
        self.penup()
        self.goto(self.x, self.y)
        self.color(const.COLOR_WHITE)
        self.hideturtle()
        self.speed(0)

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
        self.shape(const.SHAPE_CIRCLE)
        self.color(const.COLOR_BLACK)
        self.penup()
        self.goto(x, y)
       
    def destroy(self):
        self.goto(const.DIM_2000,const.COLOR_BLACK)
        self.hideturtle()

class Text(turtle.Turtle):
    def __init__(self, y, text):
        turtle.Turtle.__init__(self)
        self.color(const.COLOR_WHITE)
        self.penup()
        self.y = const.POS_MIN_275 - y
        self.goto(const.POS_MIN_264, self.y)
        self.text = text
        self.hideturtle()
        self.write(text, move=False, align=const.LEFT, font=(const.FONT, 16, const.TEXT_TYPE))

def printToPlayer(textTurtle):
    print("printToPlayer")
    cover = cleanCoverup(const.POS_500, const.POS_MIN_210)
    filled_rectangle(cover, const.DIM_1000, const.DIM_1000)
    textTurtle.write(textTurtle.text, move=False, align=const.LEFT, font=(const.FONT, 16, const.TEXT_TYPE))

def showPubInfo():
    textTurtle = textTurt(const.PUB_INFO, const.POS_220, const.POS_MIN_300)
    printToPlayer(textTurtle)

def showInstructions():
    textTurtle = textTurt(LEVEL2_INSTRUCTIONS, const.POS_MIN_250, const.POS_150)
    printToPlayer(textTurtle)
    wn.update()
    instructionsShown = True

def getClueAnswer(clue_list):

    for clue in clue_list:
        answer = turtle.textinput("Enter Your Answer Here: ", "Answer Clue Number " + str(clue.index) + " Here \n" + str(clue.text))

        if clue.index == 1:
            if answer.lower() == "time":
                print("clue 1")
            else:
                getClueAnswer(clue)
        elif clue.index == 2:
            if answer.lower() == "crowbar":
                print("clue 1")
            else:
                getClueAnswer(clue)
        elif clue.index == 3:
            if answer.lower() == "11:11":
                print("clue 1")
            else:
                getClueAnswer(clue)
        elif clue.index == 4:
            if answer.lower() == "memory":
                print("clue 1")
            else:
                getClueAnswer(clue)
        elif clue.index == 5:
            if answer.lower() == "brain":
                print("clue 1")
            else:
                getClueAnswer(clue)



#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get character at each x,y coordinate
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = const.POS_MIN_288 + (x*24)
            screen_y = const.POS_350 - (y*24)

            #check if it is an X representing a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "P":
                player.x = screen_x
                player.y =  screen_y
                player.goto(player.x, player.y)
            if character == "R":
                clue = Clue(screen_x, screen_y, LEVEL2_CLUE1, 0, 1)
                clues.append(clue)
            if character == "H":
                clue = Clue(screen_x, screen_y, LEVEL2_CLUE2, 25, 2)
                clues.append(clue)
            if character == "E":
                clue = Clue(screen_x, screen_y, LEVEL2_CLUE3, 50, 3)
                clues.append(clue)
            if character == "A":
                clue = Clue(screen_x, screen_y, LEVEL2_CLUE4, 75, 4)
                clues.append(clue)
            if character == "G":
                clue = Clue(screen_x, screen_y, LEVEL2_CLUE5, 100, 5)
                clues.append(clue)
            
def setup_shadow(shadow):
    for y in range(len(shadow)):
        for x in range(len(shadow[y])):
            #get character at each x,y coordinate
            character = shadow[y][x]
            #calculate the screen x,y coordinates
            screen_x = const.POS_MIN_288 + (x*24)
            screen_y = const.POS_350 - (y*24)

            #check if it is an X representing a wall
            if character == "X":
                shadowTurtle = shadowPen(screen_x, screen_y)
                shadows.append(shadowTurtle)

def loadMaze():
    if not instructionsShown:
        cover = cleanCoverup(const.POS_500, const.POS_500)
        filled_rectangle(cover, const.DIM_1000, const.DIM_1000)
        global pen, player, player2
        #create class instances
        pen = Pen()
        player = Player(0,0)
        setup_maze(levels[1])
        #setup_shadow(LEVEL2_SHADOWS)
        player.show()
        pen.show()
        turtle.onkey(player.go_left, const.KEY_LEFT)
        turtle.onkey(player.go_right, const.KEY_RIGHT)
        turtle.onkey(player.go_up, const.KEY_UP)
        turtle.onkey(player.go_down, const.KEY_DOWN)
        showPubInfo()

        #Main Game Loop
        while True:
            for shadowTurtle in shadows:
                if player.is_collision(shadowTurtle):
                    shadowTurtle.destroy()
                    shadows.remove(shadowTurtle)

            for clue in clues:
                if player.is_collision(clue):
                    clues_found.append(clue)
                    text = Text(clue.y_offset, clue.text)
                    texts.append(text)
                    clue.destroy()
                    if len(clues_found) > 4:
                        getClueAnswer(clues_found)   
                    clues.remove(clue)
          
            wn.update()         


showInstructions()



turtle.listen()
turtle.onkey(loadMaze, const.KEY_RETURN)

wn.tracer(0)
wn.mainloop()
