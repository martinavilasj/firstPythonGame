# coding=utf-8
import pygame, sys
from pygame.locals import *

class Sound:
    def __init__(self,sPly,sEn,sDes,sGO,sWin,sExp):
        self.sPly = sPly
        self.sEn = sEn
        self.sDes = sDes
        self.sGO = sGO
        self.sWin = sWin
        self.sExp = sExp

        self.soundSPLy = pygame.mixer.Sound(self.sPly)
        self.soundSEn = pygame.mixer.Sound(self.sEn)
        
    def soundShootPl(self):
        self.soundSPLy.play()

    def soundShootEn(self):
        self.soundSEn.play()

    def playSound(self,sn):
        sound = pygame.mixer.Sound(sn)
        sound.play()
