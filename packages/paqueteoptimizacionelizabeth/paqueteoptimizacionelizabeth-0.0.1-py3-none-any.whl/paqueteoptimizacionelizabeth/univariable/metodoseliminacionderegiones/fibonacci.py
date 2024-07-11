import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    """
    Función para calcular el (n+1)-ésimo número de Fibonacci.
    
    Parámetros:
    n (int): El índice para el cual se desea calcular el número de Fibonacci.
    
    Retorna:
    int: El (n+1)-ésimo número de Fibonacci.
    """
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
    """
    Método de búsqueda de Fibonacci para encontrar un intervalo que contiene un mínimo local de una función dada.
    
    Parámetros:
    funcion (callable): La función objetivo que se desea minimizar.
    a (float): El límite inferior del intervalo inicial.
    b (float): El límite superior del intervalo inicial.
    n (int): Número de iteraciones (relacionado con la precisión deseada).
    
    Retorna:
    tuple: Un intervalo (a, b) que contiene un mínimo local de la función.
    """
    L = b - a  # Longitud del intervalo inicial
    k = 2  # Inicialización del contador de iteraciones
    
    while k <= n:
        Lk_asterisco = (fibonacci(n - k + 1) / fibonacci(n + 1)) * L  # Cálculo de la longitud reducida del intervalo
        x1 = a + Lk_asterisco  # Primer punto de prueba
        x2 = b - Lk_asterisco  # Segundo punto de prueba
        
        fx1 = funcion(x1)  # Evaluación de la función en x1
        fx2 = funcion(x2)  # Evaluación de la función en x2
        
        if fx1 > fx2:
            a = x1  # Ajuste del límite inferior
        elif fx1 < fx2:
            b = x2  # Ajuste del límite superior
        else:
            a = x1  # Ajuste de ambos límites
            b = x2
        
        k += 1  # Incremento del contador de iteraciones
    
    print(a, b)  # Impresión del intervalo final
    return (a, b)  # Retorno del intervalo final
