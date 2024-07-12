import numpy as np
import matplotlib.pyplot as plt

from paqueteoptimizacionelizabethrm.univariable.metodosbasadosenladerivada import newton_raphson_method, secant_method, bisection_method
from paqueteoptimizacionelizabethrm.univariable.metodoseliminacionderegiones import fibonacci_search, bounding_phase_method, exhaustive_search_method, interval_halving_method, busquedaDorada
import matplotlib.pyplot as plt
import numpy as np

def grafica_2d_con_restricciones(func, x_range=(-10, 10), y_range=(-10, 10), resolution=400, constraint_value=1e6):
    """
    Genera una gráfica 2D de una función con restricciones para valores de x e y.

    Parámetros:
    func (callable): Función que devuelve el valor de la función en un punto dado.
    x_range (tuple, optional): Rango de valores de x para graficar (default=(-10, 10)).
    y_range (tuple, optional): Rango de valores de y para graficar (default=(-10, 10)).
    resolution (int, optional): Resolución de la grilla para la gráfica (default=400).
    constraint_value (float, optional): Valor de restricción para la función (default=1e6).
    """
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    posiciones = np.vstack([X.ravel(), Y.ravel()]).T

    Z = np.array([func(pos) if np.all(np.abs(pos) < constraint_value) else np.nan for pos in posiciones])
    Z = Z.reshape(X.shape)

    plt.figure(figsize=(8, 6))
    heatmap = plt.imshow(Z, extent=[x_range[0], x_range[1], y_range[0], y_range[1]], origin='lower', cmap='viridis', aspect='auto')
    plt.colorbar(heatmap)
    plt.title('Gráfica de función con restricciones')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def grafica_2d_no_restricciones(function, x_limits=(-10, 10), y_limits=(-10, 10), num_points=100):
    """
    Genera una gráfica 2D de una función sin restricciones explícitas para valores de x e y.

    Parámetros:
    function (callable): Función que devuelve el valor de la función en un punto dado.
    x_limits (tuple, optional): Límites de valores de x para graficar (default=(-10, 10)).
    y_limits (tuple, optional): Límites de valores de y para graficar (default=(-10, 10)).
    num_points (int, optional): Número de puntos en cada dimensión para la gráfica (default=100).
    """
    x = np.linspace(x_limits[0], x_limits[1], num_points)
    y = np.linspace(y_limits[0], y_limits[1], num_points)
    X, Y = np.meshgrid(x, y)
    Z = function([X, Y])
    
    plt.figure(figsize=(10, 8))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(label='f(x, y)')
    plt.title('Gráfica de la función')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def delta_x_func(x):
    return 0.01 * abs(x) if abs(x) > 0.01 else 0.0001

def plot_rangos_minimos(funcion, a, b, precisiones, initial_guess, nombre, n, delta):
    """
    Grafica la función y los puntos mínimos encontrados para distintas precisiones de un método de optimización dado.

    Parámetros:
    funcion (callable): Función objetivo que se desea minimizar.
    a (float): Límite inferior del rango de búsqueda.
    b (float): Límite superior del rango de búsqueda.
    precisiones (list): Lista de precisiones para las cuales se ejecutará el método de optimización.
    initial_guess (float): Valor inicial para el método de optimización.
    nombre (str): Nombre del método de optimización a utilizar.
    n (int): Número de iteraciones para el método Fibonacci.
    delta (float): Parámetro delta para métodos basados en la derivada.
    """
    x_valores = np.linspace(a, b, 100)
    y_valores = funcion(x_valores)

    plt.plot(x_valores, y_valores, label='Función')

    for precision in precisiones:

        if nombre == "secante":
            rango_minimo = secant_method(funcion, a, b, precision, delta_x_func(2))
        elif nombre == "bounding":
            rango_minimo = bounding_phase_method(funcion, initial_guess, delta_x_func(1))
        elif nombre == "exhaustiva":
            rango_minimo = exhaustive_search_method(a, b, precision, funcion)
        elif nombre == "fibonacci":
            rango_minimo = fibonacci_search(funcion, a, b, n)
        elif nombre == "bisection":
            rango_minimo = bisection_method(funcion, a, b, precision, delta)
        elif nombre == "newton":
            rango_minimo = newton_raphson_method(funcion, initial_guess, delta_x_funcion=lambda x: delta_x_func(x), epsilon=precision)
        elif nombre == "golden":
            rango_minimo = busquedaDorada(funcion, precision, a, b)
        elif nombre == "interval":
            rango_minimo = interval_halving_method(a, b, funcion, precision)
        else:
            raise ValueError(f"Método de optimización '{nombre}' no reconocido")

        if isinstance(rango_minimo, tuple):  # Verificar si rango_minimo es un iterable (tuple)
            min_x, max_x = rango_minimo
            plt.scatter([min_x, max_x], [funcion(min_x), funcion(max_x)], label=f'Rango mínimo ({precision})')
        elif isinstance(rango_minimo, float):
            plt.scatter([rango_minimo], [funcion(rango_minimo)], label=f'Rango mínimo ({precision})')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la función y puntos mínimos para distintas precisiones')
    plt.grid(True)
    plt.show()