import pygame

# this is the menu classes and button classes
class Menu(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
    
    def draw(self,screen):
        pygame.draw.rect(screen,(101,51,0),(self.cx,self.cy,self.width,self.height))


class WeaponMenu(Menu):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.width = 50
        self.height = 115
        self.buttons = [None,None]
    
    def draw(self,screen):
        super().draw(screen)
        for button in self.buttons:
            button.draw(screen)
            costFont = pygame.font.SysFont('Arial', 15)
            costFont.set_bold(True)
            if button.cost == None:
                costSurface = costFont.render("MAX", False, (224,224,224))
            else:
                costSurface = costFont.render("$ " + str(button.cost), False, (224,224,224))
            screen.blit(costSurface,(button.cx + 2,button.cy + 35))

    

class WeaponOptionsMenu(Menu):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.width = 300
        self.height = 100
        self.buttons = [None,None,None]

    def draw(self,screen):
        super().draw(screen)
        for button in self.buttons:
            button.draw(screen)
            costFont = pygame.font.SysFont('Arial', 20)
            costFont.set_bold(True)
            costSurface = costFont.render("$ " + str(button.cost), False, (224,224,224))
            screen.blit(costSurface,(button.cx + 3,button.cy + 60))


class Button(pygame.sprite.Sprite):
    def __init__(self,cx,cy,cost):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.cost = cost
        self.width = 40
        self.height = 40
        self.image = None
    
    def checkClicked(self,x,y):
        # since the button image has a little edge, add & minus a small number
        return self.cx + 1 <= x <= self.cx + self.width - 1 \
            and self.cy + 1 <= y <= self.cy + self.height - 1
    
    def draw(self,screen):
        screen.blit(self.image,(self.cx,self.cy))


class ButtonWithoutCost(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.cx = cx
        self.cy = cy
        self.width = 50
        self.height = 50
        self.image = None
    
    def checkClicked(self,x,y):
        # since the button image has a little edge, add & minus a small number
        return self.cx + 1 <= x <= self.cx + self.width - 1 \
            and self.cy + 1 <= y <= self.cy + self.height - 1
    
    def draw(self,screen):
        screen.blit(self.image,(self.cx,self.cy))

# image taken from 
# https://webstockreview.net/explore/clipart-pen-animation/
# edited
class DrawRangeButton(ButtonWithoutCost):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.image = pygame.transform.scale(pygame.image.load("drawRangeButton.png"),(50,50))

# image taken from 
# https://webstockreview.net/explore/clipart-pen-animation/
# edited
class CannotDrawRangeButton(ButtonWithoutCost):
    def __init__(self,cx,cy):
        super().__init__(cx,cy)
        self.image = pygame.transform.scale(pygame.image.load("cannotDrawRangeButton.png"),(50,50))


# Upgrade icon taken from:
# https://depositphotos.com/168455212/stock-illustration-grunge-red-upgrade-wording-with.html
# Further edited by myself
class UpgradeButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("upgrade.png"),(40,40))

# Upgrade icon taken from:
# https://depositphotos.com/168455212/stock-illustration-grunge-red-upgrade-wording-with.html
# Further edited by myself
class CannotUpgradeButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("notUpgrade.png"),(40,40))

# Remove icon taken from:
# http://www.iconarchive.com/show/must-have-icons-by-visualpharm/remove-icon.html
class RemoveButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("remove.png"),(40,40))

# Remove icon taken from:
# http://www.iconarchive.com/show/must-have-icons-by-visualpharm/remove-icon.html
# Edited by myself
class CannotRemoveButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("notRemove.png"),(40,40))

# images taken from 
# https://imgbin.com/png/EEb0cYaS/sprite-2d-computer-graphics-tile-based-video-game-tower-defense-png
# edited
class TowerButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("towerButton.png"),(60,60))

# images taken from 
# https://imgbin.com/png/EEb0cYaS/sprite-2d-computer-graphics-tile-based-video-game-tower-defense-png
# edited
class CannotAddTowerButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("cannotAddTowerButton.png"),(60,60))


# Image taken from https://www.pinterest.com/pin/418905202809903527/
# edited
class SunButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("sunButton.png"),(60,60))


# Image taken from https://www.pinterest.com/pin/418905202809903527/
# edited
class CannotAddSunButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("cannotAddSunButton.png"),(60,60))

# Image taken from 
# https://www.vectorstock.com/royalty-free-vector/angry-hot-chili-pepper-on-cartoon-table-vector-22026475
# Edited
class ChiliButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("addChiliButton.png"),(60,60))

# Image taken from 
# https://www.vectorstock.com/royalty-free-vector/angry-hot-chili-pepper-on-cartoon-table-vector-22026475
# Edited
class CannotAddChiliButton(Button):
    def __init__(self,cx,cy,cost):
        super().__init__(cx,cy,cost)
        self.image = pygame.transform.scale(pygame.image.load("cannotAddChiliButton.png"),(60,60))
