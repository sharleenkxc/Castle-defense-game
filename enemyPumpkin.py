import pygame
from Enemies import *

# this is the pumpkin class, inherited from enemy class

# pumkin enemy sprites are taken from :
# https://www.gameart2d.com/jack-o-lantern-free-sprites.html

class Pumpkin(Enemy):
    sprites = []
    def __init__(self,cx,cy,route):
        Pumpkin.sprites = [pygame.transform.scale(pygame.image.\
            load(f"pumpkin\Walk ({i}).png"),(50,50)) for i in range(1,11)]

        # dinosaurs move faster than knights
        self.step = 4
        self.initialLife = 20
        self.life = self.initialLife
        self.value = 50
        self.range = 70
        super().__init__(cx,cy,route)
    
    def countSprite(self):
        self.spriteCounter = (1 + self.spriteCounter) % len(Pumpkin.sprites)

    def getWeaponInRange(self,weapons):
        weaponInRange = []
        for weapon in weapons:
            weaponX,weaponY = weapon.cx,weapon.cy
            if ((weaponX - self.cx)**2 + (weaponY - self.cy)**2)**0.5 <= self.range:
                weaponInRange.append(weapon)
        return weaponInRange

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
            sprite = Pumpkin.sprites[self.spriteCounter]
        else:
            sprite = pygame.transform.flip(Pumpkin.sprites[self.spriteCounter],True,False)
        screen.blit(sprite,(self.cx,self.cy))