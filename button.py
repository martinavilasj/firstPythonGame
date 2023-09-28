#!/usr/bin/python 
# Clase para crear y manejar botones
import pygame, sys
from pygame.locals import *

class Button:
    def __init__(self, x, y, display):
        self.x = x 
        self.y = y
        self.display = display
        self.clicked = False

    def is_pressed(self, rect):
        # get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
        
        return False

    def draw_text_button(self, text, font, size):
        font = pygame.font.Font(font,size) # font --> String para ruta de la fuente
        text = font.render(text,0,(255,255,255))
        rect = text.get_rect()
        rect.centerx = self.x 
        rect.centery = self.y
        self.display.blit(text,rect)
        # Checkear si el botón es presionado
        if self.is_pressed(rect): return True
        
    
        