#!/usr/bin/python3
# coding: utf-8

# Importación de librerías.
import tkinter
from time import sleep
from tkinter import *
from pyfirmata import Arduino,util

# Configuración de la placa Arduino.
#PUERTO = ""
#board = Arduino(PUERTO)
#sleep(5)

# Configuración de los pines de los led.


# Funciones para manejar la placa.


# Creación de la ventana.
root = Tk()
root.title("Control de luz en el hogar.")
root.geometry("800x500")

# Imagen Baño
canvas_bano = Canvas(root, width=400, height=250, highlightthickness=0)
canvas_bano.pack()
imagen_bano = PhotoImage(file="bano.gif")
canvas_bano.create_image(0, 0, anchor='nw', image=imagen_bano)
canvas_bano.place(x=0, y=0)

# Imagen Salon
canvas_salon = Canvas(root, width=400, height=250, highlightthickness=0)
canvas_salon.pack()
imagen_salon = PhotoImage(file="salon.gif")
canvas_salon.create_image(0, 0, anchor='nw', image=imagen_salon)
canvas_salon.place(x=400, y=0)

# Imagen Cocina
canvas_cocina = Canvas(root, width=400, height=250, highlightthickness=0)
canvas_cocina.pack()
imagen_cocina = PhotoImage(file="cocina.gif")
canvas_cocina.create_image(0, 0, anchor='nw', image=imagen_cocina)
canvas_cocina.place(x=0, y=250)

# Imagen Habitación
canvas_habitacion = Canvas(root, width=400, height=250, highlightthickness=0)
canvas_habitacion.pack()
imagen_habitacion = PhotoImage(file="dormitorio.gif")
canvas_habitacion.create_image(0, 0, anchor='nw', image=imagen_habitacion)
canvas_habitacion.place(x=400, y=250)

# Bombilla apagada
imagen_bombilla_apagada = PhotoImage(file="bombilla2.gif")
imagen_bombilla_encendida = PhotoImage(file="bombilla1.gif")
canvas_bano.create_image(0, 0, anchor='nw', image=imagen_bombilla_apagada)
canvas_cocina.create_image(0, 0, anchor='nw', image=imagen_bombilla_apagada)
canvas_habitacion.create_image(0, 0, anchor='nw', image=imagen_bombilla_apagada)
canvas_salon.create_image(0, 0, anchor='nw', image=imagen_bombilla_apagada)

root.mainloop()