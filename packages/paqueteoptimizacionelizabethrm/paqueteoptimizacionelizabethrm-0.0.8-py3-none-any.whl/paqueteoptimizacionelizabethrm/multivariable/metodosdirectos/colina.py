import numpy as np
import math
import matplotlib.pyplot as plt

def random_generation(x, sigma):
    """
    Genera un paso aleatorio para la optimización.

    Parámetros:
    x (array-like): Punto actual en el espacio de búsqueda.
    sigma (float): Desviación estándar para la distribución normal que genera el paso aleatorio.

    Retorna:
    np.ndarray: Nuevo punto generado como un paso aleatorio desde x.
    """
    x = np.array(x)  # Convertir a una matriz de NumPy
    return x + np.random.normal(0, sigma, size=x.shape)

def random_walk_colina(f, terminate, max_iter, x0, sigma):
    """
    Algoritmo de Random Walk para la optimización.

    Parámetros:
    f (callable): Función objetivo que se desea minimizar.
    terminate (callable): Función de terminación que determina cuándo detener el algoritmo.
    max_iter (int): Número máximo de iteraciones permitidas.
    x0 (array-like): Punto inicial de la búsqueda.
    sigma (float): Desviación estándar para generar pasos aleatorios.

    Retorna:
    tuple: Mejor punto encontrado y lista de puntos históricos durante la búsqueda.
    """
    historial = [x0]  # Lista para almacenar el historial de puntos durante la búsqueda
    x_best = x0  # Mejor punto encontrado inicializado con el punto inicial
    x_best_val = f(x0)  # Valor de la función en el mejor punto encontrado
    
    iter_count = 0  # Contador de iteraciones
    while not terminate(iter_count):  # Ciclo principal hasta que se cumpla el criterio de terminación
        x_next = random_generation(x_best, sigma)  # Generar el siguiente punto aleatorio
        f_next = f(x_next)  # Evaluar la función en el siguiente punto
        
        if f_next < x_best_val:  # Si el nuevo punto es mejor que el mejor encontrado hasta ahora
            x_best = x_next  # Actualizar el mejor punto
            x_best_val = f_next  # Actualizar el valor de la función en el mejor punto
        
        historial.append(x_best)  # Agregar el mejor punto al historial
        iter_count += 1  # Incrementar el contador de iteraciones
    
    return x_best, historial

# Ejemplo de criterio de terminación basado en el número máximo de iteraciones
def max_iterations_terminate(max_iter):
    """
    Criterio de terminación basado en el número máximo de iteraciones.

    Parámetros:
    max_iter (int): Número máximo de iteraciones permitidas.

    Retorna:
    callable: Función que verifica si el número actual de iteraciones ha alcanzado max_iter.
    """
    def terminate(iter_count):
        return iter_count >= max_iter  # Retorna True si se alcanza el número máximo de iteraciones
    
    return terminate
