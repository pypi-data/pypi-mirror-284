import numpy as np 
import math

def bounding_phase_method(funcion, initial_guess, Delta):
    k = 0
    if (funcion(initial_guess - abs(Delta))) >= (funcion(initial_guess)) >= (funcion(initial_guess + abs(Delta))):
        Delta = Delta * 1
    elif (funcion(initial_guess - abs(Delta))) <= (funcion(initial_guess)) <= (funcion(initial_guess + abs(Delta))):
        Delta = Delta * -1
    else:
        return ValueError(".")

    x_actual = initial_guess
    while True:
        x_nuevo = x_actual + 2**k * Delta 
        if funcion(x_nuevo) < funcion(x_actual):
            k += 1
            x_actual = x_nuevo
        else:
            return ((x_actual - 2**(k-1) * Delta + x_actual + 2**k * Delta))/2
        
def interval_halving_method(a, b, funcion, epsilon):
    x_m = (a + b) / 2
    L = b - a
    funcion(x_m)
    while abs(L) > epsilon:
        x_1 = a + (L / 4)
        x_2 = b - (L / 4)
        r_x1 = funcion(x_1)
        r_x2 = funcion(x_2)
        if r_x1 < funcion(x_m):
            b = x_m
            x_m = x_1
        elif r_x2 < funcion(x_m):
            a = x_m
            x_m = x_2
        else:
            a = x_1
            b = x_2
        L = b - a
    
    return (a + b)/2

def secant_method(funcion, a, b, epsilon, delta_x, max_iteraciones=10000):
    x1 = a
    x2 = b
    
    iteraciones = 0

    while abs(x1 - x2) > epsilon and iteraciones < max_iteraciones:
        z = x2 - (central_difference_f_prime(funcion, x2, delta_x)/((central_difference_f_prime(funcion, x2, delta_x)-central_difference_f_prime(funcion, x1, delta_x))/(x2-x1)))
        f_prima_z = central_difference_f_prime(funcion, z, delta_x)

        if abs(f_prima_z) <= epsilon:
            return z, z 

        if f_prima_z < 0:
            x1 = z
        else:
            x2 = z

        iteraciones += 1

    return (x1 +  x2)/2 

def bisection_method(funcion, a, b, epsilon, delta_x, max_iteraciones=10000):
    x1 = a
    x2 = b
    
    iteraciones = 0

    while abs(x1 - x2) > epsilon and iteraciones < max_iteraciones:
        z = (x1 + x2) / 2
        f_prima_z = central_difference_f_prime(funcion, z, delta_x)

        if abs(f_prima_z) <= epsilon:
            return z, z 

        if f_prima_z < 0:
            x1 = z
        else:
            x2 = z

        iteraciones += 1

    return (x1 + x2)/2

def exhaustive_search_method(a, b, precision, funcion):
    n = (2/precision)*(b - a)
    Delta_x = (b - a) / n
    x1 = a
    x2 = x1 + Delta_x
    x3 = x2 + Delta_x
    
    while True:
        if funcion(x1) >= funcion(x2) <= funcion(x3):
            return (x1 + x3)/2
        else:
            x1 = x2
            x2 = x3
            x3 = x2 + Delta_x
            if x3 >= b:
                return 0

def fibonacci(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 2):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n + 1]

def fibonacci_search(funcion, a, b, n):
    L = b - a
    k = 2
    
    while k <= n:
        Lk_asterisco = (fibonacci(n - k + 1) / fibonacci(n + 1)) * L
        x1 = a + Lk_asterisco
        x2 = b - Lk_asterisco
        
        fx1 = funcion(x1)
        fx2 = funcion(x2)
        
        if fx1 > fx2:
            a = x1
        elif fx1 < fx2:
            b = x2
        else:
            a = x1
            b = x2
        
        k += 1
    return (a + b)/2

def central_difference_f_prime(f, x, delta_x):
    return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

def central_difference_f_double_prime(f, x, delta_x):
    return (f(x + delta_x) - (2 * f(x)) + f(x - delta_x)) / (delta_x ** 2)

def newton_raphson_method(funcion, initial_guess, delta_x_funcion, epsilon, max_iteraciones=10000):
    x = initial_guess
    k = 1
    while k < max_iteraciones:
        delta_x = delta_x_funcion(x)
        f_primer_derivada_x = central_difference_f_prime(funcion, x, delta_x)
        f_doble_derivada_x = central_difference_f_double_prime(funcion, x, delta_x)
        
        if abs(f_primer_derivada_x) < epsilon:
            return x
        
        x_siguiente = x - f_primer_derivada_x / f_doble_derivada_x
        
        if abs(x_siguiente - x) < epsilon:
            return x_siguiente
        
        x = x_siguiente
        k += 1
    
    return x

