import pygame
# this file contains the Bullet class (bullets of the towers)

# The image of tower's bullet is taken from:
# https://www.hiclipart.com/free-transparent-background-png-clipart-dtror

class TowerBullet(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.towerBulletImage = pygame.transform.scale(pygame.image.\
            load(f"Bullet.png"),(20,20))
        self.cx = cx
        self.cy = cy
        self.width = 20
        self.height = 20
        self.updateRect()
        self.time = 0

    def updateRect(self):
        self.rect = pygame.Rect(self.cx,self.cy, self.width,self.height)
    
    def draw(self,screen):
        screen.blit(self.towerBulletImage,(self.cx,self.cy))
