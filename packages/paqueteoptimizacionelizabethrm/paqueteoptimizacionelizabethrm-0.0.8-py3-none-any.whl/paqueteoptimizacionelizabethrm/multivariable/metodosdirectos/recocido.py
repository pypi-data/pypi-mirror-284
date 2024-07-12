import numpy as np

def tweak(X):
    """
    Función que aplica una pequeña perturbación aleatoria a la matriz X.

    Parameters:
    X : numpy array
        Matriz de entrada a la cual se le aplicará la perturbación.

    Returns:
    numpy array
        Matriz perturbada con valores aleatorios uniformemente distribuidos dentro del rango [-0.5, 0.5].
    """
    return X + np.random.uniform(-0.5, 0.5, size=X.shape)

# Algoritmo de Recocido Simulado
def simulated_annealing(f, x0, alpha, T_initial, T_min, metropolis_size):
    """
    Implementación del algoritmo de Recocido Simulado para optimización.

    Parameters:
    f : function
        Función objetivo que se desea minimizar.
    x0 : list or numpy array
        Punto inicial de la búsqueda.
    alpha : float
        Factor de enfriamiento para la temperatura.
    T_initial : float
        Temperatura inicial.
    T_min : float
        Temperatura mínima en la que se detiene la búsqueda.
    metropolis_size : int
        Número de iteraciones por cada temperatura.

    Returns:
    numpy array, list
        El mejor punto encontrado y el historial de puntos explorados durante la búsqueda.
    """
    X = np.array(x0)  # Punto inicial
    Best = np.array(x0)  # Mejor punto encontrado
    T = T_initial  # Temperatura inicial
    history = [X.copy()]  # Historial de puntos explorados

    while T > T_min:
        for _ in range(metropolis_size):
            U = tweak(X)  # Generar una perturbación aleatoria
            if f(U) < f(Best):  # Actualizar el mejor punto si encontramos una mejora
                Best = U
            # Aplicar el criterio de aceptación de Metropolis
            if f(U) < f(X) or np.exp(-(f(U) - f(X)) / T) >= np.random.uniform():
                X = U  # Aceptar el nuevo punto U
            history.append(X.copy())  # Registrar el punto explorado
        T *= alpha  # Enfriar la temperatura

    return Best, history
