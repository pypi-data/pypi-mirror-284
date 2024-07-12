import numpy as np

def delta_x_func(x):
    """
    Función que determina el valor de delta_x en función de x.
    
    Parámetros:
    x (float): El punto en el cual se desea determinar delta_x.
    
    Retorna:
    float: El valor de delta_x basado en x.
    """
    return 0.01 * abs(x) if abs(x) > 0.01 else 0.0001  # Regla para determinar delta_x

def central_difference_f_prime(f, x, delta_x):
    """
    Calcula la derivada primera de una función en un punto dado utilizando el método de diferencias centrales.
    
    Parámetros:
    f (callable): La función objetivo cuya derivada se quiere calcular.
    x (float): El punto en el cual se desea calcular la derivada.
    delta_x (float): El pequeño incremento alrededor de x.
    
    Retorna:
    float: Aproximación de la derivada primera de la función en x.
    """
    return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

def bisection_method(funcion, a, b, epsilon, delta_x, max_iteraciones=10000):
    """
    Método de bisección para encontrar un intervalo que contiene un mínimo local de una función dada.
    
    Parámetros:
    funcion (callable): La función objetivo que se desea minimizar.
    a (float): Límite inferior del intervalo inicial.
    b (float): Límite superior del intervalo inicial.
    epsilon (float): La tolerancia para la longitud del intervalo y el valor de la derivada.
    delta_x (float): El pequeño incremento utilizado para calcular la derivada.
    max_iteraciones (int, opcional): El número máximo de iteraciones permitidas (por defecto es 10000).
    
    Retorna:
    tuple: Un intervalo (x1, x2) que contiene un mínimo local de la función.
    """
    x1 = a  # Inicialización del límite inferior del intervalo
    x2 = b  # Inicialización del límite superior del intervalo
    
    # Verificación de las condiciones iniciales
    #if (central_difference_f_prime(funcion, a, delta_x) < 0) and (central_difference_f_prime(funcion, b, delta_x) > 0):
    #    epsilon = epsilon  # La función cumple con la condición requerida
    #else:
    #    raise ValueError("La función no cumple con la condición f'(a) < 0 y f'(b) > 0")
    
    iteraciones = 0  # Inicialización del contador de iteraciones

    while abs(x1 - x2) > epsilon and iteraciones < max_iteraciones:
        z = (x1 + x2) / 2  # Cálculo del punto medio del intervalo
        f_prima_z = central_difference_f_prime(funcion, z, delta_x)  # Derivada primera en z

        if abs(f_prima_z) <= epsilon:
            return z, z  # Si la derivada en z es suficientemente pequeña, retornar z como el mínimo

        if f_prima_z < 0:
            x1 = z  # Ajuste del límite inferior del intervalo
        else:
            x2 = z  # Ajuste del límite superior del intervalo

        iteraciones += 1  # Incremento del contador de iteraciones

    return x1, x2  # Retorno del intervalo final que contiene el mínimo
