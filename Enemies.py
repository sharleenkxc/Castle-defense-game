import pygame

# this is the enemy class

class Enemy(pygame.sprite.Sprite):
    def __init__(self,cx,cy,route):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.spriteCounter = 0
        self.gridSize = 50
        self.route = route
        self.xIncrecement = 0
        self.yIncrecement = 0
        self.routePosition = 0
        self.width = 50
        self.height = 50
        self.flipped = False
        self.updateRect()
  
    # move to the next tuple in self.route if finishing walking in this cell
    def updateRoute(self):
        self.updateRect()
        if self.routePosition <= len(self.route) - 2:
            if self.xIncrecement + self.step < 50 and self.yIncrecement + self.step < 50:
                self.move()
            else:
                if self.xIncrecement + self.step>= 50:
                    self.cx = self.route[self.routePosition+1][1]*50
                    self.xIncrecement = 0
                else:
                    self.cy = self.route[self.routePosition+1][0]*50
                    self.yIncrecement = 0
                self.routePosition += 1
    
    def updateRect(self):
        self.rect = pygame.Rect(self.cx,self.cy, self.width,self.height)    

    # move to the correct direction
    def move(self):
        (row1,col1) = self.route[self.routePosition]
        (row2,col2) = self.route[self.routePosition+1]
        if row1 == row2:
            if col1 < col2:
                self.cx += self.step
                self.flipped = False
            else:
                self.cx -= self.step
                self.flipped = True
            self.xIncrecement += self.step
        elif col1 == col2:
            if row1 < row2:
                self.cy += self.step
            else:
                self.cy -= self.step
            self.yIncrecement += self.step
            self.flipped = False



