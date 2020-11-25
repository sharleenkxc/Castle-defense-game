import pygame
from Enemies import *

# This is the dinosuar class, inheirted from the enemy class

#Image taken from https://opengameart.org/content/free-dino-sprites
class Dinosaur(Enemy):
    sprites = []
    def __init__(self,cx,cy,route):
        super().__init__(cx,cy,route)
        Dinosaur.sprites = [pygame.transform.scale(pygame.image.\
            load(f"enemyDinosaur\png\Run ({i}).png"),(50,50)) for i in range(1,9)]

        # dinosaurs move faster than knights
        self.step = 5
        self.initialLife = 6
        self.life = self.initialLife
        self.value = 30

    
    def countSprite(self):
        self.spriteCounter = (1 + self.spriteCounter) % len(Dinosaur.sprites)

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
            sprite = Dinosaur.sprites[self.spriteCounter]
        else:
            sprite = pygame.transform.flip(Dinosaur.sprites[self.spriteCounter],True,False)
        screen.blit(sprite,(self.cx,self.cy))