# Control de eventos
import pygame
from random import *
import enemy as eny
import asteroid as ast

class Controller:
    def __init__(self,player,background,listAsteroids,listEnemies,event,level,sound,width,height):
        self.inGame = True
        self.start_game = True

        self.p = player
        self.bk = background
        self.lA = listAsteroids
        self.lE = listEnemies
        self.evt = event
        self.lvl = level
        self.s = sound
        self.width = width
        self.height = height

        self.second = 0
        self.cont = 0

    def controlTime(self):
        self.clock = pygame.time.Clock()
        self.second = round(pygame.time.get_ticks()/1000)

    def updateTime(self):
        time = round(pygame.time.get_ticks()/1000)
        self.clock.tick(60)
        if self.second == time:
            self.cont = self.second
            self.second += 1
    
    def control_lvl(self):
        if self.p.lifes <= 0:
            self.stop_game()
            self.lvl.gameOver()
        elif self.p.points >= self.lvl.pointForWin:
            self.stop_game()
            self.lvl.winGame()
        elif self.p.points >= self.lvl.pointForUpLevel:
            if len(self.lA) > 0 or len(self.lE) > 0:
                self.lE.clear()
                self.lA.clear()
            self.lvl.upLevel()
            self.lvl.nextLevel()
            self.second += 3
        elif self.p.points == 0 and self.start_game:
            self.lvl.nextLevel()
            self.second += 3
            self.start_game = False

    def stop_game(self):
        self.inGame = False
        self.p.velX = 0
        self.bk.vel = 0

    def generate_asteroids(self,asteroideVidas):
        ctrlAst = randint(1,9999)

        if ctrlAst % 90 == 0:
            aste2 = ast.Asteroid(self.lvl.velAst,asteroideVidas,self.width,self.height,self.bk,self.s)
            self.lA.append(aste2)
    
    def generate_enemies(self,enemigoVidas):
        if self.cont % 7 == 0:
            enmy = eny.Enemy(self.lvl.velEnm,self.lvl.velDisEnm,enemigoVidas,self.width,self.height,self.bk,self.s)
            self.lE.append(enmy)
            self.cont += 1

    def control_asteroids(self):
        if len(self.lA)>0:
            for a in self.lA:
                if not self.inGame:
                    a.velM = 0
                a.drawAsteroid()
                if a.rect.top > self.height+50:
                    self.lA.remove(a)
                if self.evt.evtCollision(a.rect,self.p.rect):
                    self.p.lifes -= 1
                    self.p.drawCollision()
                    self.lA.remove(a)
                if a.lifes == 0:
                    a.destroy()
                    self.lA.remove(a)
                    self.p.points += 10
    
    def control_enemies(self):
        ctrlAst = randint(1,9999)
        if len(self.lE)>0:
            for e in self.lE:
                if not self.inGame:
                    e.velM = 0
                    e.velX = 0
                    e.velS = 0
                else:
                    if ctrlAst % 90 == 0:    
                        if len(e.listOfShoots) == 0:    
                            e.shoot()
                    self.evt.evtShooting(e,self.p)
                e.drawEnemy()
                if e.rect.top > self.height+50:
                    self.lE.remove(e)
                if e.lifes == 0:
                    self.lE.remove(e)
                    self.p.points += 100

                if self.evt.evtCollision(e.rect,self.p.rect):
                    e.enemyNum = 6
                    self.p.lifes -= 1
                    self.p.drawCollision()
                    self.lE.remove(e)