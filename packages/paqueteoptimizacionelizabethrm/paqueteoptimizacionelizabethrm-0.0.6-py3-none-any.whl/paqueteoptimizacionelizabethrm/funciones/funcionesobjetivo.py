
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

def funcion_clase(x):
    r = x**2 + 3
    return r

def funcion_lata(x):
    r = 2*np.pi*x**2+500/x
    return r

def funcion_caja(L):
    r = (-1)*((200*L)-(60*(L**2))+(4*(L**3)))
    return r

def funcion_1(x):
    r = (x**2)+(54/x)
    return r

def funcion_2(x):
    r = (x**3) + (2*x) -3
    return r

def funcion_3(x):
    r = (x**4) + (x**2) - 33
    return r

def funcion_4(x):
    r = (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)
    return r 

def rastrigin_function(x, A=10):
    n = len(x)
    return A * n + sum([xi**2 - A * np.cos(2 * np.pi * xi) for xi in x])

def ackley_function(X):
    x, y = X[0], X[1]
    a = 20
    b = 0.2
    c = 2 * np.pi
    
    t1 = -a * np.exp(-b * np.sqrt(0.5 * (x**2 + y**2)))
    t2 = -np.exp(0.5 * (np.cos(c * x) + np.cos(c * y)))
    r = t1 + t2 + a + np.e
    
    return r

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def rosenbrock_function(x):
    n = len(x)
    sumatoria = 0
    for i in range(n - 1):
        sumatoria += 100 * (x[i + 1] - x[i]**2)**2 + (1 - x[i])**2
    return sumatoria

def beale_function(x):
    x, y = x[0], x[1]
    t1 = (1.5 - x + x * y)**2
    t2 = (2.25 - x + x * y**2)**2
    t3 = (2.625 - x + x * y**3)**2
    r = t1 + t2 + t3
    return r

def goldstein_price_function(X):
    x, y = X[0], X[1]
    t1 = 1 + (x + y + 1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2)
    t2 = 30 + (2 * x - 3 * y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2)
    r = t1 * t2
    return r

def booth_function(X):
    x, y = X[0], X[1]
    t1 = (x + 2*y - 7)**2
    t2 = (2*x + y - 5)**2
    r = t1 + t2
    return r

def bukin_function_n6(X):
    x, y = X[0], X[1]
    t1 = 100 * np.sqrt(np.abs(y - 0.01 * x**2))
    t2 = 0.01 * np.abs(x + 10)
    r = t1 + t2
    return r

def matyas_function(X):
    x, y = X[0], X[1]
    result = 0.26 * (x**2 + y**2) - 0.48 * x * y
    return result

def matyas_function(X):
    x, y = X[0], X[1]
    result = 0.26 * (x**2 + y**2) - 0.48 * x * y
    return result

def levy_function(X):
    x, y = X[0], X[1]
    return np.sin(3*np.pi*x)**2 + (x-1)**2 * (1 + np.sin(3*np.pi*y)**2) + (y-1)**2 * (1 + np.sin(2*np.pi*y)**2)

def himmelblau_function(X):
    x = X[0]
    y = X[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def three_hump_camel_function(X):
    x = X[0]
    y = X[1]
    return 2 * x**2 - 1.05 * x**4 + x**6 / 6 + x * y + y**2

def easom_function(X):
    x = X[0]
    y = X[1]
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

def cross_in_tray_function(X):
    x = X[0]
    y = X[1]
    return -0.0001 * (np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))) + 1)**0.1

def eggholder_function(X):
    x = X[0]
    y = X[1]
    return -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))

def holder_table_function(X):
    x = X[0]
    y = X[1]
    return -np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1 - np.sqrt(x**2 + y**2) / np.pi)))

def mccormick_function(X):
    x = X[0]
    y = X[1]
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1

def schaffer_function_n2(X):
    x = X[0]
    y = X[1]
    numerator = np.sin(x**2 - y**2)**2 - 0.5
    denominator = (1 + 0.001 * (x**2 + y**2))**2
    return 0.5 + numerator / denominator

def schaffer_function_n4(X):
    x = X[0]
    y = X[1]
    numerador = np.cos(np.sin(np.abs(x**2 - y**2)))**2 - 0.5
    denominador = (1 + 0.001 * (x**2 + y**2))**2
    return 0.5 + numerador / denominador

def styblinski_tang_function(X):
    X, Y = X[0], X[1]
    return (X**4 - 16 * X**2 + 5 * X + Y**4 - 16 * Y**2 + 5 * Y) / 2


def shekel_function(x):
    m = 10  
    c = np.array([4, 2, 1, 4, 1, 2, 1, 4, 2, 1])  
    a = np.array([
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]) 

    result = 0
    for i in range(m):
        result += 1 / (c[i] + ((x[0] - a[0, i])**2 + (x[1] - a[1, i])**2))

    return result - 1

def rosenbrock_with_constraints(x):
    rosenbrock_value = (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2
    
    constraint1 = (x[0] - 1)**3 - x[1] + 1
    constraint2 = x[0] + x[1] - 2
    
    if constraint1 > 0 or constraint2 > 0:
        return 1e6  
    else:
        return rosenbrock_value

def rosenbrock_with_disk_constraint(x):
    rosenbrock_formula = (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2
    
    constraint = x[0]**2 + x[1]**2 - 2
    
    if constraint > 0:
        return 1e6  
    else:
        return rosenbrock_formula
    
def mishras_bird(x):
    r = np.sin(x[1]) * np.exp((1 - np.cos(x[0]))**2) + np.cos(x[0]) * np.exp((1 - np.sin(x[1]))**2) + (x[0] - x[1])**2
    
    constraint = (x[0] + 5)**2 + (x[1] + 5)**2
    
    if constraint >= 25:
        return 1e6
    else:
        return r
    
def townsend_with_constraints(x):
    def townsend_function(x):
        x1, y = x[0], x[1]
        return - (np.cos((x1 - 0.1) * y))**2 - x1 * np.sin(3 * x1 + y)

    def heart_constraint(x):
        x1, y = x[0], x[1]
        t = np.arctan2(y, x1)
        rhs = (2 * np.cos(t) - 0.5 * np.cos(2 * t) - 0.25 * np.cos(3 * t) - 0.125 * np.cos(4 * t))**2 + (2 * np.sin(t))**2
        return x1**2 + y**2 - rhs

    if heart_constraint(x) >= 0:
        return 1e6 
    else:
        return townsend_function(x)
    
def gomez_levy_with_constraints(x):
    x1, y = x[0], x[1]
    
    f = 4 * x1**2 - 2.1 * x1**4 + (1/3) * x1**6 + x1 * y - 4 * y**2 + 4 * y**4
    
    constraint = -np.sin(4 * np.pi * x1) + 2 * np.sin(2 * np.pi * y)**2 - 1.5
    
    if constraint > 0:
        return 1e6
    else:
        return f
    
def simionescu_with_constraints(x):
    x1, y = x[0], x[1]
    simionescu_value = 0.1 * x1 * y
    r_T = 1
    r_S = 0.2
    n = 8
    
    theta = np.arctan2(y, x1)
    constraint_value = (r_T + r_S * np.cos(n * theta))**2 - (x1**2 + y**2)
    
    if constraint_value < 0:
        return 1e6  
    else:
        return simionescu_value
    
