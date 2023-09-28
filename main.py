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

# Variables Globales
width = 800
height = 500
title = "Primer juego en python"
inGame = False

# Variables del entorno
fondoImagen = "resources/bks/bk.png"
fondoPosVertical = -500
fondoColor = (255,255,255)
fuenteTexto = "resources/fonts/font.ttf"

# Variables del Jugador
playerVelocidad = 0 # Múltiplos de 10
playerVelMovimiento = 10 
playerVelDisparo = 20
playerVidas = 5 
playerColor = "Red" # Red, Orange, Blue, Green

# Variables de Enemigos
enemigoVelMovimiento = 1
enemigoVelDisparo = -10
enemigoVidas = 3

# Variables de Asteroides
asteroideVelMovimiento = 5
asteroideVidas = 1

# Sonidos
sonidoDisparoPlayer = "resources/players/shoot.ogg"
sonidoDisparoEnemigo = "resources/enemies/shootEn.ogg"

# Sacando la variable display fuera de la función start
display = pygame.display.set_mode((width,height))

## IMPORTANTE siempre iniciar pygame antes de llamar cualquier función de este ##
pygame.init()

def start():
    #display = pygame.display.set_mode((width,height))
    bk1 = bk.Background(fondoImagen,playerVelocidad,fondoPosVertical,fondoColor,display)
    s1 = sounds.Sound(sonidoDisparoPlayer,sonidoDisparoEnemigo,"","","","")
    p1 = ply.Player(playerVelMovimiento,playerVelDisparo,0,playerVidas,playerColor,width,height,bk1,s1)
    lvl1= lvl.Level(0,3000,bk1)
    listEnemies = []
    listAsteroids = []
    event = events.Event(width,height,p1)
    
    pygame.display.set_caption(title)

    #
    #
    clock = pygame.time.Clock()
    second = 1
    cont = 1
    contS = 1
    contL = 1
    #
    #

    inGame = True
    while True:
        ctrlAst = randint(1,9999) #Control de aparición de asteroides 
        bk1.drawBackground()
        bk1.moveBackground()
        
        #
        #
        time = round(pygame.time.get_ticks()/1000)
        clock.tick(60)
        if second == time:
            cont = second
            contS = second
            second += 1
            contL += 1
            #print(str(second))
            #print(str(contL))
        #
        #
        
        if p1.lifes <= 0:
            inGame = False
            p1.velX = 0
            bk1.vel = 0
            bk1.drawText(fuenteTexto,"Game Over",40,width/2,height/2)
        elif p1.points >= lvl1.pointForWin:
            inGame = False
            p1.velX = 0
            bk1.vel = 0
            lvl1.winGame()
        elif p1.points >= lvl1.pointForUpLevel:
            if contL > 5:
                contL = 1
            if contL % 5 == 0:
                inGame = True
                lvl1.upLevel()
                listEnemies.clear()
                listAsteroids.clear()
            else:
                p1.velX = 0
                lvl1.nextLevel()
                inGame = False      

        p1.drawPlayer()
        p1.drawPlayerLife()
        p1.drawPlayerPoints()

        # Utilizar eventos predefinidos de pygame    
        for evt in pygame.event.get():
            # Cerrar ventana cuando el usuario clickee sobre la X
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # FUNC Mover player cuando se presiona flecha izquierda o derecha
            if inGame:
                if evt.type == KEYDOWN:
                    event.evtKeyDown(evt.key)
                if evt.type == KEYUP:
                    event.evtKeyUp(evt.key)
            
        #Cambiar CONT por Time
        if inGame:
            if ctrlAst % 90 == 0:
                aste2 = ast.Asteroid(asteroideVelMovimiento,asteroideVidas,width,height,bk1,s1)
                listAsteroids.append(aste2)
            if cont % 7 == 0:
                enmy = eny.Enemy(enemigoVelMovimiento,enemigoVelDisparo,enemigoVidas,width,height,bk1,s1)
                listEnemies.append(enmy)
                cont += 1

        if len(listAsteroids)>0:
            for a in listAsteroids:
                if not inGame:
                    a.velM = 0
                a.drawAsteroid()
                if a.rect.top > height+50:
                    listAsteroids.remove(a)
                if event.evtCollision(a.rect,p1.rect):
                    p1.lifes -= 1
                    p1.drawCollision()
                    listAsteroids.remove(a)
                if a.lifes == 0:
                    listAsteroids.remove(a)
                    p1.points += 10
                    a.destroy()


        if len(listEnemies)>0:
            for e in listEnemies:
                if not inGame:
                    e.velM = 0
                    e.velX = 0
                    e.velS = 0
                else:
                    #Cambiar contS por Time
                    if contS % 5 == 0:    
                        if len(e.listOfShoots) == 0:    
                            e.shoot()
                    event.evtShooting(e,p1)
                e.drawEnemy()
                if e.rect.top > height+50:
                    listEnemies.remove(e)
                if e.lifes == 0:
                    listEnemies.remove(e)
                    p1.points += 100

                if event.evtCollision(e.rect,p1.rect):
                    e.enemyNum = 6
                    p1.lifes -= 1
                    p1.drawCollision()
                    listEnemies.remove(e)
        
        event.evtShootingPlayer(p1,listEnemies,listAsteroids)

        pygame.display.update()    

def main_menu():
    # Fondo del menu, igual que en el juego pero sin movimiento
    bk_menu = bk.Background(fondoImagen,playerVelocidad,fondoPosVertical,fondoColor,display)

    # Definiendo botones
    start_button = btn.Button(width/2,height*0.4,display)
    quit_button = btn.Button(width/2,height*0.5,display)

    # Título de la ventana
    pygame.display.set_caption("Menu principal")

    while True:
        # Dibujar fondo
        bk_menu.drawBackground()

        # Dibujar titulo del juego
        bk_menu.drawText(fuenteTexto,"Mein Teil",70,width/2,height*0.2)

        # Dibujar botones
        if start_button.draw_text_button("START",fuenteTexto,40):
            start()
        if quit_button.draw_text_button("QUIT",fuenteTexto,40):
            pygame.quit()
            sys.exit()
        
        for evt in pygame.event.get():
            # Cerrar ventana cuando el usuario clickee sobre la X
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        # Refrescar pantalla
        pygame.display.update()

main_menu()

#start()
