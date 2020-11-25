import pygame
import pickle
from FrameWork import *
from createWaves import *

# this is the mode allow users to place obstacles

class PlaceObstaclesMode(PygameGame):
    def init(self):
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        self.nextImage = pygame.transform.scale(pygame.image.load("next.png"),(180,90))
        self.instructionImage = pygame.transform.scale(pygame.image.load("obstacleInstruction.png"),(700,110))

        
        # grid based
        self.size = 50
        self.rows = self.height//self.size
        self.cols = self.width//self.size

        self.obstaclePositions = []
        self.route = pickle.load(open("selfCreatedMapRoute.txt","rb"))
        self.error = None
        self.timerCount = 0

    def timerFired(self,dt):
        self.timerCount += 1
        if self.timerCount % 45 == 0:
            self.error = None

    def mousePressed(self,x,y):     
        if (self.width-200 <= x <= self.width-200+180 and \
            self.height-100 <= y <= self.height-100 + 90):
            if len(self.obstaclePositions) >= 10:
                CreateWavesMode().run()
            else:
                self.error = pygame.transform.scale(pygame.image.load("obstacleError.png"),(300,300))
        else:
            if ((x//self.size)*self.size,(y//self.size)*self.size) in self.obstaclePositions:
                self.obstaclePositions.remove(((x//self.size)*self.size,(y//self.size)*self.size))
                pickle.dump(self.obstaclePositions,open("createdObstacles.txt","wb"))
            elif not (y//self.size,x//self.size) in self.route:
                self.obstaclePositions.append(((x//self.size)*self.size,(y//self.size)*self.size))
                pickle.dump(self.obstaclePositions,open("createdObstacles.txt","wb"))

            
        

    
    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        for row in range(self.rows):
            for col in range(self.cols):
                (x0, y0) = (col*self.size,row*self.size)
                pygame.draw.rect(screen,(0,0,0),(x0,y0,self.size,self.size),1)
                if (row,col) in self.route:
                    pygame.draw.rect(screen,(0,0,0),(x0,y0,self.size,self.size))
                if (col*self.size,row*self.size) in self.obstaclePositions:
                    # rock image taken from  https://www.cleanpng.com/free/cartoon-rock.html
                    screen.blit(pygame.transform.scale(pygame.image.load("obstacleRock.png"),\
                        (50,50)),(col*self.size,row*self.size))
        screen.blit(self.nextImage,(self.width-200,self.height-100))
        screen.blit(self.instructionImage,(150,0))
        if self.error != None:
            screen.blit(self.error,(350,250))