import numpy as np
import matplotlib.pyplot as plt

def interval_halving_method(a, b, funcion, epsilon):
    """
    Método de bisección para encontrar un intervalo que contiene un mínimo local de una función dada.
    
    Parámetros:
    a (float): El límite inferior del intervalo inicial.
    b (float): El límite superior del intervalo inicial.
    funcion (callable): La función objetivo que se desea minimizar.
    epsilon (float): La tolerancia para la longitud del intervalo.
    
    Retorna:
    tuple: Un intervalo (a, b) que contiene un mínimo local de la función.
    """
    x_m = (a + b) / 2  # Punto medio del intervalo inicial
    L = b - a  # Longitud del intervalo inicial
    
    funcion(x_m)  # Evaluación de la función en el punto medio (puede ser utilizado para otros propósitos)
    
    while abs(L) > epsilon:  # Repetir hasta que la longitud del intervalo sea menor que epsilon
        x_1 = a + (L / 4)  # Primer punto de prueba en el intervalo
        x_2 = b - (L / 4)  # Segundo punto de prueba en el intervalo
        
        r_x1 = funcion(x_1)  # Evaluación de la función en x_1
        r_x2 = funcion(x_2)  # Evaluación de la función en x_2
        
        if r_x1 < funcion(x_m):  # Si la función en x_1 es menor que en x_m
            b = x_m  # Ajustar el límite superior
            x_m = x_1  # Actualizar el punto medio
        elif r_x2 < funcion(x_m):  # Si la función en x_2 es menor que en x_m
            a = x_m  # Ajustar el límite inferior
            x_m = x_2  # Actualizar el punto medio
        else:
            a = x_1  # Ajustar el límite inferior
            b = x_2  # Ajustar el límite superior
        
        L = b - a  # Actualizar la longitud del intervalo
    
    return a, b  # Retornar el intervalo que contiene el mínimo local
