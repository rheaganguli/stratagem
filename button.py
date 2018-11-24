#Code for the button class
class button():
    def __init__(self, pygame, win, colour, x, y, width, height, text):
        self.pygame = pygame
        self.win = win
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
#Every button has a 'draw' function which draws a rectangle
    def draw(self):
        self.pygame.draw.rect(self.win, self.colour, (self.x,self.y,self.width,self.height))
        

#Code which enables the 'click' function which checks whether the x & y co-ordinates
#of the mouse click are within that of the button
    def clicked(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if (pos[0] > self.x) and (pos[0] < self.x + self.width):
            if (pos[1] > self.y) and (pos[1] < self.y + self.height):
                print(self.text + ' button Clicked')
                return True        
        else:
            return False

