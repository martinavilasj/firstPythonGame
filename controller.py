# Control de eventos
from pygame.locals import *
from random import *

class Controller:
     def __init__(self,player,background,listAsteroids,listEnemies,evt,level):
        self.inGame = True
        self.start_game = True

        self.p = player
        self.bk = background
        self.lA = listAsteroids
        self.lE = listEnemies
        self.evt = event
        self.lvl = level

        self.second = 0
        self.contL = 0
    
    def controlTime(self):
        self.clock = pygame.time.Clock()
        self.second = round(pygame.time.get_ticks()/1000)

    def updateTime(self):
        time = round(pygame.time.get_ticks()/1000)
        self.clock.tick(60)
        if self.second == time:
            cont = self.second
            self.contS = self.second
            self.second += 1
            self.contL += 1
