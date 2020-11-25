import pygame
import pickle
from FrameWork import *
from savedMapMode import *
from userWillingness import *

# this mode allows user to choose their amount of money to start with

class SetMoneyMode(PygameGame):
    def init(self):
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        self.nextImage = pygame.transform.scale(pygame.image.load("next.png"),(180,90))
        self.moneyImage = pygame.transform.scale(pygame.image.load("setMoney.png"),(500,200))

        self.money = 'Enter Here'


    def keyPressed(self,keyCode, modifier):
        if keyCode == pygame.K_BACKSPACE and len(self.money) > 0:
            self.money = self.money[:-1]
        elif keyCode == pygame.K_0:
            self.money += '0'
        elif keyCode == pygame.K_1:
            self.money += '1'
        elif keyCode == pygame.K_2:
            self.money += '2'
        elif keyCode == pygame.K_3:
            self.money += '3'
        elif keyCode == pygame.K_4:
            self.money += '4'
        elif keyCode == pygame.K_5:
            self.money += '5'
        elif keyCode == pygame.K_6:
            self.money += '6'
        elif keyCode == pygame.K_7:
            self.money += '7'
        elif keyCode == pygame.K_8:
            self.money += '8'
        elif keyCode == pygame.K_9:
            self.money += '9'

            

    def mousePressed(self,x,y):
        if self.width-200 <= x <= self.width-200+180 and \
            self.height-100 <= y <= self.height-100 + 90:
            pickle.dump(self.money,open("startMoney.txt","wb"))
            
            self.parameters = pickle.load(open("createMonster.txt","rb"))
            if ("step" in self.parameters) and ("life" in self.parameters) and \
                ("value" in self.parameters):
                AskWillingnessMode().run()
            else:
                SavedMapMode().run()

    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.moneyImage,(250,200))
        moneyFont = pygame.font.SysFont('Arial', 28)
        moneySurface = moneyFont.render(self.money, False, (0,0,0))
        screen.blit(moneySurface,(550,230))
        screen.blit(self.nextImage,(self.width-200,self.height-100))
