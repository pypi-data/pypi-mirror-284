import numpy as np
import matplotlib.pyplot as plt

# La función `exhaustive_search_method` realiza una búsqueda exhaustiva para encontrar un intervalo [x1, x3]
# donde una función dada `funcion` tiene un mínimo local. Si no se encuentra tal intervalo, devuelve None.
# 
# Parámetros:
# - a: límite inferior del intervalo de búsqueda.
# - b: límite superior del intervalo de búsqueda.
# - precision: el tamaño del paso para la búsqueda.
# - funcion: la función que se va a minimizar.

def exhaustive_search_method(a, b, precision, funcion):
    # Calcula el número de pasos n basado en la precisión deseada.
    n = (2/precision)*(b - a)
    # Calcula el incremento Delta_x basado en el número de pasos n.
    Delta_x = (b - a) / n
    # Inicializa los puntos x1, x2 y x3.
    x1 = a
    x2 = x1 + Delta_x
    x3 = x2 + Delta_x
    
    # Bucle de búsqueda.
    while True:
        # Comprueba si x2 es un mínimo local.
        if funcion(x1) >= funcion(x2) <= funcion(x3):
            # Devuelve el intervalo [x1, x3] que contiene el mínimo local.
            return x1, x3
        else:
            # Mueve los puntos x1, x2 y x3 un paso adelante.
            x1 = x2
            x2 = x3
            x3 = x2 + Delta_x
            # Si x3 ha alcanzado o superado el límite superior b, devuelve None.
            if x3 >= b:
                return None
