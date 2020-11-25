import pygame
from FrameWork import *

from map1 import *
from map2 import *
from createMapRouteMode import *

import pickle

# This is the instruction screen mode, splash screen mode and create enemy mode
# also includes the inserter class to take user input

# instruction screen - instructions to be added later
# background image taken from: 
# https://photos.com/featured/cartoon-desert-landscape-in-flat-design-vector-illustration-ekaterina-vakhrameeva.html?product=art-print
class InstructionScreenMode(PygameGame):
    def init(self):
        self.counter = 0
        # images used in the instruction images are all taken from game images which are all previously cited
        self.instruction = [pygame.transform.scale(pygame.image.\
            load(f"instruction ({i}).png"),(self.width,self.height)) for i in range(1,6)]   
    
    def keyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_SPACE:
            SplashScreenMode().run()
        elif keyCode == pygame.K_RIGHT and self.counter < 4:
            self.counter += 1
        elif keyCode == pygame.K_LEFT and self.counter > 0:
            self.counter -= 1

    def redrawAll(self,screen):
        instruction = self.instruction[self.counter]
        screen.blit(instruction,(0,0))


# instruction image taken from https://thenounproject.com/term/instructions/
# background image taken from: 
# https://photos.com/featured/cartoon-desert-landscape-in-flat-design-vector-illustration-ekaterina-vakhrameeva.html?product=art-print
class SplashScreenMode(PygameGame):
    def init(self):
        self.background = pygame.transform.scale(pygame.image.load("splash.png"),(self.width,self.height))
        self.easyModeImage = pygame.transform.scale(pygame.image.load("easyMode.png"),(200,100))
        self.hardModeImage = pygame.transform.scale(pygame.image.load("hardMode.png"),(200,100))
        self.instructionImage = pygame.transform.scale(pygame.image.load("instructionButton.png"),(100,100))
        self.selfCreateImage = pygame.transform.scale(pygame.image.load("createButton.png"),(200,100))
        self.saveMapImage = pygame.transform.scale(pygame.image.load("save.png"),(200,100))
        self.robotImage = pygame.transform.scale(pygame.image.load('createEnemyButton.png'),(100,95))

        # music taken from https://www.youtube.com/watch?v=L_P5V-9h0BE
        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play(-1,4)
        pygame.mixer.music.set_volume(0.5)



    def mousePressed(self,x,y):
        if 850 <= x <= 850 + 100 and \
            self.height - 120 <= y <= self.height - 120 + 100:
            InstructionScreenMode().run()
        elif 550 <= x <= 550 + 200 and \
            self.height - 300 <= y <= self.height - 300 + 100:
            MapTwoMode().run()
        elif 250 <= x <= 250 + 200 and \
            self.height - 300 <= y <= self.height - 300 + 100:
            MapOneMode().run()
        elif 250 <= x <= 250 + 200 and \
            self.height - 150 <= y <= self.height - 150 + 100:
            CreateMapRouteMode().run()
        elif 850 <= x <= 850 + 100 and \
            self.height - 230 <= y <= self.height - 230 + 95:
            BuildRobotMonsterMode().run()
        elif 550 <= x <= 550 + 200 and \
            self.height - 150 <= y <= self.height - 150 + 100:
            SavedMapMode().run()

    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.easyModeImage,(250,self.height - 300))
        screen.blit(self.hardModeImage,(550,self.height - 300))
        screen.blit(self.instructionImage,(850,self.height - 120))
        screen.blit(self.selfCreateImage,(250,self.height - 150))
        screen.blit(self.saveMapImage,(550,self.height - 150))
        screen.blit(self.robotImage,(850,self.height - 230))


