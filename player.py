# coding=utf-8
import pygame, sys
from pygame.locals import *
import background, beam

class Player:
    def __init__(self,velM,velS,velX,lifes,color,width,height,bk,sn,name):
        self.velM = velM # velM --> entero para la velocidad del jugador al presionar teclas de movimiento
        self.velS = velS # velS --> entero para velocidad del disparo
        self.velX = velX # velX --> variable modificadora de velocidad para movimiento continuo
        self.lifes = lifes # lifes --> entero para cantidad de vidas del jugador
        self.color = color # color --> String para elegir color del jugador (Red, Orange, Blue)
        self.width = width
        self.height = height        
        self.posX = width/2 # width --> ancho del juego para posicionar en el medio
        self.posY = height/1.10
        self.bk = bk
        self.sn = sn
        self.name = name
        
        self.listOfShoots = []
        self.points = 0

        self.playerImg = pygame.image.load("resources/players/player"+self.color+".png")
        self.rect = self.playerImg.get_rect()

        
    def drawPlayer(self):
        if self.lifes <= 0:
            self.playerImg = pygame.image.load("resources/players/playerDestroy.png")

        self.posX += self.velX
        if self.posX <= 0 or self.posX >= self.width:
            self.velX = 0

        self.rect.centerx = self.posX
        self.rect.centery = self.posY

        self.bk.drawObjet(self.playerImg, self.rect)

    def drawPlayerPoints(self):
        self.bk.drawText("resources/fonts/font.ttf",str(self.points),20,self.width/1.1,self.height/15)
    
    def drawPlayerName(self):
        self.bk.drawText("resources/fonts/font.ttf",str(self.name),20,self.width/1.4,self.height/15)

    def drawPlayerLife(self):
        playerImgLife = pygame.image.load("resources/players/player"+self.color+"Life.png")
        self.bk.drawObjet(playerImgLife,(self.width/40,self.height/25))
        self.bk.drawText("resources/fonts/font.ttf",str(self.lifes),20,self.width/10,self.height/15)
    
    def drawCollision(self):
        coll = pygame.image.load("resources/players/coll.png")
        self.bk.drawObjet(coll,self.rect)
        self.sn.playSound("resources/players/damage.ogg")
    
    def shoot(self):
        shoot = beam.Beam(self.posX,self.posY,self.velS,self.bk,"Player")
        self.listOfShoots.append(shoot)
        self.sn.soundShootPl()

    def setPlayer(self):
        self.drawPlayer()
        self.drawPlayerLife()
        self.drawPlayerPoints()
        self.drawPlayerName()