# coding=utf-8

import background
import player

class Level:
    def __init__(self,pointForUpLevel,pointForWin,bk):
        self.lvl = 1
        self.pointForUpLevel = pointForUpLevel
        self.pointForWin = pointForWin
        self.bk = bk
    
    def nextLevel(self):
        self.bk.drawText("resources/fonts/font.ttf","Nivel "+str(self.lvl),40,800/2,500/2)

    def upLevel(self):
        self.pointForUpLevel += 1000
        self.lvl += 1
        self.bk.vel += 10
    
    def winGame(self):
        self.bk.drawText("resources/fonts/font.ttf","Ganaste!",40,800/2,500/2)
