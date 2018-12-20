#Code for the button class
class button():
    def __init__(self, pygame, win, colour, x, y, width, height, text, size):
        self.pygame = pygame
        self.win = win
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size


    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()
        
#Every button has a 'draw' function which draws a rectangle
    def draw(self):
        self.pygame.draw.rect(self.win, self.colour, (self.x,self.y,self.width,self.height))

        smallText = self.pygame.font.Font("freesansbold.ttf", int(self.size))
        textSurface, textRect = self.text_objects(self.text, smallText)

        text_x = self.x + self.width/2
        text_y = self.y + self.height/2
        textRect.center = ((text_x,text_y))

        self.win.blit(textSurface, textRect)
        

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

