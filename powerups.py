#!/usr/bin/python3
# Clase para generar power ups

from random import *
import pygame

class Powerup:
    def __init__(self,width,height,velocidad):
        self.lista_powerups = ["vida","veldisparo","power"]
        self.powerup = self.lista_powerups[randint(0,2)]
        self.image = pygame.image.load("resources/powerups/" + self.powerup + ".png")

        self.width = width
        self.height = height
        self.vel = velocidad

        self.pos_x = randint(50,self.width-50)
        self.pos_y = -100

        self.rect = self.image.get_rect()

        # Timer
        self.timer = {}

    def draw_powerup(self,bk):
        self.move_powerup()

        
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        bk.drawObjet(self.image, self.rect)
    
    def move_powerup(self):
        if self.pos_y < self.height+50:
            self.pos_y += self.vel

    def set_powerup(self, player):
        if self.powerup == "vida":
            player.lifes += 1
        elif self.powerup == "veldisparo":
            player.velS += 10
        elif self.powerup == "power":
            player.damage = 3
            player.powered = True
    
    def unset_powerup(self, player):
        if self.powerup == 'veldisparo':
            player.velS -= 10
        elif self.powerup == 'power':
            player.damage = 1
            player.powered = False

    def set_timer(self,time_start,time_stop):
        self.timer["time_start"] = time_start
        self.timer["time_stop"] = time_stop