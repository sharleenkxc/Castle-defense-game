import pygame
from weapon import *
from fire import *

# this is the sun class, inherited from weapon class

# images taken from 
# https://www.uihere.com/free-cliparts/smiley-yellow-text-messaging-clip-art-sun-cartoon-png-clip-art-image-1230665
# https://www.pinterest.com/pin/418905202809903527/
# https://www.pngfind.com/mpng/JbJxiR_heat-clipart-sunshine-cartoon-sun-hd-png-download/
class Sun(Weapon):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.weaponImages = [pygame.transform.scale(pygame.image.\
            load(f"sunImages\sun{i}.png"),(50,50)) for i in range(1,4)]
        self.width = 50
        self.height = 50
        self.price = [220,300,400]
        self.removeCost = 150
        self.range = 60
        self.damage = 0.4
        self.tempDamage = 0.4
        self.tempRange = 60
        self.fireRing = None
    
    def getEnemiesInRange(self,enemies):
        enemiesInRange = []
        for enemy in enemies:
            enemyX,enemyY = enemy.cx,enemy.cy
            if ((enemyX - self.cx)**2 + (enemyY - self.cy)**2)**0.5 <= self.range:
                enemiesInRange.append(enemy)
        return enemiesInRange

    def attack(self,target):
        targetX,targetY = target.cx,target.cy
        self.fireRing = SunFire(self.cx + self.width/2 - self.range,\
            self.cy + self.height/2 - self.range,self.range*2)
    

    def __eq__(self,other):
        return isinstance(other,Sun) and other.cx == self.cx and other.cy == self.cy
    
    def __hash__(self):
        return hash((self.cx,self.cy))

    def draw(self,screen):
        screen.blit(self.weaponImages[self.level],(self.cx,self.cy))
        if self.fireRing != None:
            self.fireRing.draw(screen)
        
    def drawRange(self,screen):
        pygame.draw.circle(screen,(225,225,225),(self.cx + self.width//2,\
            self.cy + self.height//2),self.range,2)
        font = pygame.font.SysFont('Arial', 20)
        font.set_bold(True)
        damageSurface = font.render("damage:" + str(self.damage), False, (225,225,225))
        screen.blit(damageSurface,(self.cx + self.width//2,self.cy + self.height//2))
