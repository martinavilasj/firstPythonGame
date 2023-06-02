# coding=utf-8
import pygame, sys
from pygame.locals import *

class Event:
    def __init__(self,width,height,player):
        self.w = width
        self.h = height
        self.p = player
    
    def evtKeyDown(self,evt):
        if evt == K_LEFT:
            if self.p.posX >= 0:
                self.p.velX = -(self.p.velM)
        elif evt == K_RIGHT:
            if self.p.posX <= self.w:
                self.p.velX = self.p.velM
        elif evt == K_SPACE:
            self.p.shoot()
    
    def evtKeyUp(self,evt):
        if evt == K_LEFT:
            self.p.velX = 0
        elif evt == K_RIGHT:
            self.p.velX = 0
    
    def evtShooting(self,pj,pj2):
        if len(pj.listOfShoots)>0:
            for s in pj.listOfShoots:
                s.drawShoot()
                s.trajectory()
                if self.evtCollision(pj2.rect,s.rect):
                    pj2.lifes -= 1
                    pj2.drawCollision()
                    pj.listOfShoots.remove(s)
                if s.pj == "Enemy":
                    if s.rect.top > self.h:
                        pj.listOfShoots.remove(s)
                else:
                    if s.rect.top < 0:
                        pj.listOfShoots.remove(s)
    
    def evtShootingPlayer(self,pj,listEn,listAst):
        if len(pj.listOfShoots)>0:
            for s in pj.listOfShoots:
                s.drawShoot()
                s.trajectory()
                for a in listAst:
                    if self.evtCollision(a.rect,s.rect):
                        a.lifes -= 1
                        #pj.listOfShoots.remove(s)
                for e in listEn:
                    if self.evtCollision(e.rect,s.rect):
                        e.lifes -= 1
                        pj.points += 20
                        pj.listOfShoots.remove(s)
                if s.rect.top < -100:
                    pj.listOfShoots.remove(s)

    def evtCollision(self,obj1,obj2):
        if obj1.colliderect(obj2):
            return True
        else:
            return False
