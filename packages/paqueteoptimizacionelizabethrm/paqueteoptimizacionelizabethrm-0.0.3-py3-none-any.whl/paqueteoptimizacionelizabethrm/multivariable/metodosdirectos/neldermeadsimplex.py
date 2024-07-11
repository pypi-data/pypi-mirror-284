import numpy as np
import math
import matplotlib.pyplot as plt

def simplex_inicial(alpha, punto_inicial):
    """
    Genera el simplex inicial para el algoritmo de Mead (Nelder-Mead).

    Parámetros:
    alpha (float): Parámetro de ajuste para calcular los puntos del simplex inicial.
    punto_inicial (list): Punto inicial alrededor del cual se genera el simplex.

    Retorna:
    list: Lista de puntos que conforman el simplex inicial.
    """
    N = len(punto_inicial)
    puntos_simplex = [punto_inicial]
    delta_1 = ((math.sqrt(N + 1) + N - 1)/(N*math.sqrt(2)))*alpha
    delta_2 = ((math.sqrt(N + 1)- 1)/(N * math.sqrt(2)))*alpha

    for i in range(N):
        nuevo_punto = punto_inicial.copy()
        for j in range(N):
            if j == i:
                nuevo_punto[j] += delta_1
            else:
                nuevo_punto[j] += delta_2
        puntos_simplex.append(nuevo_punto)

    return puntos_simplex

def mead_simplex(funcion, punto_inicial, epsilon, gamma, beta):
    """
    Implementación del método de Mead (Nelder-Mead) para optimización sin restricciones.

    Parámetros:
    funcion (callable): Función objetivo que se desea minimizar.
    punto_inicial (list): Punto inicial alrededor del cual se realiza la búsqueda.
    epsilon (float): Criterio de convergencia, diferencia mínima entre los valores de la función.
    gamma (float): Parámetro de reflexión.
    beta (float): Parámetro de contracción.

    Retorna:
    tuple: Punto óptimo encontrado y lista de simplex en cada iteración.
    """
    N = len(punto_inicial)
    simplex = simplex_inicial(0.5, punto_inicial)  # Genera el simplex inicial
    v = [funcion(punto) for punto in simplex]  # Evalúa la función en cada punto del simplex
    xl_i = np.argmin(v)  # Índice del punto de menor valor (mejor punto)
    xh_i = np.argmax(v)  # Índice del punto de mayor valor (peor punto)
    xg_i = None
    for i in range(len(v)):
        if v[i] < v[xh_i]:
            xg_i =  i
    
    if xg_i == None:
        xg_i = xl_i
   
    xc = np.mean(np.delete(simplex, xh_i, axis=0), axis=0)  # Calcula el centroide excluyendo el peor punto
    
    historial = [simplex.copy()]  # Inicializa el historial de simplex
    
    # Ciclo principal de optimización
    while (np.sqrt(np.sum((v - funcion(xc))**2) / (N + 1))) >= epsilon:
        v = [funcion(punto) for punto in simplex]  # Evalúa la función en cada punto del simplex
        xl_i = np.argmin(v)  # Índice del punto de menor valor (mejor punto)
        xh_i = np.argmax(v)  # Índice del punto de mayor valor (peor punto)
        
        for i in range(len(v)):
            if v[i] < v[xh_i]:
                xg_i =  i

        if xg_i == None:
            xg_i = xl_i        

        xc = np.mean(np.delete(simplex, xh_i, axis=0), axis=0)  # Calcula el centroide excluyendo el peor punto
        xr = 2 * xc - simplex[xh_i]  # Reflexión respecto al centroide
        x_new = xr
        fxr = funcion(xr)
        
        if fxr < v[xl_i]:
            x_new = (1 + gamma) * xc - gamma * simplex[xh_i]  # Expansión
        elif fxr >= v[xh_i]:
            x_new = (1 - beta) * xc + beta * simplex[xh_i]  # Contracción
        elif v[xg_i] < fxr and v[xg_i] < v[xh_i]:
            x_new = (1+beta)*xc - beta*simplex[xh_i]  # Contracción interna

        fxnew = funcion(x_new)
        simplex[xh_i] = x_new  # Actualiza el peor punto del simplex
        historial.append(simplex.copy())  # Guarda el estado del simplex en el historial

    return simplex[xl_i], historial  # Retorna el punto óptimo y el historial de simplex
