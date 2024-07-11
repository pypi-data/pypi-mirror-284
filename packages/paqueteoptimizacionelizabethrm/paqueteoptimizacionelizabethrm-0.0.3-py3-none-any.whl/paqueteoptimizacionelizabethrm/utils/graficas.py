import numpy as np
import matplotlib.pyplot as plt

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

def plot_rangos_minimos(funcion, a, b, precisiones, initial_guess, metodo_optimizacion):
    """
    Grafica la función y los puntos mínimos encontrados para distintas precisiones de un método de optimización dado.

    Parámetros:
    funcion (callable): Función objetivo que se desea minimizar.
    a (float): Límite inferior del rango de búsqueda.
    b (float): Límite superior del rango de búsqueda.
    precisiones (list): Lista de precisiones para las cuales se ejecutará el método de optimización.
    initial_guess (float): Valor inicial para el método de optimización.
    metodo_optimizacion (callable): Función que realiza el método de optimización sobre la función dada.
    """
    x_valores = np.linspace(a, b, 1000)
    y_valores = funcion(x_valores)

    plt.plot(x_valores, y_valores, label='Función')

    for precision in precisiones:
        rango_minimo = metodo_optimizacion(funcion, initial_guess, precision)
        if rango_minimo:
            min_x, max_x = rango_minimo
            plt.scatter([min_x, max_x], [funcion(min_x), funcion(max_x)], label=f'Rango mínimo ({precision})')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la función y puntos mínimos para distintas precisiones')
    plt.grid(True)
    plt.show()
