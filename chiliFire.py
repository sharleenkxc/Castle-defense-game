import pygame

# This is the fire the chili creates when attacking

# image taken from:
# http://www.waveguide.com/blog/run-into-the-fire-or-you-might-get-burned/
# edited
class ChiliFire(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.chiliFireImage = pygame.transform.scale(pygame.image.\
            load('fireLine.png'),(1000,50))
        self.cx = cx
        self.cy = cy
        self.width = 1000
        self.height = 50
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.cx,self.cy, self.width,self.height)
    
    def draw(self,screen):
        screen.blit(self.chiliFireImage,(self.cx,self.cy))
