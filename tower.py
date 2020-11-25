import pygame
from weapon import *
from bullet import *
import math

# this is the tower class, inherited from weapon class

# images taken from 
# https://imgbin.com/png/EEb0cYaS/sprite-2d-computer-graphics-tile-based-video-game-tower-defense-png
class Tower(Weapon):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.weaponImages = [pygame.transform.scale(pygame.image.\
            load(f"tower\weaponTower{i}.png"),(50,50)) for i in range(1,4)]
        self.width = 50
        self.height = 50
        self.price = [180,260,380]
        self.removeCost = 120
        self.range = 80
        self.tempRange = 80
        self.damage = 1
        self.tempDamage = self.damage
        self.bullets = pygame.sprite.Group()

        self.lastTime = 0
    
    def getEnemiesInRange(self,enemies):
        enemiesInRange = []
        for enemy in enemies:
            enemyX,enemyY = enemy.cx,enemy.cy
            if ((enemyX - self.cx)**2 + (enemyY - self.cy)**2)**0.5 <= self.range:
                enemiesInRange.append(enemy)
        return enemiesInRange


    def attack(self,target):
        targetX,targetY = target.cx,target.cy
        self.bullets.add(TowerBullet(self.cx + 10,self.cy + 10))
        
        for bullet in self.bullets:
            yDistance = (self.cy - targetY)/5
            bullet.cy -= yDistance
            if self.cy - targetY != 0:
                xDistance = yDistance*(self.cx-targetX)/(self.cy - targetY)
            else:
                if self.cx > targetX:
                    xDistance = 20
                else:
                    xDistance = -20
            bullet.cx -= xDistance





    def __eq__(self,other):
        return isinstance(other,Tower) and other.cx == self.cx and other.cy == self.cy
    
    def __hash__(self):
        return hash((self.cx,self.cy))

    def draw(self,screen):
        screen.blit(self.weaponImages[self.level],(self.cx,self.cy))
        for bullet in self.bullets:
            bullet.draw(screen)
        
    def drawRange(self,screen):
        pygame.draw.circle(screen,(225,225,225),(self.cx + self.width//2,\
            self.cy + self.height//2),self.range,2)
        font = pygame.font.SysFont('Arial', 20)
        font.set_bold(True)
        damageSurface = font.render("damage:" + str(self.damage), False, (225,225,225))
        screen.blit(damageSurface,(self.cx + self.width//2,self.cy + self.height//2))


