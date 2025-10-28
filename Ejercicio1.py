import numpy as np
import matplotlib.pyplot as plt

def lagrange_3puntos(x0, y0, x1, y1, x2, y2):
    """Calcula el polinomio de Lagrange para 3 puntos."""
    A = np.array([[1, x0, x0**2], [1, x1, x1**2], [1, x2, x2**2]])
    b = np.array([y0, y1, y2])
    return np.linalg.solve(A, b)

def graficar(coef, puntos):
    """Grafica el polinomio y los puntos."""
    x_plot = np.linspace(min(puntos[:, 0]) - 1, max(puntos[:, 0]) + 1, 200)
    y_plot = coef[0] + coef[1]*x_plot + coef[2]*x_plot**2
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, 'b-', label=f'P(x) = {coef[0]:.2f} + {coef[1]:.2f}x + {coef[2]:.2f}x²')
    plt.plot(puntos[:, 0], puntos[:, 1], 'ro', markersize=10, label='Puntos dados')
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Polinomio de Lagrange - 3 puntos')
    plt.show()

# Ejemplo de uso
print("Polinomio de Lagrange para 3 puntos\n" + "="*40)
x0, y0 = 1, 2
x1, y1 = 3, 4
x2, y2 = 5, 10

puntos = np.array([[x0, y0], [x1, y1], [x2, y2]])
print(f"Puntos: ({x0}, {y0}), ({x1}, {y1}), ({x2}, {y2})")

coef = lagrange_3puntos(x0, y0, x1, y1, x2, y2)
print(f"\nP(x) = {coef[0]:.4f} + ({coef[1]:.4f})x + ({coef[2]:.4f})x²")

graficar(coef, puntos)

# Tus propios puntos
print("\n" + "="*40 + "\nIngresa tus propios puntos:")
x0, y0 = float(input("x0: ")), float(input("y0: "))
x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))

puntos = np.array([[x0, y0], [x1, y1], [x2, y2]])
coef = lagrange_3puntos(x0, y0, x1, y1, x2, y2)
print(f"\nP(x) = {coef[0]:.4f} + ({coef[1]:.4f})x + ({coef[2]:.4f})x²")

graficar(coef, puntos)