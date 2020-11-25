import pygame
from FrameWork import *
from GameOverMode import *
from WinMode import *

import os
import math
from enemyKnight import *
from enemyZombie import *
import random
from dinosaur import *
from tower import *
from bullet import *
from castle import *
from MenuAndButtons import *
from sun import *
from chili import *
from obstacle import *
from createdMonster import *
from enemyPumpkin import *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

# This is the game mode

# This is the main game mode that uses map 1        
class GameMode(PygameGame):
    def init(self):
        # background taken from https://cubebrush.co/truf-design/products/oedmoa/top-down-desert-pack
        background = pygame.image.load('background.jpg').convert()
        self.background = pygame.transform.scale(background, (self.width,self.height))
        self.enemies = pygame.sprite.Group()
        self.enemyList = []
        self.timerCount = 0
        self.weapons = []
        self.towers = set()
        self.suns = set()
        self.chilis = set()
        self.weaponPos = set()
        self.selectedObstacle = None        
        
        # This game's appearance is based on grids
        self.size = 50
        self.rows = self.height//self.size
        self.cols = self.width//self.size

        self.weaponMenu = None
        self.weaponOptionsMenu = None
        self.canAddWeapon = True
        self.addingTower = False
        self.addingSun = False
        self.addingChili = False
        self.drawRange = False
        self.attackingObstacles = False
        self.currentWave = 0
        self.enemyWaves = dict()

        self.pumpkins = []
        self.spriteCounter = 0
        self.count = 0
        # image taken from :
        # https://www.seekclipart.com/clipart/iTTRTiR_splash-png-orange-orange-paint-splash-png-clipart/
        self.pumpkinAttackSprites = [pygame.transform.scale(pygame.image.load('pumpkinAttack.png'),(70,70)),\
            pygame.transform.scale(pygame.image.load('pumpkinAttack1.png'),(70,70))]


    def timerFired(self,dt):
        self.timerCount += 1
        if self.timerCount % 10 == 0:
            self.spriteCounter = (1 + self.spriteCounter) % len(self.pumpkinAttackSprites)
        for enemies in self.enemies:
            enemies.updateRoute()
            enemies.countSprite()

        self.towerAttack()
        self.sunAttack()
        self.chiliAttack()
        self.pumpkinAttack()

        if self.timerCount % 5 == 0:
            self.chilis = set()
        if pygame.sprite.spritecollide(self.castle, self.enemies, True):
            self.castle.life -= 1
            if len(self.enemies) == 0:
                self.currentWave += 1
                if self.currentWave == self.numOfWaves:
                    pygame.mixer.music.stop()
                    WinMode().run()
            if self.castle.life <= 0:
                pygame.mixer.music.stop()
                GameOverMode().run()
        if self.timerCount % 15 == 0 and len(self.enemyWaves[self.currentWave]) > 0:
            newEnemy = self.enemyWaves[self.currentWave].pop(0)
            self.enemies.add(newEnemy)
            self.enemyList.append(newEnemy)
            if isinstance(newEnemy,Pumpkin):
                self.pumpkins.append(newEnemy)


        self.buildWeaponMenu()
        self.buildWeaponOptionsMenu()
        self.buildRangeButton()

    def buildRangeButton(self):
        if len(self.weapons) == 0:
            self.rangeButton = CannotDrawRangeButton(self.width - 60, 110)
        else:
            self.rangeButton = DrawRangeButton(self.width - 60, 110)

    # build the menu options for the selected weapon
    def buildWeaponMenu(self):
        for weapon in self.weapons:
            if weapon.isSelected:
                self.canAddWeapon = False
                self.weaponMenu = WeaponMenu(weapon.cx + weapon.width,weapon.cy - 20)
                if self.money >= weapon.removeCost:
                    self.weaponMenu.buttons[1] = RemoveButton(self.weaponMenu.cx + 5,\
                        self.weaponMenu.cy + 60,weapon.removeCost)
                else:
                    self.weaponMenu.buttons[1] = CannotRemoveButton(self.weaponMenu.cx + 5,\
                        self.weaponMenu.cy + 60,weapon.removeCost)

                if weapon.level + 1 == 3:
                    self.weaponMenu.buttons[0] = CannotUpgradeButton(self.weaponMenu.cx + 5,\
                        self.weaponMenu.cy + 5,None)
                elif weapon.level < 2 and self.money >= weapon.price[weapon.level + 1]:
                    self.weaponMenu.buttons[0] = UpgradeButton(self.weaponMenu.cx + 5,\
                        self.weaponMenu.cy + 5,weapon.price[weapon.level + 1])
                else:
                    self.weaponMenu.buttons[0] = CannotUpgradeButton(self.weaponMenu.cx + 5,\
                        self.weaponMenu.cy + 5,weapon.price[weapon.level + 1])

    # Build the menu where players can choose different kinds of weapons
    def buildWeaponOptionsMenu(self):
        self.weaponOptionsMenu = WeaponOptionsMenu(self.width - 350,0)
        # build tower button
        if self.money >= 180:
            self.weaponOptionsMenu.buttons[0] = TowerButton(self.weaponOptionsMenu.cx + 20,\
                self.weaponOptionsMenu.cy + 10,180)
        else:
            self.weaponOptionsMenu.buttons[0] = CannotAddTowerButton\
                (self.weaponOptionsMenu.cx + 20,self.weaponOptionsMenu.cy + 10,180)
        # build sun button
        if self.money >= 220:
            self.weaponOptionsMenu.buttons[1] = SunButton(self.weaponOptionsMenu.cx + 110,\
                self.weaponOptionsMenu.cy + 10,220)
        else:
            self.weaponOptionsMenu.buttons[1] = CannotAddSunButton\
                (self.weaponOptionsMenu.cx + 110,self.weaponOptionsMenu.cy + 10,220)
        # build chili button
        if self.money >= 600:
            self.weaponOptionsMenu.buttons[2] = ChiliButton(self.weaponOptionsMenu.cx + 200,\
                self.weaponOptionsMenu.cy + 10,600)
        else:
            self.weaponOptionsMenu.buttons[2] = CannotAddChiliButton\
                (self.weaponOptionsMenu.cx + 200,self.weaponOptionsMenu.cy + 10,600)

    def pumpkinAttack(self):
        for pumpkin in self.pumpkins:
            pumpkinX,pumpkinY = pumpkin.cx,pumpkin.cy
            pumpkinRange = pumpkin.range
            if len(self.weapons) > 0:
                weaponInRange = pumpkin.getWeaponInRange(self.weapons)
                if len(weaponInRange) == 0:
                    self.count = 0
                    for weapon in self.weapons:
                        if weapon.attacked:
                            weapon.attacked = False
                            weapon.range = weapon.tempRange
                            weapon.damage = weapon.tempDamage
                else:
                    self.count += 1
                for weapon in weaponInRange:
                    weapon.attacked = True
                    if self.count == 1:
                        weapon.range -= int(0.2*weapon.range)
                        weapon.damage -= 0.4*weapon.damage


    # each tower shoots the first enemy in range using bullets
    def towerAttack(self):    
        for tower in self.towers:
            towerX,towerY = tower.cx,tower.cy
            towerRange = tower.range
            if len(self.enemyList) > 0:
                enemiesInRange = tower.getEnemiesInRange(self.enemyList)
                maxMove = 0
                target = None
                initialX,initialY = 0,350
                obstaclesInRange = tower.getEnemiesInRange(self.obstacles)
                for obstacle in self.obstacles:
                    if obstacle.isSelected and (obstacle in obstaclesInRange):
                        self.attackingObstacles = True
                        tower.attack(obstacle)
                        pygame.sprite.spritecollide(obstacle,tower.bullets,True)
                        obstacle.life -= tower.damage
                        obstacle.isAttacked = True
                        if obstacle.life <= 0:
                            self.obstacles.remove(obstacle)
                            if (obstacle.cx,obstacle.cy) in self.obstaclePositions:
                                self.obstaclePositions.remove((obstacle.cx,obstacle.cy))
                            self.selectedObstacle = None
                            self.money += obstacle.value
                    else:
                        obstacle.isAttacked = False

                if self.selectedObstacle == None:
                    self.attackingObstacles = False

                if self.attackingObstacles == False:  
                    for enemy in enemiesInRange:
                        enemyX,enemyY = enemy.cx,enemy.cy
                        move = abs(enemyX-initialX) + abs(enemyY-initialY)
                        if move > maxMove:
                            maxMove = move
                            target = enemy
                            targetX,targetY = target.cx,target.cy
                            if self.timerCount % 5 == 0:
                                tower.attack(target)
                                pygame.sprite.spritecollide(target,tower.bullets,True)
                                target.life -= tower.damage
                                if target.life <= 0:
                                    self.enemies.remove(target)
                                    enemiesInRange.remove(target)
                                    self.enemyList.remove(target)
                                    self.money += target.value
                                    if len(self.enemyList) == 0:
                                        self.currentWave += 1
                                        if self.currentWave == self.numOfWaves:
                                            pygame.mixer.music.stop()
                                            WinMode().run()
               
            # remove bullets that are generated long time ago                
            for bullet in tower.bullets:
                bullet.updateRect()
                bullet.time += 1
                if bullet.time > 15:
                    tower.bullets.remove(bullet)

    def sunAttack(self):    
        for sun in self.suns:
            sunX,sunY = sun.cx,sun.cy
            sunrRange = sun.range
            if len(self.enemyList) > 0:
                enemiesInRange = sun.getEnemiesInRange(self.enemyList)
                if len(enemiesInRange) == 0:
                    sun.fireRing = None

                obstaclesInRange = sun.getEnemiesInRange(self.obstacles)
                for obstacle in self.obstacles:
                    if obstacle in obstaclesInRange:
                        if obstacle.isSelected:
                            self.attackingObstacles = True
                            sun.attack(obstacle)
                            self.attackObstaclesInRange(obstaclesInRange,sun)
                        else:
                            obstacle.isAttacked = False

                if self.selectedObstacle == None:
                    self.attackingObstacles = False
                
                for target in enemiesInRange:
                    sun.attack(target)
                    target.life -= sun.damage
                    self.attackObstaclesInRange(obstaclesInRange,sun)
                    if target.life <= 0:
                        self.enemies.remove(target)
                        enemiesInRange.remove(target)
                        self.enemyList.remove(target)
                        self.money += target.value
                        if len(self.enemyList) == 0:
                            self.currentWave += 1
                            if self.currentWave == self.numOfWaves:
                                pygame.mixer.music.stop()
                                WinMode().run()
        
    def attackObstaclesInRange(self,obstaclesInRange,sun):
        for obstacle in obstaclesInRange:
            obstacle.life -= sun.damage
            obstacle.isAttacked = True
            if obstacle.life <= 0:
                self.obstacles.remove(obstacle)
                self.selectedObstacle = None
                self.money += obstacle.value
                if (obstacle.cx,obstacle.cy) in self.obstaclePositions:
                    self.obstaclePositions.remove((obstacle.cx,obstacle.cy))
                


    def chiliAttack(self):    
        for chili in self.chilis:
            chiliY = chili.cy
            if len(self.enemyList) > 0:
                enemiesInRange = chili.getEnemiesInRange(self.enemyList)
                if len(enemiesInRange) == 0:
                    chili.fireLine = None
                for target in enemiesInRange:
                    chili.attack(target)
                    target.life -= 8
                    if target.life <= 0:
                        self.enemies.remove(target)
                        enemiesInRange.remove(target)
                        self.enemyList.remove(target)
                        self.money += target.value
                        if len(self.enemyList) == 0:
                            self.currentWave += 1
                            if self.currentWave == self.numOfWaves:
                                pygame.mixer.music.stop()
                                WinMode().run()
                           
    
    def mousePressed(self,x,y):
        clickX,clickY = (x//self.size)*self.size,(y//self.size)*self.size
        for weapon in self.weapons:
            if weapon.cx == clickX and weapon.cy == clickY:
                weapon.selectWeapon()

        # update the selection status of obstacles
        if self.selectedObstacle != None and self.selectedObstacle.rect.collidepoint((x,y)):
            self.selectedObstacle.isSelected = False
            self.selectedObstacle = None
        else:
            for obstacle in self.obstacles:
                obstacle.isSelected = False
                if obstacle.cx == clickX and obstacle.cy == clickY:
                    obstacle.isSelected = True
                    self.selectedObstacle = obstacle        

        if self.addingTower:
            if (y//self.size,x//self.size) in self.route or \
                ((x//self.size)*self.size,(y//self.size)*self.size) in self.obstaclePositions:
                self.addingTower = True
            else:
                if self.canAddWeapon and \
                    not (x//self.size,y//self.size) in self.weaponPos:
                    self.addNewWeapon(Tower(clickX,clickY))
                    self.weaponPos.add((x//self.size,y//self.size))
                self.addingTower = False
        
        if self.addingSun:
            if (y//self.size,x//self.size) in self.route or \
                ((x//self.size)*self.size,(y//self.size)*self.size) in self.obstaclePositions:
                self.addingSun = True
            else:
                if self.canAddWeapon and \
                    not (x//self.size,y//self.size) in self.weaponPos:
                    self.addNewWeapon(Sun(clickX,clickY))
                    self.weaponPos.add((x//self.size,y//self.size))
                self.addingSun = False

        if self.addingChili:
            if ((x//self.size)*self.size,(y//self.size)*self.size) in self.obstaclePositions:
                self.addingSun = True
            else:
                if self.canAddWeapon:
                    self.addNewWeapon(Chili(clickX,clickY))
                self.addingChili = False

        for button in self.weaponOptionsMenu.buttons:
            if button.checkClicked(x,y):
                if isinstance(button,TowerButton):
                    self.addingTower = True
                elif isinstance(button,SunButton):
                    self.addingSun = True
                elif isinstance(button,ChiliButton):
                    self.addingChili = True

        if self.rangeButton.checkClicked(x,y):
            self.drawRange = not self.drawRange
        
        # pop weapon menu for selected weapons
        for weapon in self.weapons:
            if weapon.isSelected:
                # Cannot add another weapon when menu option pops up for one weapon
                self.canAddWeapon = False
                if self.weaponMenu != None:  
                    for button in self.weaponMenu.buttons:
                        if button.checkClicked(x,y):
                            if isinstance(button,UpgradeButton) and weapon.level < 2:
                                if isinstance(weapon,Tower):
                                    weapon.range += 20
                                    weapon.tempRange += 20
                                    weapon.damage += 0.6*weapon.damage
                                    weapon.tempDamage += 0.6*weapon.tempDamage
                                elif isinstance(weapon,Sun):
                                    weapon.range += 15
                                    weapon.tempRange += 15
                                    weapon.damage += 0.3*weapon.damage
                                    weapon.tempDamage += 0.3*weapon.tempDamage
                                weapon.level += 1
                                self.money -= weapon.price[weapon.level]
                            elif isinstance(button,RemoveButton):
                                self.weapons.remove(weapon)
                                self.weaponPos.remove((weapon.cx//self.size,weapon.cy//self.size))
                                self.money -= weapon.removeCost
                                self.canAddWeapon = True
                                if isinstance(weapon,Tower):
                                    self.towers.remove(weapon)
                                elif isinstance(weapon,Sun):
                                    self.suns.remove(weapon)
                            weapon.isSelected = False
            else:
                self.canAddWeapon = True
   
    def addNewWeapon(self,newWeapon):
       if self.money >= newWeapon.price[0]:
            self.money -= newWeapon.price[0]
            if isinstance(newWeapon,Tower):
                self.towers.add(newWeapon)
                self.weapons.append(newWeapon)
            elif isinstance(newWeapon,Sun):
                self.suns.add(newWeapon)
                self.weapons.append(newWeapon)
            elif isinstance(newWeapon,Chili):
                self.chilis.add(newWeapon)

    
    def drawMoney(self,screen):
        # draws the amount of money players currently have
        # Money icon taken from:
        # https://www.kissclipart.com/saving-money-cartoon-png-clipart-saving-clip-art-7xljyj/
        moneyImage = pygame.transform.scale(pygame.image.load("money.png").convert_alpha(),(60,60))
        screen.blit(moneyImage,(0,0))
        moneyFont = pygame.font.SysFont('comicsansms', 26)
        moneySurface = moneyFont.render("$" + str(self.money), False, (225,225,225))
        screen.blit(moneySurface,(60,10))
    
    def drawWaves(self,screen):
        waveFont = pygame.font.SysFont('comicsansms', 40)
        waveSurface = waveFont.render("Wave " + str(self.currentWave + 1) + "/" + \
            str(self.numOfWaves), False, (225,225,225))
        screen.blit(waveSurface,(self.width//2 - 80,10))

    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        pumpkinSprite = self.pumpkinAttackSprites[self.spriteCounter]

        # draws the map
        for row in range(self.rows):
            for col in range(self.cols):
                if (row,col) in self.route:
                    (x0, y0) = (col*self.size,row*self.size)
                    pygame.draw.rect(screen,(0,0,0),(x0,y0,self.size,self.size))
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            if obstacle.isAttacked:
                obstacle.drawLifeBar(screen)
            if obstacle.isSelected:
                obstacle.drawTarget(screen)
            
        self.castle.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
            enemy.drawLifeBar(screen)
        for tower in self.towers:
            tower.draw(screen)
            if self.drawRange:
                tower.drawRange(screen)
            if tower.attacked:
                screen.blit(pumpkinSprite,(tower.cx - 5,tower.cy - 5))

            if tower.isSelected and self.weaponMenu != None:
                self.weaponMenu.draw(screen)
        for sun in self.suns:
            sun.draw(screen)
            if self.drawRange:
                sun.drawRange(screen)
            if sun.attacked:
                screen.blit(pumpkinSprite,(sun.cx - 10,sun.cy - 10))

            if sun.isSelected and self.weaponMenu != None:
                self.weaponMenu.draw(screen)
        for chili in self.chilis:
            chili.draw(screen)

        self.drawMoney(screen)
        self.drawWaves(screen)
        if self.weaponOptionsMenu != None:       
            self.weaponOptionsMenu.draw(screen)
        
        self.rangeButton.draw(screen)
