# coding=utf-8
import pygame, sys
from pygame.locals import *

class Event:
    def __init__(self,evt,sounds):
        self.evt = evt
        self.sound = sounds

    def evtGeneral(self):
        for event in self.evt:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    def evtInputText(self,input_text):
        for event in self.evt:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == K_RETURN:
                    self.sound.playEnterKey()
                else:
                    if len(input_text) < 12:
                        input_text += event.unicode
                        self.sound.playInputText()
        return input_text

    def evtPressEnter(self):
        for event in self.evt:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return True
        return False
    
    def evtPressEscape(self):
        for event in self.evt:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
        return False

    def evtInGame(self,width,height,player):
        self.w = width
        self.h = height
        self.p = player
        for event in self.evt:
            if event.type == KEYDOWN:
                self.evtKeyDown(event)
            if event.type == KEYUP:
                self.evtKeyUp(event)

    def evtKeyDown(self,event):
        if event.key == K_LEFT:
            if self.p.posX >= 0:
                self.p.velX = -(self.p.velM)
        if event.key == K_RIGHT:
            if self.p.posX <= self.w:
                self.p.velX = self.p.velM
        if event.key == K_SPACE:
            self.p.shoot()
    
    def evtKeyUp(self,event):
        if event.key == K_LEFT:
            self.p.velX = 0
        if event.key == K_RIGHT:
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
                        a.lifes -= pj.damage
                        #pj.listOfShoots.remove(s)
                for e in listEn:
                    if self.evtCollision(e.rect,s.rect):
                        e.getDamage(pj,s)
                        pj.points += 20
                        pj.listOfShoots.remove(s)
                if s.rect.top < -100:
                    pj.listOfShoots.remove(s)

    def evtCollision(self,obj1,obj2):
        if obj1.colliderect(obj2):
            return True
        else:
            return False