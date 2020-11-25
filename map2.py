from GameMode import *

# this is the map for hard mode
class MapTwoMode(GameMode):
    def init(self):
        super().init()
        # music taken from https://www.youtube.com/watch?v=gC08RbZVi4c
        pygame.mixer.music.load('map2 music.mp3')
        self.money = 400
        self.route = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),\
            (6, 4), (6, 5), (6, 6), (6, 7), (7, 7), (8, 7), (8, 8), (8, 9), \
            (7, 9), (6, 9), (6, 10), (6, 11)]
        castleRow,castleCol = self.route[-1]
        castleX,castleY = castleCol*self.size-20,castleRow*self.size
        self.castle = Castle(castleX,castleY)
        self.numOfWaves = 7
        
        self.enemyWaves[0] = [Knight(150,0,self.route) for _ in range(10)] + [Dinosaur(150,0,self.route) for _ in range(3)] 
        self.enemyWaves[1] = [Knight(150,0,self.route) for _ in range(15)] + [Dinosaur(150,0,self.route) for _ in range(3)] + [Pumpkin(150,0,self.route)]
        self.enemyWaves[2] = [Knight(150,0,self.route) for _ in range(10)] + [Dinosaur(150,0,self.route) for _ in range(8)] + [Pumpkin(150,0,self.route)]
        self.enemyWaves[3] = [Knight(150,0,self.route) for _ in range(10)] + \
            [Dinosaur(150,0,self.route) for _ in range(5)] + [Zombie(150,0,self.route) for _ in range(2)] 
        self.enemyWaves[4] = [Knight(150,0,self.route) for _ in range(10)] + \
            [Dinosaur(150,0,self.route) for _ in range(6)] + [Zombie(150,0,self.route) for _ in range(3)]
        self.enemyWaves[5] = [Knight(150,0,self.route) for _ in range(10)] + \
            [Zombie(150,0,self.route) for _ in range(3)] + [Pumpkin(150,0,self.route) for _ in range(2)]
        self.enemyWaves[6] = [Knight(150,0,self.route) for _ in range(15)] + \
            [Dinosaur(150,0,self.route) for _ in range(8)]  + [Zombie(150,0,self.route) for _ in range(4)] 

        self.obstaclePositions = [(100,100), (100,150), (100,200), (200,100), \
            (200,250), (150,350), (250,350), (300,350), (350,250), (400,300), \
                (350,450), (400,450), (500,400), (450,250)]
        self.obstacles = pygame.sprite.Group()
        for pos in self.obstaclePositions:
            (x,y) = pos
            self.obstacles.add(Obstacle(x,y))
        pygame.mixer.music.play(-1,33)
