import turtle
import math
import random
import os

wn = turtle.Screen()
wn.bgcolor((0,0,0))
wn.setup(700,900)
wn.tracer(0)

print('stage 1')
images = ["R2.gif", "L6.gif", "R2E.gif", "L5E.gif"]

cluePics = ["my_tweet.gif", 'clue_2.gif']

for image in images:
    turtle.register_shape(image)
#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Creates the squares over the maze so that the maze is hidden from the gamers
class shadowPen(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        print("I'm hiding the turtle")
        self.hideturtle()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("R2.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

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


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


class Clue(turtle.Turtle):
    def __init__(self, x, y, clue):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.clue = cluePics[clue]
        self.goto(x, y)
        self.x = x
        self.y = y
        

    def showClue(self):
        self.shape(self.clue)
        self.goto(self.x, self.y - 600)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
 
print('stage 2')       
levels = [""]
shadows = [""]
#X's represent the walls of the maze, P represents player and T represents the clues
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXE         XXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"XC      XX  XXXT      EXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXXT  XXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XT                XXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXXT        X",
"XXXE                    X",
"XXXT         XXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXXT             X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX          XXXXT       X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

shadow = [
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

treasures = []
clues = []
enemies = []
shadows = []
#add maze to mazes list
levels.append(level_1)

print('stage 3')
os.system('python3 server.py')

#create class instances
pen = Pen()
player = Player()

walls = []            


#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get character at each x,y coordinate
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = -288 + (x*24)
            screen_y = 350 - (y*24)

            #check if it is an X representing a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "T":
                treasure = Treasure(screen_x, screen_y)
                treasures.append(treasure)
            if character == "C":
                clue = Clue(screen_x, screen_y, 0)
                clues.append(clue)

def setup_shadow(shadow):
    for y in range(len(shadow)):
        for x in range(len(shadow[y])):
            #get character at each x,y coordinate
            character = shadow[y][x]
            #calculate the screen x,y coordinates
            screen_x = -288 + (x*24)
            screen_y = 350 - (y*24)

            #check if it is an X representing a wall
            if character == "X":
                shadowTurtle = shadowPen(screen_x, screen_y)
                shadows.append(shadowTurtle)


        
print('stage 4')

#set up the level

setup_maze(levels[1])
#setup_shadow(shadow)
#print (walls)


turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)

print('Running client')
os.system('python3 client.py')

print('stage 5')
#Main Game Loop
while True:

    for treasure in treasures:
        if player.is_collision(treasure):
            #Adds treasure gold to player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for shadowTurtle in shadows:
        if player.is_collision(shadowTurtle):
            print("I'm checking for shadow")
            shadowTurtle.destroy()
            shadows.remove(shadowTurtle)

    for clue in clues:
        if player.is_collision(clue):
            print("Clue found")
            clue.showClue()

    
    wn.update()


print('stage 6')
