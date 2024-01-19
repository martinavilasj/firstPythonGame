# coding=utf-8

import pygame, sys
from pygame.locals import *
from random import *
import background, beam

class Enemy:
    def __init__(self,velM,velS,lifes,width,height,bk,sn):
        self.velM = velM # velM --> entero para la velocidad del jugador al presionar teclas de movimiento
        self.velS = velS # velS --> entero para velocidad del disparo
        self.velX = velM # velX --> controla los bordes de la pantalla
        self.lifes = lifes # lifes --> entero para cantidad de vidas del jugador
        #self.color = color # color --> String para elegir color del jugador (Red, Orange, Blue)
        self.width = width
        self.height = height         
        self.posX = choice([1,width/2,width/3,width/1.5,width]) # width --> ancho del juego para posicionar en el medio
        self.posY = -100
        self.bk = bk
        self.sn = sn # Objeto sonido
        self.listOfShoots = []
        self.enemyNum = self.enemyRandom()
        self.enemyImg = pygame.image.load("resources/enemies/enemy"+str(self.enemyNum)+".png")
        self.rect = self.enemyImg.get_rect()

    def drawEnemy(self):
        self.moveEnemy()

        self.rect.centerx = self.posX
        self.rect.centery = self.posY

        self.bk.drawObjet(self.enemyImg, self.rect)

    def enemyRandom(self):
        return randint(1,4)
    
    def shoot(self):
        shoot_img = pygame.image.load("resources/beam/fireEnemy.png")
        shoot = beam.Beam(self.posX,self.posY,self.velS,self.bk,shoot_img,"Enemy")
        self.listOfShoots.append(shoot)
        self.sn.soundShootEn()

    def moveEnemy(self):
        if self.posY < self.height+50:
            self.posY += self.velM
            
            if self.posX <= 0 or self.posX > self.width:
                self.velX = -(self.velX)
            self.posX += self.velX
    
    def getDamage(self,pj,beam):
        self.sn.playSound("resources/enemies/damageEn.ogg")
        self.lifes -= pj.damage

        img = pygame.image.load("resources/beam/damageEnemy.png")
        rect = img.get_rect()
        rect.left = beam.rect.left
        rect.top = self.posY

        self.bk.drawObjet(img,rect)
    
    def destroy(self):
        self.sn.playSound("resources/enemies/explosion.ogg")
