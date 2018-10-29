class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 6
        self.health = 10
        self.visible = True

    def draw(self,win):

    def hit(self, value):
        if self.health > 0:
            self.health -= value
        else:
            self.visible = False
        print('hit')

    def move(self):
