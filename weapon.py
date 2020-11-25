import pygame

# this is the weapon class

class Weapon(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.width = 50
        self.height = 50
        self.price = [0,0,0]
        self.level = 0
        self.removeCost = 0
        self.isSelected = False
        self.attacked = False
    
    # returns true if the weapon is selected by player
    # used for upgrade - will be implemented later
    def selectWeapon(self):
        self.isSelected = not self.isSelected

    
