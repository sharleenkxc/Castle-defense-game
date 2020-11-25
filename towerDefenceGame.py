import pygame
from FrameWork import *
from SplashScreenMode import *
 
# This is the file to run the game

class TowerDefenceGame(PygameGame):
    def init(self):
        SplashScreenMode().run()
    
    
game = TowerDefenceGame()
game.run()