import pygame

# this is the fire of the sun weapon

# The image is taken from:
# https://www.netclipart.com/isee/bmxJJo_flame-vector-ring-ring-of-fire-png/
class SunFire(pygame.sprite.Sprite):
    def __init__(self,cx,cy,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.sunFireImage = pygame.transform.scale(pygame.image.\
            load('sunFire.png'),(self.size,self.size))
        self.cx = cx
        self.cy = cy
        self.width = self.size
        self.height = self.size
        self.updateRect()
    
    def updateRect(self):
        self.rect = pygame.Rect(self.cx,self.cy, self.width,self.height)
    
    def draw(self,screen):
        screen.blit(self.sunFireImage,(self.cx,self.cy))
