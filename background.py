# coding=utf-8
import pygame, sys
from pygame.locals import *

class Background:
    def __init__(self, img, vel, posY, color,display):
        self.img = pygame.image.load(img) # img --> ruta de imagen
        self.vel = vel # vel --> entero para velocidad de fondo
        self.posY = posY # posY --> entero para posición inicial del fondo
        self.posIn = posY
        self.color = color # color --> tupla para color de fondo
        self.display = display # Pantalla donde se van a dibujar los elementos

    def drawBackground(self):
        self.display.fill(self.color)
        self.display.blit(self.img,(0,self.posY))
    
    def drawObjet(self,obj,position):
        self.display.blit(obj,position)

    def drawText(self,font,text,size,posLeft,posTop):
        self.font = pygame.font.Font(font,size) # font --> String para ruta de la fuente
        text = self.font.render(text,0,(255,255,255))
        rect = text.get_rect()
        rect.centerx = posLeft
        rect.centery = posTop
        self.display.blit(text,rect)

    def drawLeftText(self,font,text,size,posLeft,posTop):
        self.font = pygame.font.Font(font,size) # font --> String para ruta de la fuente
        text = self.font.render(text,0,(255,255,255))
        rect = text.get_rect()
        rect.centery = posTop
        rect.left = posLeft
        self.display.blit(text,rect)
    
    def drawRightText(self,font,text,size,posLeft,posTop):
        self.font = pygame.font.Font(font,size) # font --> String para ruta de la fuente
        text = self.font.render(text,0,(255,255,255))
        rect = text.get_rect()
        rect.centery = posTop
        rect.right = posLeft
        self.display.blit(text,rect)

    def moveBackground(self):
        if self.posY<-50:
            self.posY+=self.vel
        else:
            self.posY=self.posIn   