def regla_eliminacion(x1, x2, fx1, fx2, a, b) -> tuple [float, float]:
    if fx1 > fx2:
        return x1, b
    
    if fx1 < fx2:
        return a, x2
    
    return x1, x2
    
def w_to_x(w:float, a, b) -> float:
    return w * (b-a) + a
    
def busquedaDorada(funcion, epsilon:float, a: float=None, b:float=None) -> float:
    PHI = (1 + math.sqrt(5))/ 2 - 1
    aw, bw = 0, 1
    Lw = 1
    k = 1

    while Lw > epsilon:
        w2 = aw + PHI*Lw
        w1 = bw - PHI*Lw
        aw, bw = regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)),
                                     funcion(w_to_x(w2, a, b)), aw, bw)
            
        k+=1
        Lw = bw - aw

    return (w_to_x(aw, a, b) +w_to_x(bw, a, b))/2
        
def gradiente(f, x, deltaX=0.001):
    """
    Calcula el gradiente de la función f en el punto x utilizando aproximación numérica de las derivadas parciales.

    Parámetros:
    f (callable): Función cuyo gradiente se desea calcular.
    x (array-like): Punto en el cual se evalúa el gradiente.
    deltaX (float): Paso para la aproximación numérica de las derivadas parciales.

    Retorna:
    list: Gradiente de f en x.
    """
    grad = []
    for i in range(0, len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i]+deltaX
        xn[i] = xn[i]-deltaX
        grad.append((f(xp)-f(xn))/(2*deltaX))
    return grad


def conjugate_gradient(f, x0, epsilon1, epsilon2, epsilon3, metodo):
    """
    Implementación del método de gradiente conjugado para minimización de funciones.

    Parámetros:
    f (callable): Función objetivo a minimizar.
    x0 (array-like): Punto inicial de búsqueda.
    epsilon1 (float): Tolerancia para el paso de línea.
    epsilon2 (float): Tolerancia para la norma del gradiente.
    epsilon3 (float): Tolerancia para la norma del gradiente.
    metodo (str): Método para la búsqueda de paso de línea ('biseccion', 'interval', 'bounding', 'secante', 'exhaustiva', 'dorado', 'fibonacci', 'newton').

    Retorna:
    array-like: Punto óptimo encontrado que minimiza la función f.
    """
    xk = x0  # Inicializar el punto inicial
    gk = np.array(gradiente(f, xk))  # Calcular el gradiente en el punto inicial
    sk = -gk  # Dirección de búsqueda inicial es opuesta al gradiente
    k = 0  # Contador de iteraciones
    terminar = False  # Bandera para terminar el ciclo
    
    while not terminar:
        if np.linalg.norm(gk) <= epsilon3:
            terminar = True
        
        def alpha_function(alpha):
            return f(xk + alpha * sk)
        
        # Selección del método para encontrar el paso de línea
        if metodo == 'biseccion':
            alpha = bisection_method(alpha_function, 0.0, 1.0, epsilon1, delta_x=0.0001)
        elif metodo == 'interval':
            alpha = interval_halving_method(0.0, 1.0, alpha_function, epsilon1)
        elif metodo == 'bounding':
            alpha = bounding_phase_method(alpha_function, 0, epsilon1)
        elif metodo == 'secante':
            alpha = secant_method(alpha_function, 0.0, 1.0, epsilon1, delta_x=0.0001)
        elif metodo == 'exhaustiva':
            alpha = exhaustive_search_method(0.0, 1.0, epsilon1, alpha_function)
        elif metodo == 'dorado':
            alpha = busquedaDorada(alpha_function, epsilon=epsilon1, a=0.0, b=1.0)
        elif metodo == 'fibonacci':
            alpha = fibonacci_search(alpha_function, 0.0, 5.0, 20)
        elif metodo == 'newton':
            alpha = newton_raphson_method(alpha_function, initial_guess=0.5, delta_x_funcion=lambda x: epsilon1, epsilon=epsilon1)
        
        # Calcular el siguiente punto usando el paso de línea encontrado
        xk1 = xk + alpha * sk
        
        # Condición de convergencia basada en la norma del cambio relativo
        if np.linalg.norm(xk1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
            terminar = True
        
        # Calcular el gradiente en el nuevo punto
        gk1 = np.array(gradiente(f, xk1))
        
        # Calcular el coeficiente beta para la dirección de búsqueda conjugada
        beta_k = np.dot(gk1, gk1) / np.dot(gk, gk)
        
        # Actualizar la dirección de búsqueda conjugada
        sk = -gk1 + beta_k * sk
        
        # Actualizar el punto actual
        xk = xk1
        gk = gk1

        k += 1  # Incrementar el contador de iteraciones
    
    return xk  # Retornar el punto óptimo encontrado