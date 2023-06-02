# coding=utf-8
import pygame, sys
from pygame.locals import *
from random import *

class Asteroid:
    def __init__(self,velM,lifes,width,height,bk,sn):
        self.velM = velM
        self.lifes = lifes
        self.width = width
        self.height = height
        self.bk = bk
        
        self.sn = sn

        self.posY = -100
        self.posX = randint(0,self.width)
        self.asteroidNum = randint(1,6)
        self.asteroidImg = pygame.image.load("resources/asteroids/asteroid"+str(self.asteroidNum)+".png")
        self.rect = self.asteroidImg.get_rect()

    def drawAsteroid(self):
        self.moveAsteroid()

        self.rect.centerx = self.posX
        self.rect.centery = self.posY

        self.bk.drawObjet(self.asteroidImg, self.rect)

    def moveAsteroid(self):
        if self.posY < self.height+50:
            self.posY += self.velM
    
    def destroy(self):
        self.sn.playSound("resources/asteroids/destroy.ogg")
