import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor((0,0,0))
wn.setup(700,700)
wn.tracer(0)

images = ["R2.gif", "L6.gif", "R2E.gif", "L5E.gif"]  

for image in images:
    turtle.register_shape(image)
#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("white")
        self.penup()
        self.speed(0)

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

    def is_collision(self, other):
        a = self.xcor() -other.xcor()
        b = self.ycor() -other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:
            return True
        else:
            return False

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("L5E.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("L5E.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("R2E.gif")
        else:
            dx = 0
            dy = 0

        #check if player is close so you can follow him

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
#calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
#check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])
#set time to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))
    def is_close(self, other):
        a = self.xcor() -other.xcor()
        b = self.ycor() -other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
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
 
        
levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXE          XXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXXT      EXX",
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
"XXXE                     X",
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

treasures = []
enemies = []
#add maze to mazes list
levels.append(level_1)

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
            screen_y = 288 - (y*24)

            
            
            #check if it is an X representing a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("triangle")
                pen.stamp()
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "T":
                treasure = Treasure(screen_x, screen_y)
                treasures.append(treasure)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))


#set up the level
setup_maze(levels[1])
print (walls)

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)

#start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250) 

#Main Game Loop
while True:

    for treasure in treasures:
        if player.is_collision(treasure):
            #Adds treasure gold to player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

#checks if player collides with enemy
    for enemy in enemies:
        if player.is_collision(enemy):
            print("You Lose!")
    wn.update()

    
