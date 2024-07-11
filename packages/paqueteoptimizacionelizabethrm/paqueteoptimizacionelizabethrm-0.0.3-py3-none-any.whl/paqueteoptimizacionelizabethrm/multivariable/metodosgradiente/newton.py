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
        f_x1 = central_difference_f_prime(funcion, x1, delta_x)
        f_x2 = central_difference_f_prime(funcion, x2, delta_x)
        if abs(f_x1 - f_x2) < 1e-10:
            raise ValueError("La función no cumple con la condición f'(a) < 0 y f'(b) > 0")
        
        z = x2 - (f_x2 / ((f_x2 - f_x1) / (x2 - x1)))
        f_prima_z = central_difference_f_prime(funcion, z, delta_x)

        if abs(f_prima_z) <= epsilon:
            return z, z 

        if f_prima_z < 0:
            x1 = z
        else:
            x2 = z

        iteraciones += 1

    return (x1 + x2) / 2

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
        
def hessian_matrix(f, x, deltaX):
    """
    Calcula la matriz hessiana de una función f en un punto x dado.

    Parámetros:
    f (callable): Función cuya matriz hessiana se desea calcular.
    x (array-like): Punto en el cual se evalúa la matriz hessiana.
    deltaX (float): Paso para la aproximación numérica de las derivadas parciales.

    Retorna:
    list of list: Matriz hessiana de f en x.
    """
    fx = f(x)  # Valor de la función en el punto x
    N = len(x)  # Dimensión del espacio de entrada (número de variables)
    H = []  # Inicializar la matriz hessiana como una lista vacía

    # Calcular cada elemento de la matriz hessiana
    for i in range(N):
        hi = []  # Lista para almacenar las segundas derivadas parciales respecto a cada variable
        for j in range(N):
            if i == j:
                # Calcular la segunda derivada parcial respecto a la misma variable (diagonal principal)
                xp = x.copy()
                xn = x.copy()
                xp[i] = xp[i] + deltaX
                xn[i] = xn[i] - deltaX
                hi.append((f(xp) - 2 * fx + f(xn)) / (deltaX**2))
            else:
                # Calcular la segunda derivada parcial cruzada respecto a dos variables diferentes
                xpp = x.copy()
                xpn = x.copy()
                xnp = x.copy()
                xnn = x.copy()
                
                xpp[i] = xpp[i] + deltaX
                xpp[j] = xpp[j] + deltaX

                xpn[i] = xpn[i] + deltaX
                xpn[j] = xpn[j] - deltaX

                xnp[i] = xnp[i] - deltaX
                xnp[j] = xnp[j] + deltaX

                xnn[i] = xnn[i] - deltaX
                xnn[j] = xnn[j] - deltaX

                hi.append((f(xpp) - f(xpn) - f(xnp) + f(xnn)) / (4 * deltaX**2))

        H.append(hi)  # Agregar la lista de segundas derivadas parciales a la matriz hessiana

    return H


def gradiente(f, x, deltaX=0.001):
    """
    Calcula el gradiente de una función escalar f en un punto x dado.

    Parámetros:
    f (callable): Función escalar que se desea evaluar.
    x (array-like): Punto en el cual se evalúa el gradiente.
    deltaX (float): Paso para la aproximación numérica de las derivadas parciales.

    Retorna:
    list: Lista con los componentes del gradiente de f en x.
    """
    grad = []
    for i in range(0, len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i]+deltaX
        xn[i] = xn[i]-deltaX
        grad.append((f(xp)-f(xn))/(2*deltaX))
    return grad

def newton(funcion, x0, epsilon1, epsilon2, M, metodo):
    """
    Implementa el método de Newton para la optimización de funciones.

    Parámetros:
    funcion (callable): Función objetivo que se desea minimizar.
    x0 (array-like): Punto inicial de la búsqueda.
    epsilon1 (float): Tolerancia para la norma del gradiente que determina la convergencia.
    epsilon2 (float): Tolerancia para la diferencia relativa entre dos iteraciones consecutivas.
    M (int): Número máximo de iteraciones permitidas.
    metodo (str): Método de búsqueda de paso a utilizar ('fibonacci', 'newton', 'dorado', 'interval', 'bounding', 'exhaustiva', 'biseccion', 'secante').

    Retorna:
    np.ndarray: Mejor punto encontrado que aproxima el mínimo de la función.
    """
    terminar = False
    xk= x0
    k = 0
    while not terminar:
        grad = np.array(gradiente(funcion, xk))
        matriz_hessiana = hessian_matrix(funcion, xk, 0.001)
        hess_inv = np.linalg.inv(matriz_hessiana)

        if np.linalg.norm(grad) < epsilon1 or k >= M:
            terminar = True

        else:
            def alpha_function(alpha):
                return funcion(xk - alpha * np.dot(hess_inv, grad))
            
            if metodo == 'fibonacci':
                alpha = fibonacci_search(alpha_function, 0.0, 5.0, 20)
            elif metodo == 'newton':
                alpha = newton_raphson_method(alpha_function, initial_guess=1, delta_x_funcion=lambda x: epsilon2, epsilon=epsilon2)
            elif metodo == 'dorado':
                alpha = busquedaDorada(alpha_function, epsilon=epsilon2, a=0.0, b=1.0)
            elif metodo == 'interval':
                alpha = interval_halving_method(a=0.0, b=1.0, funcion=alpha_function, epsilon=epsilon2)
            elif metodo == 'bounding':
                alpha = bounding_phase_method(alpha_function, 0, 0.001)
            elif metodo == 'exhaustiva':
                alpha = exhaustive_search_method(0.0, 1.0, epsilon2, alpha_function)
            elif metodo == 'biseccion':
                alpha = bisection_method(alpha_function, 1, 10, epsilon2, delta_x=0.0001)
            elif metodo == 'secante':
                alpha = secant_method(alpha_function, 1, 10, epsilon2, delta_x=0.0001)
            #matriz_hessiana = hessian_matrix(funcion, xk, 0.001)
            x_k1 = xk - (alpha*np.dot(np.linalg.inv(matriz_hessiana), grad))
            #print(xk, alpha, grad, x_k1)
            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 1e-10) <= epsilon2:
                terminar = True
            k= k + 1
            xk=  x_k1

    return xk

