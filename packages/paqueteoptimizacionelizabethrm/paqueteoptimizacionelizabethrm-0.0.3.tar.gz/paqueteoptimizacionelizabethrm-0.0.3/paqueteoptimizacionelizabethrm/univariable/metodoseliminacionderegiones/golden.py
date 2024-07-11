import numpy as np 
import math

def regla_eliminacion(x1, x2, fx1, fx2, a, b) -> tuple[float, float]:
    """
    Regla de eliminación para el método de búsqueda dorada.
    
    Parámetros:
    x1 (float): Primer punto de prueba en el intervalo.
    x2 (float): Segundo punto de prueba en el intervalo.
    fx1 (float): Valor de la función en x1.
    fx2 (float): Valor de la función en x2.
    a (float): Límite inferior del intervalo actual.
    b (float): Límite superior del intervalo actual.
    
    Retorna:
    tuple: Un nuevo intervalo (a, b) ajustado.
    """
    if fx1 > fx2:
        return x1, b  # Si f(x1) > f(x2), el nuevo intervalo es [x1, b]
    
    if fx1 < fx2:
        return a, x2  # Si f(x1) < f(x2), el nuevo intervalo es [a, x2]
    
    return x1, x2  # Si f(x1) == f(x2), el nuevo intervalo es [x1, x2]
    
def w_to_x(w: float, a, b) -> float:
    """
    Convierte un valor w en el intervalo [0, 1] a un valor en el intervalo [a, b].
    
    Parámetros:
    w (float): Valor en el intervalo [0, 1].
    a (float): Límite inferior del intervalo objetivo.
    b (float): Límite superior del intervalo objetivo.
    
    Retorna:
    float: Valor correspondiente en el intervalo [a, b].
    """
    return w * (b - a) + a  # Escala w al intervalo [a, b]
    
def busquedaDorada(funcion, epsilon: float, a: float=None, b: float=None) -> float:
    """
    Método de búsqueda dorada para encontrar un mínimo local de una función dada.
    
    Parámetros:
    funcion (callable): La función objetivo que se desea minimizar.
    epsilon (float): La tolerancia para la longitud del intervalo.
    a (float): Límite inferior del intervalo inicial.
    b (float): Límite superior del intervalo inicial.
    
    Retorna:
    float: Aproximación del punto que minimiza la función en el intervalo [a, b].
    """
    PHI = (1 + math.sqrt(5)) / 2 - 1  # Razón áurea
    aw, bw = 0, 1  # Intervalo inicial en términos de w
    Lw = 1  # Longitud del intervalo en términos de w
    k = 1  # Contador de iteraciones

    while Lw > epsilon:  # Repetir hasta que la longitud del intervalo sea menor que epsilon
        w2 = aw + PHI * Lw  # Segundo punto de prueba en términos de w
        w1 = bw - PHI * Lw  # Primer punto de prueba en términos de w
        # Actualizar los límites del intervalo utilizando la regla de eliminación
        aw, bw = regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), funcion(w_to_x(w2, a, b)), aw, bw)
            
        k += 1  # Incremento del contador de iteraciones
        Lw = bw - aw  # Actualización de la longitud del intervalo en términos de w

    # Retornar la media de los extremos del intervalo final, convertido al intervalo [a, b]
    return (w_to_x(aw, a, b) + w_to_x(bw, a, b)) / 2
