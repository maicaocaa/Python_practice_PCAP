# esto es un modulo
# o main module o script, es primer modulo que se carga para empezar la aejecucion de la app.
# luego todos los modulos son un package y asi los modulos pueden lamarse igual en diferntes apckage sin generar conflictos.
# loc priemros modulos son 
# package evita coliniones y conflictos de nombre.
# ya tengo isntalado  python runtime enviroment
# tambein hay una python virtual machine
# la carga se separa en 2 fases diferenciadas

# tiene que tener un pyton doc string
# -------------------------
# Module Imports
# ---------------------------

# importaciones de modulso a utilizar
# import should be grouped in the following order:
#   starndar library imports
#   related third party imports
#   local apllication/library specific imports
# yout should put a blanc linke between each group of imports.
# https://docs.python.org/3/library/index.html
# https://peps.python.org/pep-0008/


import builtins
import calendar
import datetime
import math
import random
import statistics
import string

import planning         # custom
import mathutils        # custom module > mathutils.py
import strutils         # custom module > strutils.py
import convertutils     # custom module > convertutils.py



print (f"PI: {math.pi}")
print (math.e)
print (math.pow(2.3))
print(math.sqrt(4))


print("-" * 50)
print("Module:string")
print("-" * 50)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.capwords("maria cao caamaño"))

print("-" * 50)
print("Module:string")
print("-" * 50)
print(datetime.MINYEAR)
print(datetime.MAXYEAR)

print("-" * 50)
print("Module:planning")
print("-" * 50)
print(f"planning.current_year(): {planning.current_year()}")       #funcion a nivel modulo
print(planning.remaining_days()) 
print(planning.remaining_days()) 
print(planning.is_lap_year())    #funcion a nivel modulo invocado con argumento por defecto que es current_year
print(planning.is_lap_year(2024)) #funcion a nivel modulo invodaco con parametros de posicion
print(planning.is_lap_year(year=2024)) #funcion a nivel modulo invodaco argumento parametroo por nombre


