"""
Módulo prediccion: regresión lineal y = a*x + b ajustada por tanteo.
"""

# Parámetros elegidos por tanteo (ver bitácora en el README).
A = 2.0
B = -3952.0


def calcular_y(valores_x, a, b):
    """Retorna la lista de valores y = a*x + b para cada x."""
    return [a * x + b for x in valores_x]


def calcular_mae(reales, estimados):
    """Mean Absolute Error: promedio de |real - estimado|."""
    suma = 0
    for i in range(len(reales)):
        suma += abs(reales[i] - estimados[i])
    return suma / len(reales)


def predecir(anio, a=None, b=None):
    """Estima los matriculados para un año dado."""
    a = A if a is None else a
    b = B if b is None else b
    return a * anio + b
