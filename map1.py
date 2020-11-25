from GameMode import *

# this is the map for easy mode
class MapOneMode(GameMode):
    def init(self):
        super().init()
        # music taken from :https://www.youtube.com/watch?v=SjC8v5MmEF8
        pygame.mixer.music.load('map1 music.mp3')
        self.money = 600
        self.route = [(7, 0),(7, 1),(7, 2),(7, 3),(6, 3),(5, 3),(4, 3),(4, 4),\
            (4, 5),(4, 6),(4, 7),(5, 7),(6, 7),(7, 7),(8, 7),(8, 8),(8, 9),\
            (8, 10),(8, 11),(8, 12),(8, 13),(7, 13),(6, 13),(6, 14),(6, 15),\
            (7, 15),(8, 15),(8, 16),(8, 17),(8, 18),(8, 19)]
        castleRow,castleCol = self.route[-2]
        castleX,castleY = castleCol*self.size,castleRow*self.size
        self.castle = Castle(castleX,castleY)
        self.numOfWaves = 5
        self.enemyWaves[0] = [Knight(0,350,self.route) for _ in range(10)]
        self.enemyWaves[1] = [Knight(0,350,self.route) for _ in range(15)]
        self.enemyWaves[2] = [Knight(0,350,self.route) for _ in range(10)] + [Dinosaur(0,350,self.route)]
        self.enemyWaves[3] = [Knight(0,350,self.route) for _ in range(5)] + \
            [Dinosaur(0,350,self.route) for _ in range(5)] + [Zombie(0,350,self.route)]
        self.enemyWaves[4] = [Knight(0,350,self.route) for _ in range(8)] + \
            [Dinosaur(0,350,self.route) for _ in range(6)] + [Zombie(0,350,self.route) for _ in range(2)]


        self.obstaclePositions = [(150,400), (100,400), (100,300), (100,250),\
            (200,250), (250,300), (200,350), (300,350), (300,400), \
            (400,350), (400,150), (350,150), (450,300), (500,350), \
            (550,350), (500,450), (450,450), (400,450), (700,400), \
            (600,300), (700,250), (800,300)]
        self.obstacles = pygame.sprite.Group()
        for pos in self.obstaclePositions:
            (x,y) = pos
            self.obstacles.add(Obstacle(x,y))
        pygame.mixer.music.play(-1)


