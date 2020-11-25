import pygame
# This is the castle class

# Castle Image taken from https://dlpng.com/png/1716001
# Heart Image taken from https://www.pinterest.com/pin/41095415322678932/

class Castle(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.castleImage = pygame.transform.scale(pygame.image.load("castleImage.png"),(100,100))
        self.heartImage = pygame.transform.scale(pygame.image.load("heart.png"),(30,30))
        self.width = 100
        self.height = 100
        self.life = 10
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.cx,self.cy, self.width,self.height)
    
    def draw(self,screen):
        screen.blit(self.castleImage,(self.cx,self.cy - 50))

        screen.blit(self.heartImage,(self.cx + 50,self.cy - 80))
        life = pygame.font.SysFont('comicsansms', 26)
        lifeSurface = life.render(str(self.life), False, (225,225,225))
        screen.blit(lifeSurface,(self.cx + 20,self.cy - 85))



