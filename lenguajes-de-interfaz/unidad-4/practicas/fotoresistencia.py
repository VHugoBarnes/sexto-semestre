#!/usr/bin/python3
# coding: utf-8

# Importación de librerías.
import tkinter
from time import sleep
from tkinter import *
from pyfirmata import Arduino, util

# Configuración de la placa Arduino.
board = Arduino("COM5")

# Configuración de los pines.
ldr = board.get_pin('a:0:i')
iterator = util.Iterator(board)
iterator.start()

# dicts de paletas en hexadecimal
light = {
    "texto": "#b8b2a6",
    "fondo": "#fdfdf6",
    "boton": "#f4dada",
    "otros": "#683d94",
}

dark = {
    "texto": "#ee4540",
    "fondo": "#2d132c",
    "boton": "#c72c41",
    "otros": "#801336",
}

# Creación de ventana.
root = Tk()
root.title("Modo oscuro/Modo claro")
root.geometry("600x400")

while True:
    valor_ldr = ldr.read()
    texto1 = "Esta es una prueba de que se puede cambiar el tema de la app con una fotoresistencia, ahora estamos con un valor de luminosidad de: " + str(valor_ldr)
    if valor_ldr < 470:
        root.configure(bg=dark['fondo'])
        titulo = Label(root,
                    text="Modo oscuro activado",
                    fg=dark['texto'],
                    font=("Arial", 21, "bold"),
                    bg=dark['fondo']
                    )
        titulo.place(x=170, y=40)

        texto = Text( root,
                    fg=dark['texto'],
                    font=("Arial", 14),
                    bg=dark['fondo'],
                    wrap=WORD,
                    width=32,
                    height=4,
                    highlightthickness=0
                    )
        scroll = Scrollbar(root, command=texto.yview)
        texto.config()
        texto.place(x=140, y=100)
        texto.insert(END, texto1)

        boton = Button(root,
                    text="Soy un botón :o",
                    bg=dark['boton'],
                    fg=dark['otros'],
                    bd=0,
                    highlightthickness=0
                    )
        boton.place(x=240, y=350)
    elif valor_ldr > 470:
        root.configure(bg=light['fondo'])
        titulo = Label(root,
                    text="Modo claro activado",
                    fg=light['texto'],
                    font=("Arial", 21, "bold"),
                    bg=light['fondo']
                    )
        titulo.place(x=170, y=40)

        texto = Text( root,
                    fg=light['texto'],
                    font=("Arial", 14),
                    bg=light['fondo'],
                    wrap=WORD,
                    width=32,
                    height=4,
                    highlightthickness=0
                    )
        scroll = Scrollbar(root, command=texto.yview)
        texto.config()
        texto.place(x=140, y=100)
        texto.insert(END, texto1)

        boton = Button(root,
                    text="Soy un botón :o",
                    bg=light['boton'],
                    fg=light['otros'],
                    bd=0,
                    highlightthickness=0
                    )
        boton.place(x=240, y=350)
        
    board.exit()
    root.mainloop()
