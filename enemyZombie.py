import pygame
from Enemies import *

# this is the zombie class, inherited from enemy class

# image taken from https://www.gameart2d.com/the-zombies-free-sprites.html
class Zombie(Enemy):
    sprites = []
    def __init__(self,cx,cy,route):
        super().__init__(cx,cy,route)
        Zombie.sprites = [pygame.transform.scale(pygame.image.\
            load(f"zombie\Walk ({i}).png"),(50,50)) for i in range(1,11)]
        Zombie.sprites += [pygame.transform.scale(pygame.image.\
            load(f"zombie\Attack ({i}).png"),(50,50)) for i in range(1,9)]
        self.initialLife = 80
        self.life = self.initialLife
        self.value = 80
        self.step = 3
        
    def countSprite(self):
        self.spriteCounter = (1 + self.spriteCounter) % len(Zombie.sprites)
    
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
            sprite = Zombie.sprites[self.spriteCounter]
        else:
            sprite = pygame.transform.flip(Zombie.sprites[self.spriteCounter],True,False)
        screen.blit(sprite,(self.cx,self.cy))
