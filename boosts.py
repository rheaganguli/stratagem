class boosts(object):
    def __init__(self,x,y,radius,color,boostType,text,duration):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.boostType = boostType
        self.text = text
        self.duration = duration

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
