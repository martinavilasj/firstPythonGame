#!/usr/bin/python 
# Clase para crear y manejar botones
import pygame, sys
from pygame.locals import *

class Button():
    def __init__(self, x, y, name, display):
        self.x = x 
        self.y = y
        self.name = name
        self.display = display
        self.rect = None
        self.img_button = self.name+".png"
        self.img_button_clicked = self.name+"_selected.png"
        self.image = self.img_button
        self.clicked = False
        self.buttons = None

    def is_pressed(self):
        # get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
        
        return False
    
    def set_radio_buttons(self, buttons):
        self.buttons = buttons

    def draw_text_button(self, text, font, size):
        font = pygame.font.Font(font,size) # font --> String para ruta de la fuente
        text = font.render(text,0,(255,255,255))
        self.rect = text.get_rect()
        self.rect.centerx = self.x 
        self.rect.centery = self.y
        self.display.blit(text,self.rect)
        # Checkear si el botón es presionado
        if self.is_pressed(): return True

    def draw_image_button(self, root):
        path = root+self.image
        button_img = pygame.image.load(path)
        self.rect = button_img.get_rect()
        self.rect.centerx = self.x 
        self.rect.centery = self.y
        self.display.blit(button_img,self.rect)
    
    def update_select(self):
        if self.is_pressed():
            for rb in self.buttons:
                rb.clicked = False
            self.clicked = True

        if self.clicked:
            self.image = self.img_button_clicked
        else:
            self.image = self.img_button

    
        