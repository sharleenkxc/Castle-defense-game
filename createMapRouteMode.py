import pygame
import pickle
from FrameWork import *
from placeObstaclesMode import *

# this is the mode for user to build their own route

class CreateMapRouteMode(PygameGame):
    def init(self):
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        self.nextImage = pygame.transform.scale(pygame.image.load("next.png"),(180,90))
        self.instructionImage = pygame.transform.scale(pygame.image.load("routeInstruction.png"),(700,110))
        # grid based
        self.size = 50
        self.rows = self.height//self.size
        self.cols = self.width//self.size

        self.route = []
        self.errorImage = None
        self.timerCount = 0

    def timerFired(self,dt):
        self.timerCount += 1
        if self.timerCount % 45 == 0:
            self.errorImage = None
    
    def mousePressed(self,x,y):
        if self.width-200 <= x <= self.width-200+180 and \
            self.height-100 <= y <= self.height-100 + 90:
            PlaceObstaclesMode().run()
        else:
            if (y//self.size,x//self.size) in self.route:
                self.route.remove((y//self.size,x//self.size))
                pickle.dump(self.route,open("selfCreatedMapRoute.txt","wb"))
            else:
                if self.route != []:
                    lastRow,lastCol = self.route[-1]
                    if (y//self.size == lastRow and abs(lastCol - x//self.size) == 1) or\
                        (x//self.size == lastCol and abs(lastRow - y//self.size) == 1):
                        self.route.append((y//self.size,x//self.size))
                        pickle.dump(self.route,open("selfCreatedMapRoute.txt","wb"))
                    else:
                        self.errorImage = pygame.transform.scale(pygame.image.load("routeError.png"),(300,300))


                else:
                    self.route.append((y//self.size,x//self.size))
                    pickle.dump(self.route,open("selfCreatedMapRoute.txt","wb"))
                


    
    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        for row in range(self.rows):
            for col in range(self.cols):
                (x0, y0) = (col*self.size,row*self.size)
                pygame.draw.rect(screen,(0,0,0),(x0,y0,self.size,self.size),1)
                if (row,col) in self.route:
                    pygame.draw.rect(screen,(0,0,0),(x0,y0,self.size,self.size))
        screen.blit(self.nextImage,(self.width-200,self.height-100))
        screen.blit(self.instructionImage,(150,0))
        if self.errorImage != None:
            screen.blit(self.errorImage,(350,250))


