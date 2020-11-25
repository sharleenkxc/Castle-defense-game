import pygame
from Enemies import *
import pickle

# This is the user-created robot class

# robot sprites taken from https://www.gameart2d.com/the-robot---free-sprites.html
class Robot(Enemy):
    sprites = []
    def __init__(self,cx,cy,route):
        super().__init__(cx,cy,route)
        Robot.sprites = [pygame.transform.scale(pygame.image.\
            load(f"robot\Run ({i}).png"),(50,50)) for i in range(1,9)]
        Robot.sprites += ([pygame.transform.scale(pygame.image.\
            load(f"robot\RunShoot ({i}).png"),(50,50)) for i in range(1,9)])

        self.parameters = pickle.load(open("createMonster.txt","rb"))

        self.step = int(self.parameters["step"])
        self.initialLife = int(self.parameters["life"])
        self.life = self.initialLife
        self.value = int(self.parameters["value"])
    
    def countSprite(self):
        self.spriteCounter = (1 + self.spriteCounter) % len(Robot.sprites)

    def drawLifeBar(self,screen):
        length = 40
        width = 8
        interval = length/self.initialLife
        lostLife = self.initialLife - self.life
        if self.life*interval < length/2:
            fill = (225,0,0)
        else:
            fill = (0,225,0)
        pygame.draw.rect(screen,(225,225,225),(self.cx,self.cy - 10,length,width))
        pygame.draw.rect(screen,fill,(self.cx,self.cy - 10,self.life*interval,width))

    def draw(self,screen):
        if self.flipped == False:
            sprite = Robot.sprites[self.spriteCounter]
        else:
            sprite = pygame.transform.flip(Robot.sprites[self.spriteCounter],True,False)
        screen.blit(sprite,(self.cx,self.cy))