class BuildRobotMonsterMode(PygameGame):
    def init(self):
        # music taken from https://www.youtube.com/watch?v=snunX2zlnmI
        pygame.mixer.music.load('create music.mp3')
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        # robot sprites taken from https://www.gameart2d.com/the-robot---free-sprites.html
        self.sprites = [pygame.transform.scale(pygame.image.\
            load(f"robot\Run ({i}).png"),(200,200)) for i in range(1,9)]
        self.sprites += ([pygame.transform.scale(pygame.image.\
            load(f"robot\RunShoot ({i}).png"),(200,200)) for i in range(1,9)])
        self.spriteCounter = 0
        self.timerCount = 0
        # small icon representing life, value and step are made with powerpoint
        self.life = Inserter("life","Enter Here",400,50,pygame.transform.scale(pygame.image.load("life.png"),(350,100)))
        self.value = Inserter("value","Enter Here",400,250,pygame.transform.scale(pygame.image.load("value.png"),(350,100)))
        self.step = Inserter("step","Enter Here",400,450,pygame.transform.scale(pygame.image.load("step.png"),(350,100)))
        self.inserter = [self.life,self.value,self.step]
        self.selected = None
        self.parameters = dict()
        self.backImage = pygame.transform.scale(pygame.image.load("back.png"),(180,90))
        pygame.mixer.music.play(-1,35)
        self.error = None
        self.haveError = False

    
    def timerFired(self,dt):
        self.timerCount += 1
        if self.timerCount % 5 == 0:
            self.spriteCounter = (1 + self.spriteCounter) % len(self.sprites)
        if self.timerCount % 45 == 0:
            self.error = None
            self.haveError = False

    def mousePressed(self,x,y):
        for inserter in self.inserter:
            if inserter.checkClicked(x,y):
                self.selected = inserter
        if self.width-200 <= x <= self.width-200+180 and \
            self.height-100 <= y <= self.height-100 + 90:
            for inserter in self.inserter:
                if not inserter.inputText.isdigit():
                    self.haveError = True
                    self.error = pygame.transform.scale(pygame.image.load("integerError.png"),(300,300))
            if self.haveError == False:
                for inserter in self.inserter:
                    self.parameters[inserter.name] = int(inserter.inputText)
                    pickle.dump(self.parameters,open("createMonster.txt","wb"))
                pygame.mixer.music.stop()
                SplashScreenMode().run()
            

        
    def keyPressed(self,keyCode, modifier):
        if self.selected != None:
            if keyCode == pygame.K_BACKSPACE and len(self.selected.inputText) > 0:
                self.selected.inputText = self.selected.inputText[:-1]
            elif keyCode == pygame.K_0:
                self.selected.inputText += '0'
            elif keyCode == pygame.K_1:
                self.selected.inputText += '1'
            elif keyCode == pygame.K_2:
                self.selected.inputText += '2'
            elif keyCode == pygame.K_3:
                self.selected.inputText += '3'
            elif keyCode == pygame.K_4:
                self.selected.inputText += '4'
            elif keyCode == pygame.K_5:
                self.selected.inputText += '5'
            elif keyCode == pygame.K_6:
                self.selected.inputText += '6'
            elif keyCode == pygame.K_7:
                self.selected.inputText += '7'
            elif keyCode == pygame.K_8:
                self.selected.inputText += '8'
            elif keyCode == pygame.K_9:
                self.selected.inputText += '9'


    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        sprite = self.sprites[self.spriteCounter]
        screen.blit(sprite,(100,self.height//2 - 100))
        for inserter in self.inserter:
            inserter.draw(screen)
        screen.blit(self.backImage,(self.width-200,self.height-100))
        if self.error != None:
            screen.blit(self.error,(350,250))


class Inserter(pygame.sprite.Sprite):
    def __init__(self,name,inputText,cx,cy,image):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.name = name
        self.inputText = inputText
        self.image = image
        self.width = 350
        self.height = 100

    def checkClicked(self,x,y):
        return self.cx <= x <= self.cx + self.width\
            and self.cy <= y <= self.cy + self.height
    
    def draw(self,screen):
        screen.blit(self.image,(self.cx,self.cy))
        font = pygame.font.SysFont('Arial', 28)
        surface = font.render(self.inputText, False, (0,0,0))
        screen.blit(surface,(self.cx + 180,self.cy + 30))


