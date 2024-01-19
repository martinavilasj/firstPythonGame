import pygame, sys
from pygame.locals import *
import background

class Beam:
    def __init__(self,posX,posY,vel,bk,image,pj):
        self.pj = pj
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY
        self.vel = vel
        self.bk = bk

    def drawShoot(self):
        self.bk.drawObjet(self.image,self.rect)

    def trajectory(self):
        self.rect.top -= self.vel

