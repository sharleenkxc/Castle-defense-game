import pygame
import pickle
from FrameWork import *
from setMoney import *

# this is the mode to let users choose the number of waves they want
class CreateWavesMode(PygameGame):
    def init(self):
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        self.nextImage = pygame.transform.scale(pygame.image.load("next.png"),(180,90))
        self.waveImage = pygame.transform.scale(pygame.image.load("wave.png"),(500,200))
        

        self.wave = 'Enter Here'


    def keyPressed(self,keyCode, modifier):
        if keyCode == pygame.K_BACKSPACE and len(self.wave) > 0:
            self.wave = self.wave[:-1]
        elif keyCode == pygame.K_0:
            self.wave += '0'
        elif keyCode == pygame.K_1:
            self.wave += '1'
        elif keyCode == pygame.K_2:
            self.wave += '2'
        elif keyCode == pygame.K_3:
            self.wave += '3'
        elif keyCode == pygame.K_4:
            self.wave += '4'
        elif keyCode == pygame.K_5:
            self.wave += '5'
        elif keyCode == pygame.K_6:
            self.wave += '6'
        elif keyCode == pygame.K_7:
            self.wave += '7'
        elif keyCode == pygame.K_8:
            self.wave += '8'
        elif keyCode == pygame.K_9:
            self.wave += '9'
            

    def mousePressed(self,x,y):
        if self.width-200 <= x <= self.width-200+180 and \
            self.height-100 <= y <= self.height-100 + 90:
            pickle.dump(self.wave,open("numOfWaves.txt","wb"))
            SetMoneyMode().run()

    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.waveImage,(250,200))
        waveFont = pygame.font.SysFont('Arial', 28)
        waveSurface = waveFont.render(self.wave, False, (0,0,0))
        screen.blit(waveSurface,(550,230))
        screen.blit(self.nextImage,(self.width-200,self.height-100))
