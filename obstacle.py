import pygame

# this is the obstacle class

# rock image taken from  https://www.cleanpng.com/free/cartoon-rock.html
# target image taken from https://www.iconfinder.com/icons/100064/google_places_icon
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.width = 50
        self.height = 50
        self.initialLife = 80
        self.life = self.initialLife
        self.isSelected = False
        self.isAttacked = False
        self.value = 20
        self.obstacleImage = pygame.transform.scale(pygame.image.load("obstacleRock.png"),(50,50))
        self.targetImage = pygame.transform.scale(pygame.image.load("obstacleTarget.png"),(20,20))
        self.updateRect()
    
    def __repr__(self):
        return f"{self.cx},{self.cy}"
          
    def updateRect(self):
        self.rect = pygame.Rect(self.cx,self.cy, self.width,self.height)    

    def drawLifeBar(self,screen):
        length = 30
        width = 6
        interval = length/self.initialLife
        lostLife = self.initialLife - self.life
        if self.life*interval < length/2:
            fill = (225,0,0)
        else:
            fill = (0,225,0)
        pygame.draw.rect(screen,(225,225,225),(self.cx + 15,self.cy - 10,length,width))
        pygame.draw.rect(screen,fill,(self.cx + 15,self.cy - 10,self.life*interval,width))

    def selectObstacle(self):
        self.isSelected = not self.isSelected

    def drawTarget(self,screen):
        screen.blit(self.targetImage,(self.cx + self.width//2,self.cy - 5))    

    def draw(self,screen):
        screen.blit(self.obstacleImage,(self.cx,self.cy))    


