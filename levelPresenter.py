import pygame
bg = pygame.image.load('bg.jpg')

class levelPresenter(object):
    
    def __init__(self, pygame, win):
        self.pygame = pygame
        self.win = win                     
        print('something')
        
        
    def present(self):
        self.win.fill((0,0,0))
        self.win.blit(bg, (0,0))
        print("level has been loaded")

            
