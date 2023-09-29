# coding=utf-8

import background
import player

class Level:
    def __init__(self,pointForUpLevel,pointForWin,bk,velAst,velEnm,velDisEnm):
        self.lvl = 1
        self.pointForUpLevel = pointForUpLevel
        self.pointForWin = pointForWin
        self.bk = bk
        # Agregando velocidad de asteroides y enemigos
        self.velAst = velAst
        self.velEnm = velEnm
        # Agregando velocidad disparo enemigo
        self.velDisEnm = velDisEnm
    
    def nextLevel(self):
        self.bk.drawText("resources/fonts/font.ttf","Nivel "+str(self.lvl),40,800/2,500/2)

    def upLevel(self):
        self.pointForUpLevel += 500
        self.lvl += 1
        self.bk.vel += 5
        self.bk.posY = 0
        self.velAst += 1
        self.velEnm += 0.5
        self.velDisEnm += -5
    
    def winGame(self):
        self.bk.drawText("resources/fonts/font.ttf","Ganaste!",40,800/2,500/2)
