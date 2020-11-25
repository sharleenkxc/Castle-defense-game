import pygame
from GameMode import *
import pickle
import random

# this is users' last created map

class SavedMapMode(GameMode):
    def init(self):
        super().init()
        # music taken from https://www.youtube.com/watch?v=rvqXalxhYmQ
        pygame.mixer.music.load('saved map music.mp3')
        self.money = int(pickle.load(open("startMoney.txt","rb")))
        self.route = pickle.load(open("selfCreatedMapRoute.txt","rb"))
        castleRow,castleCol = self.route[-1]
        castleX,castleY = castleCol*self.size - 20,castleRow*self.size
        self.castle = Castle(castleX,castleY)
        self.numOfWaves = int(pickle.load(open("numOfWaves.txt","rb")))
        startY,startX = self.route[0][0]*50,self.route[0][1]*50
        for num in range(self.numOfWaves):
            self.parameters = pickle.load(open("createMonster.txt","rb"))
            if ("step" in self.parameters) and ("life" in self.parameters) and \
                ("value" in self.parameters):
                userWillingness = pickle.load(open('willingness.txt','rb'))
                if userWillingness == 'yes':
                    self.enemyWaves[num] = [Knight(startX,startY,self.route) for _ in range(random.randint(5,15))] + \
                    [Dinosaur(startX,startY,self.route) for _ in range(random.randint(0,3*num))] + \
                    [Zombie(startX,startY,self.route) for _ in range(random.randint(0,1*num//2))] +\
                    [Robot(startX,startY,self.route) for _ in range(random.randint(1,2))]
            else:
                self.enemyWaves[num] = [Knight(startX,startY,self.route) for _ in range(random.randint(5,15))] + \
                [Dinosaur(startX,startY,self.route) for _ in range(random.randint(0,3*num))] + \
                [Zombie(startX,startY,self.route) for _ in range(random.randint(0,1*num//2))]
                

        self.obstaclePositions = pickle.load(open("createdObstacles.txt","rb"))
        self.obstacles = pygame.sprite.Group()
        for pos in self.obstaclePositions:
            (x,y) = pos
            self.obstacles.add(Obstacle(x,y))
        pygame.mixer.music.play(-1)
