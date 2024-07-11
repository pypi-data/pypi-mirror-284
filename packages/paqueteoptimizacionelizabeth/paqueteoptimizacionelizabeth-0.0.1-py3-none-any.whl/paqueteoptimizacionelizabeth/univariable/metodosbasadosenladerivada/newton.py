
import numpy as np

def central_difference_f_prime(f, x, delta_x):
    """
    Calcula la derivada primera de una función en un punto dado utilizando el método de diferencias centrales.
    
    Parámetros:
    f (callable): La función objetivo cuya derivada se quiere calcular.
    x (float): El punto en el cual se desea calcular la derivada.
    delta_x (float): El pequeño incremento alrededor de x.
    
    Retorna:
    float: Aproximación de la derivada primera de la función en x.
    """
    return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

def central_difference_f_double_prime(f, x, delta_x):
    """
    Calcula la derivada segunda de una función en un punto dado utilizando el método de diferencias centrales.
    
    Parámetros:
    f (callable): La función objetivo cuya derivada se quiere calcular.
    x (float): El punto en el cual se desea calcular la derivada.
    delta_x (float): El pequeño incremento alrededor de x.
    
    Retorna:
    float: Aproximación de la derivada segunda de la función en x.
    """
    return (f(x + delta_x) - (2 * f(x)) + f(x - delta_x)) / (delta_x ** 2)

def newton_raphson_method(funcion, initial_guess, delta_x_funcion, epsilon, max_iteraciones=10000):
    """
    Implementa el método de Newton-Raphson para encontrar una raíz de una función.
    
    Parámetros:
    funcion (callable): La función objetivo cuya raíz se quiere encontrar.
    initial_guess (float): El valor inicial para comenzar la búsqueda de la raíz.
    delta_x_funcion (callable): Función que determina el valor de delta_x en función de x.
    epsilon (float): La tolerancia para el criterio de convergencia.
    max_iteraciones (int, opcional): El número máximo de iteraciones permitidas (por defecto es 10000).
    
    Retorna:
    float: Aproximación de la raíz de la función.
    """
    x = initial_guess  # Inicialización del valor de x
    k = 1  # Inicialización del contador de iteraciones
    while k < max_iteraciones:
        delta_x = delta_x_funcion(x)  # Cálculo de delta_x utilizando la función proporcionada
        f_primer_derivada_x = central_difference_f_prime(funcion, x, delta_x)  # Derivada primera en x
        f_doble_derivada_x = central_difference_f_double_prime(funcion, x, delta_x)  # Derivada segunda en x
        
        if abs(f_primer_derivada_x) < epsilon:  # Criterio de convergencia basado en la derivada primera
            return x
        
        x_siguiente = x - f_primer_derivada_x / f_doble_derivada_x  # Actualización de x usando Newton-Raphson
        
        if abs(x_siguiente - x) < epsilon:  # Criterio de convergencia basado en el cambio en x
            return x_siguiente
        
        x = x_siguiente  # Actualización del valor de x para la siguiente iteración
        k += 1  # Incremento del contador de iteraciones
    
    return x  # Retorno de x si no se alcanzó la convergencia en el número máximo de iteraciones

def delta_x_func(x):
    """
    Función que determina el valor de delta_x en función de x.
    
    Parámetros:
    x (float): El punto en el cual se desea determinar delta_x.
    
    Retorna:
    float: El valor de delta_x basado en x.
    """
    return 0.01 * abs(x) if abs(x) > 0.01 else 0.0001  # Regla para determinar delta_x
