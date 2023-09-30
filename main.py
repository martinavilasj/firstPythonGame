#!/usr/bin/python
# coding=utf-8
# Importar al principio las librerias 
# pygame contiene las librerias para crear videojuegos
# sys nos sirve para manejar las ventanas del sistema operativo
# random es una libreria que nos permite crear número aleatorios
import pygame, sys, events
import player as ply
import background as bk
import enemy as eny
import asteroid as ast
import sounds
import level as lvl
from pygame.locals import *
from random import *
import button as btn
import controller as ctrl

# Variables Globales
width = 800
height = 500
title = "Primer juego en python" # Título de ventana
gameTitle = "JUEGUITO" # Título del juego
inGame = False

# Variables del entorno
fondoImagen = "resources/bks/bk-1.png"
fondoPosVertical = -500
fondoColor = (255,255,255)
fuenteTexto = "resources/fonts/font.ttf"

# Variables del Jugador
playerVelocidad = 5 # Múltiplos de 10
playerVelMovimiento = 10 
playerVelDisparo = 20
playerVidas = 3 
playerColor = "Red" # Red, Orange, Blue, Green
playerName = "Juanito"

# Variables de Enemigos
enemigoVelMovimiento = 1
enemigoVelDisparo = -10
enemigoVidas = 3

# Variables de Asteroides
asteroideVelMovimiento = 5
asteroideVidas = 1

# Variables de control
pointsForUpLevel = 1000
pointsForWin = 3000

# Sonidos
sonidoDisparoPlayer = "resources/players/shoot.ogg"
sonidoDisparoEnemigo = "resources/enemies/shootEn.ogg"

# Sacando la variable display fuera de la función start
display = pygame.display.set_mode((width,height))

# Clase eventos
event = events.Event('')

## IMPORTANTE siempre iniciar pygame antes de llamar cualquier función de este ##
pygame.init()

def start():
    bk1 = bk.Background(fondoImagen,playerVelocidad,fondoPosVertical,fondoColor,display)
    s1 = sounds.Sound(sonidoDisparoPlayer,sonidoDisparoEnemigo,"","","","")
    p1 = ply.Player(playerVelMovimiento,playerVelDisparo,0,playerVidas,playerColor,width,height,bk1,s1,playerName)
    lvl1= lvl.Level(pointsForUpLevel,pointsForWin,bk1,asteroideVelMovimiento,enemigoVelMovimiento,enemigoVelDisparo)
    listEnemies = []
    listAsteroids = []
    controller = ctrl.Controller(p1,bk1,listAsteroids,listEnemies,event,lvl1,s1,width,height)

    pygame.display.set_caption(title)

    controller.controlTime()

    while True:
        bk1.drawBackground()
        bk1.moveBackground()
        # Control de eventos
        event.evt = pygame.event.get()
        event.evtGeneral()
        
        p1.setPlayer()

        controller.control_lvl()
        if controller.inGame:
            event.evtInGame(width,height,p1)
            controller.generate_asteroids(asteroideVidas)
            controller.generate_enemies(enemigoVidas)
        
        controller.updateTime()

        controller.control_asteroids()
        controller.control_enemies()

        event.evtShootingPlayer(p1,listEnemies,listAsteroids)

        pygame.display.update()   

def select_player():
    run = True
    bk_select_menu = bk.Background(fondoImagen,playerVelocidad,fondoPosVertical,fondoColor,display)

    # Crear lista de naves a elegir
    list_players = [
        btn.Button(width*0.2,height*0.2,"playerRed",display),
        btn.Button(width*0.4,height*0.2,"playerBlue",display),
        btn.Button(width*0.6,height*0.2,"playerGreen",display),
        btn.Button(width*0.8,height*0.2,"playerOrange",display)
    ]

    start_button = btn.Button(width/2,height*0.8,"start",display)
    
    # Crear lista de naves en cada objeto particular
    for player in list_players:
        player.set_radio_buttons(list_players)
    # Seleccionar primer nave por defecto
    list_players[0].clicked = True

    # Usar global para cambiar el valor de la variable para todas las funciones
    global playerColor
    global playerName

    name_text = ''
    while run:
        event.evt = pygame.event.get()
        event.evtGeneral()

        bk_select_menu.drawBackground()
        bk_select_menu.drawText(fuenteTexto,"Selecciona una nave",35,width/2,height*0.4)
        bk_select_menu.drawText(fuenteTexto,"Nombre:",30,width*0.2,height*0.6)

        # Llamar a evento para la inserción de caracteres en pantalla
        name_text = event.evtInputText(name_text)
        bk_select_menu.drawLeftText(fuenteTexto,name_text,25,width*0.32,height*0.6)

        # Dibujar todas las naves y detectar cual fue elegida
        for player in list_players:
            player.draw_image_button("resources/players/")
            player.update_select()
            if player.clicked:
                playerColor = player.name.replace('player','')
        
        if start_button.draw_text_button("START",fuenteTexto,40):
            playerName = name_text
            run = False
            start()

        # Refrescar pantalla
        pygame.display.update()


def main_menu():
    run = True
    # Fondo del menu, igual que en el juego pero sin movimiento
    bk_menu = bk.Background(fondoImagen,playerVelocidad,fondoPosVertical,fondoColor,display)

    # Definiendo botones
    start_button = btn.Button(width/2,height*0.4,"start",display)
    quit_button = btn.Button(width/2,height*0.55,"quit",display)

    # Título de la ventana
    pygame.display.set_caption("Menu principal")

    while run:
        # Dibujar fondo
        bk_menu.drawBackground()

        event.evt = pygame.event.get()
        event.evtGeneral()

        # Dibujar titulo del juego
        bk_menu.drawText(fuenteTexto,gameTitle,70,width/2,height*0.2)

        # Dibujar botones
        if start_button.draw_text_button("START",fuenteTexto,40):
            run = False
            select_player()
        if quit_button.draw_text_button("QUIT",fuenteTexto,40):
            pygame.quit()
            sys.exit()

        # Refrescar pantalla
        pygame.display.update()

main_menu()
