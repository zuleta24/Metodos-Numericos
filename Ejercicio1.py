import numpy as np

def lagrange_3puntos(x0, y0, x1, y1, x2, y2):
    """
    Calcula el polinomio de Lagrange para 3 puntos.
    Retorna coeficientes [a0, a1, a2] de P(x) = a0 + a1*x + a2*x²
    """
    # Matriz de Vandermonde
    A = np.array([
        [1, x0, x0**2],
        [1, x1, x1**2],
        [1, x2, x2**2]
    ])
    
    b = np.array([y0, y1, y2])
    
    # Resolver el sistema A*coef = b
    coef = np.linalg.solve(A, b)
    
    return coef

def mostrar_polinomio(coef):
    """Imprime el polinomio de forma legible"""
    a0, a1, a2 = coef
    print(f"\nP(x) = {a0:.4f} + ({a1:.4f})x + ({a2:.4f})x²")

# Ejemplo de uso
print("Polinomio de Lagrange para 3 puntos")
print("="*40)

# Puntos de ejemplo
x0, y0 = 1, 2
x1, y1 = 3, 4
x2, y2 = 5, 10

print(f"Puntos: ({x0}, {y0}), ({x1}, {y1}), ({x2}, {y2})")

# Calcular polinomio
coef = lagrange_3puntos(x0, y0, x1, y1, x2, y2)
mostrar_polinomio(coef)

# Verificar
print("\nVerificación:")
for x, y in [(x0, y0), (x1, y1), (x2, y2)]:
    p_x = coef[0] + coef[1]*x + coef[2]*x**2
    print(f"P({x}) = {p_x:.4f} ≈ {y}")

print("\n" + "="*40)
print("Ingresa tus propios puntos:")
x0 = float(input("x0: "))
y0 = float(input("y0: "))
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

coef = lagrange_3puntos(x0, y0, x1, y1, x2, y2)
mostrar_polinomio(coef)