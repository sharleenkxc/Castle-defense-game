import pygame
from weapon import *
from chiliFire import *

# This is the chili class, inherited from weapon class

# Image taken from https://www.vectorstock.com/royalty-free-vector/angry-hot-chili-pepper-on-cartoon-table-vector-22026475

class Chili(Weapon):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.weaponImages = pygame.transform.scale(pygame.image.load("chili.png"),(50,50))
        self.width = 50
        self.height = 50
        self.price = [600]
        self.fireLine = None
    
    def getEnemiesInRange(self,enemies):
        enemiesInRange = []
        for enemy in enemies:
            if self.cy == enemy.cy:
                enemiesInRange.append(enemy)
        return enemiesInRange

    def attack(self,target):
        targetX,targetY = target.cx,target.cy
        self.fireLine = ChiliFire(0,self.cy)

    def __eq__(self,other):
        return isinstance(other,Chili) and other.cx == self.cx and other.cy == self.cy
    
    def __hash__(self):
        return hash((self.cx,self.cy))

    def draw(self,screen):
        if self.fireLine != None:
            self.fireLine.draw(screen)
        screen.blit(self.weaponImages,(self.cx,self.cy))


