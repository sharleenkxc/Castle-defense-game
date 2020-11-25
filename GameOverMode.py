import pygame
from FrameWork import *

# this is the game over mode
class GameOverMode(PygameGame):
    def init(self):
        self.bgColor = (0,0,0)
        pygame.font.init()


    def redrawAll(self,screen):
        instruction = pygame.font.SysFont('Arial', 80)
        instructionSurface = instruction.render('Game Over', False, (225,225,225))
        instructionRect = instructionSurface.get_rect(center = (self.width/2, self.height/2))
        screen.blit(instructionSurface,instructionRect)

