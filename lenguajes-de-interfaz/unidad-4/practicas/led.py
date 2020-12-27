#!/usr/bin/python3
# coding: utf-8

import tkinter
from tkinter import *
from time import sleep
from pyfirmata import Arduino, util

# Configuración de la placa Arduino.
board = Arduino('/dev/ttyACM0')
sleep(5)

# Configuración de los pines de los led.
ROJO = 11
VERDE = 10
AZUL = 9

# Función para cambiar el led a color Rojo.
def rojo():
    board.digital[ROJO].write(0)
    board.digital[VERDE].write(1)
    board.digital[AZUL].write(1)

# Función para cambiar el led a color Verde.
def verde():
    board.digital[ROJO].write(1)
    board.digital[VERDE].write(0)
    board.digital[AZUL].write(1)

# Función para cambiar el led a color Azul.
def azul():
    board.digital[ROJO].write(1)
    board.digital[VERDE].write(1)
    board.digital[AZUL].write(0)

# Función para cambiar el led a color Violeta.
def violeta():
    board.digital[ROJO].write(0)
    board.digital[VERDE].write(1)
    board.digital[AZUL].write(0)

# Función para cambiar el led a color Amarillo.
def amarillo():
    board.digital[ROJO].write(0)
    board.digital[VERDE].write(0)
    board.digital[AZUL].write(1)

# Función para cambiar el led a color Azul Marino.
def azul_marino():
    board.digital[ROJO].write(1)
    board.digital[VERDE].write(0)
    board.digital[AZUL].write(0)

# Función para cambiar el led a color Blanco.
def blanco():
    board.digital[ROJO].write(0)
    board.digital[VERDE].write(0)
    board.digital[AZUL].write(0)

root = Tk()
root.title("Control de colores RGB")
root.geometry("465x225")
root.configure(bg="#d3abf5")

color_boton = "#9C7FB5"
color_letra = "#2E2536"

btn_rojo = Button(root, text="Cambiar a color Rojo.", bg=color_boton, fg=color_letra,
                  command=lambda: rojo())
btn_rojo.grid(column=1, row=1, ipadx=24, pady=3, padx=3)

btn_verde = Button(root, text="Cambiar a color Verde.", bg=color_boton, fg=color_letra,
command=lambda: verde())
btn_verde.grid(column=1, row=2, ipadx=20, pady=3, padx=3)

btn_azul = Button(root, text="Cambiar a color Azul.", bg=color_boton, fg=color_letra,
command=lambda: azul())
btn_azul.grid(column=1, row=3, ipadx=24, pady=3, padx=3)

btn_violeta = Button(root, text="Cambiar a color Violeta.", bg=color_boton, fg=color_letra,
command=lambda: violeta())
btn_violeta.grid(column=2, row=1, ipadx=25, pady=3, padx=3)

btn_amarillo = Button(root, text="Cambiar a color Amarillo.", bg=color_boton, fg=color_letra,
command=lambda: amarillo())
btn_amarillo.grid(column=2, row=2, ipadx=20, pady=3, padx=3)

btn_azul_marino = Button(root, text="Cambiar a color Azul Marino.", bg=color_boton, fg=color_letra,
command=lambda: azul_marino())
btn_azul_marino.grid(column=2, row=3, ipadx=10, pady=3, padx=3)

btn_blanco = Button(root, text="Cambiar a color Blanco.", bg=color_boton, fg=color_letra,
command=lambda: blanco())
btn_blanco.grid(column=2, row=4, ipadx=25, pady=3, padx=3)

root.mainloop()
