# coding: utf-8

import re

email = input("Ingresa el correo a evaluar: \n")

if re.fullmatch(r"^[a-z0-9_-]+(?:\.[a-z0-9_-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
    print("Correo valido")
else:
    print("Correo invalido")