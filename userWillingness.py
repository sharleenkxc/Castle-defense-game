import pygame
import pickle
from FrameWork import *
from savedMapMode import *

# this mode asks user whether they want to include their self-created enemy in their self-created map
class AskWillingnessMode(PygameGame):
    def init(self):
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        self.askImage = pygame.transform.scale(pygame.image.load("askWillingness.png"),(600,140))
        # yes and no icon are made with powerpoint
        self.yesImage = pygame.transform.scale(pygame.image.load("yes.png"),(100,100))
        self.noImage = pygame.transform.scale(pygame.image.load("no.png"),(100,100))


    def mousePressed(self,x,y):
        if 300 <= x <= 400 and 400 <= y <= 500:
            pickle.dump("yes",open("willingness.txt","wb"))
            SavedMapMode().run()
        elif 600 <= x <= 700 and 400 <= y <= 500:
            pickle.dump("no",open("willingness.txt","wb"))
            SavedMapMode().run()

    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.askImage,(200,200))
        screen.blit(self.yesImage,(300,400))
        screen.blit(self.noImage,(600,400))

