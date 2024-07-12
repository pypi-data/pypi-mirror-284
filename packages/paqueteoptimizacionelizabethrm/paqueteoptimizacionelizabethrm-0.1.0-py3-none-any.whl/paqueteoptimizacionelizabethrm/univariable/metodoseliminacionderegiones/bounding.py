
import numpy as np
import matplotlib.pyplot as plt

def bounding_phase_method(funcion, initial_guess, Delta):
    """
    Función para encontrar un intervalo que contiene un mínimo local de una función dada.
    
    Parámetros:
    funcion (callable): La función objetivo que se desea minimizar.
    initial_guess (float): La conjetura inicial para el punto de inicio.
    Delta (float): El tamaño del paso inicial.
    
    Retorna:
    tuple: Un intervalo (a, b) que contiene un mínimo local de la función.
    """
    k = 0  # Inicialización del contador de iteraciones
    
    # Determinación de la dirección del paso basado en los valores de la función en los puntos alrededor del initial_guess
    if (funcion(initial_guess - abs(Delta))) >= (funcion(initial_guess)) >= (funcion(initial_guess + abs(Delta))):
        Delta = Delta * 1  # Mantener la dirección positiva del paso
    elif (funcion(initial_guess - abs(Delta))) <= (funcion(initial_guess)) <= (funcion(initial_guess + abs(Delta))):
        Delta = Delta * -1  # Invertir la dirección del paso
    else:
        # Si no se puede determinar la dirección, se sugiere intentar con otros valores
        return ("Intente con otro valor de initial guess")
    
    x_actual = initial_guess  # Inicialización de la posición actual
    
    while True:
        x_nuevo = x_actual + 2**k * Delta  # Cálculo del nuevo punto
        if funcion(x_nuevo) < funcion(x_actual):
            # Si la función disminuye, continuar en la misma dirección
            k += 1
            x_actual = x_nuevo
        else:
            # Si la función no disminuye, retornar el intervalo encontrado
            print(x_actual - 2**(k-1) * Delta, x_actual + 2**k * Delta)
            return (x_actual - 2**(k-1) * Delta, x_actual + 2**k * Delta)
