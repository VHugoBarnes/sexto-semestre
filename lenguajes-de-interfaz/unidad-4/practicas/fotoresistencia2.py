#!/usr/bin/python3
# coding: utf-8

# Importación de las librerías.
from time import sleep
from pyfirmata import Arduino, util
import pygame


# Configuración de la placa Arduino.
board = Arduino("COM5") # El puerto que tengas para el Arduino.

# Configuración de los pines.
ldr = board.get_pin('a:0:i')
iterator = util.Iterator(board)
iterator.start()

# dicts de paletas en hexadecimal
light = {
    "texto": (184, 178, 166),
    "fondo": (253, 253, 246),
    "boton": (244, 218, 218),
    "otros": (104, 61, 148),
}

dark = {
    "texto": (238, 69, 64),
    "fondo": (45, 19, 44),
    "boton": (199, 44, 65),
    "otros": (128, 19, 54),
}

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

fuente = pygame.font.SysFont("Arial", 21)

texto_oscuro = fuente.render("Modo oscuro activado", True, dark['texto'], dark['fondo'])
texto_claro = fuente.render("Modo claro activado", True, light['texto'], light['fondo'])
lectura = ""

terminado = False

while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True

    #valor_ldr = ldr.read()
    if valor_ldr < 470: # MODO OSCURO.
        screen.fill(dark['fondo'])
        screen.blit(texto_oscuro,
                    (300 - texto_oscuro.get_width() // 2, 140 - texto_oscuro.get_height() // 2))
        lectura = fuente.render("El nivel de luz es de: " + str(valor_ldr), True, dark['texto'], dark['fondo'])
        screen.blit(lectura,
                    (300 - lectura.get_width() // 2, 180 - lectura.get_height() // 2))

    if valor_ldr > 470: # MODO CLARO.
        screen.fill(light['fondo'])
        screen.blit(texto_claro,
                    (300 - texto_claro.get_width() // 2, 140 - texto_claro.get_height() // 2))
        lectura = fuente.render("El nivel de luz es de: " + str(valor_ldr), True, light['texto'], light['fondo'])
        screen.blit(lectura,
                    (300 - lectura.get_width() // 2, 180 - lectura.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
