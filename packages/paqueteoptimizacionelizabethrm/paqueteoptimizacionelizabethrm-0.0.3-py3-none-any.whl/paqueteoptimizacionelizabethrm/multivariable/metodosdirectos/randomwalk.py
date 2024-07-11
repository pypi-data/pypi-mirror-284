import numpy as np

# Algoritmo Random Walk con generación de pasos aleatorios
def random_walk(f, x0, max_iter, mu, sigma):
    """
    Implementa el algoritmo Random Walk para minimizar una función objetivo.

    Parámetros:
    f (func): Función objetivo que se desea minimizar.
    x0 (list or array): Punto de inicio del algoritmo.
    max_iter (int): Número máximo de iteraciones.
    mu (float): Media de la distribución normal para generar pasos aleatorios.
    sigma (float): Desviación estándar de la distribución normal para generar pasos aleatorios.

    Retorna:
    x_mejor (array): La mejor solución encontrada.
    history (list): Historial de puntos visitados durante la búsqueda.
    """
    
    # Inicializar el mejor punto y el punto actual con el punto de inicio
    x_mejor = np.array(x0)
    x_actual = np.array(x0)
    # Guardar el historial de puntos visitados, comenzando con el punto de inicio
    history = [x_actual.copy()]

    # Iterar hasta alcanzar el número máximo de iteraciones
    for _ in range(max_iter):
        # Generar un nuevo punto aleatorio basado en la distribución normal
        x_n = x_actual + np.random.normal(mu, sigma, size=x_actual.shape)
        # Si el nuevo punto es mejor que el mejor punto encontrado hasta ahora, actualizar el mejor punto
        if f(x_n) < f(x_mejor):
            x_mejor = x_n
        # Actualizar el punto actual con el nuevo punto generado
        x_actual = x_n
        # Agregar el nuevo punto al historial de puntos visitados
        history.append(x_actual.copy())

    # Retornar la mejor solución encontrada y el historial de puntos visitados
    return x_mejor, history

