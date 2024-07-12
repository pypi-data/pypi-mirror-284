import numpy as np

def exploratory_move(xc, delta, function):
    """
    Realiza un movimiento exploratorio desde el punto xc en dirección delta para minimizar la función objetivo.

    Parámetros:
    xc (array-like): Punto actual en el espacio de búsqueda.
    delta (array-like): Vector de pasos para moverse en cada dirección.
    function (callable): Función objetivo que se desea minimizar.

    Retorna:
    tuple: Nuevo punto en el espacio de búsqueda, arreglo booleano indicando éxito de cada movimiento, punto anterior.
    """
    N = len(xc)  # Número de dimensiones
    xc_previous = xc.copy()  # Copia del punto actual como punto anterior
    success = np.zeros(N, dtype=bool)  # Arreglo para indicar éxito de cada movimiento
    
    # Iterar sobre cada dimensión
    for i in range(N):
        xi_plus_delta = xc.copy()
        xi_plus_delta[i] += delta[i]  # Moverse hacia adelante en la dirección i
        xi_minus_delta = xc.copy()
        xi_minus_delta[i] -= delta[i]  # Moverse hacia atrás en la dirección i
        
        # Evaluar la función en los puntos actual, adelante y atrás
        f = function(*xc)
        f_plus = function(*xi_plus_delta)
        f_minus = function(*xi_minus_delta)
        
        # Determinar cuál valor es el mínimo
        f_min = min(f, f_plus, f_minus)
        
        # Actualizar el éxito del movimiento y el punto actual si se encontró un mínimo diferente al punto actual
        if f_min == f:
            success[i] = False
        elif f_min == f_plus:
            xc = xi_plus_delta
            success[i] = True
        else:
            xc = xi_minus_delta
            success[i] = True
    
    return xc, success, xc_previous

def pattern_movement(x_current, x_previous):
    """
    Realiza el movimiento de patrón según el método de Hooke-Jeeves.

    Parámetros:
    x_current (array-like): Punto actual en el espacio de búsqueda.
    x_previous (array-like): Punto anterior en el espacio de búsqueda.

    Retorna:
    array-like: Nuevo punto calculado según el movimiento de patrón.
    """
    x_current = np.array(x_current)
    x_previous = np.array(x_previous)
    xp = x_current + ((x_current) - (x_previous))  # Calcula el nuevo punto como x_current + (x_current - x_previous)
    return xp

def hooke_jeeves(initial_point, deltas, alpha, epsilon, function):
    """
    Implementación del método de Hooke-Jeeves para minimización de funciones.

    Parámetros:
    initial_point (array-like): Punto inicial de búsqueda.
    deltas (array-like): Vector de pasos para moverse en cada dirección.
    alpha (float): Factor de reducción de pasos en caso de fracaso en la búsqueda.
    epsilon (float): Tolerancia para detener el algoritmo.
    function (callable): Función objetivo que se desea minimizar.

    Retorna:
    tuple: Punto óptimo encontrado que minimiza la función, número de iteraciones realizadas.
    """
    k = 0  # Inicialización del contador de iteraciones
    x_current = initial_point  # Punto actual de búsqueda inicial
    
    # Iterar mientras el máximo de los pasos sea mayor o igual a la tolerancia epsilon
    while max(abs(np.array(deltas))) >= epsilon:
        
        # Realizar el movimiento exploratorio desde el punto actual
        x_next, success, x_previous = exploratory_move(x_current, deltas, function)
        
        # Si hubo éxito en algún movimiento, actualizar el punto actual
        if success.any():
            x_current = x_next
            k += 1
            
            # Calcular el nuevo punto según el movimiento de patrón
            x_new_position = pattern_movement(x_current, x_previous)
            
            # Realizar un segundo movimiento exploratorio desde el nuevo punto
            x_new_position2, success, xp = exploratory_move(x_new_position, deltas, function)
            
            # Si el valor de la función en el segundo punto es menor que en el punto actual, actualizar el punto actual
            if function(*x_new_position2) < function(*x_current):
                x_current = x_new_position
        
        else:
            deltas = np.array(deltas) / alpha  # Reducir los pasos en caso de fracaso en el movimiento exploratorio
    
    return x_current, k  # Retornar el punto óptimo encontrado y el número de iteraciones realizadas
