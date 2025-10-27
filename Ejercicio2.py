import numpy as np
import matplotlib.pyplot as plt #zule esta es para la grafica

#ax^3 + bx^2 + cx + d)
print("Ingresa los coeficientes del polinomio ax^3 + bx^2 + cx + d:")
a = float(input("Coeficiente de x^3 (a): "))
b = float(input("Coeficiente de x^2 (b): "))
c = float(input("Coeficiente de x (c): "))
d = float(input("Término independiente (d): "))

# x  calcular la derivada y el paso h es la distancia
x = float(input("Ingresa el valor de x para calcular la derivada: "))
h = float(input("Ingresa el valor del paso h: "))

# polinomio
def polinomio(x):
    return a * x**3 + b * x**2 + c * x + d

# Derivada analítica para calcular el porcentaje
def derivada_teorica(x):
    return 3 * a * x**2 + 2 * b * x + c

# método de cinco puntos
def derivada_numerica(x, h):
    return (-polinomio(x + 2*h) + 8*polinomio(x + h) - 8*polinomio(x - h) + polinomio(x - 2*h)) / (12 * h)


v_teorico = derivada_teorica(x)
v_experimental = derivada_numerica(x, h)

# formula para calcular el error porcentual
error = abs((v_teorico - v_experimental) / v_teorico) * 100


print(f"\nDerivada teórica en x = {x}: {v_teorico}")
print(f"Derivada experimental en x = {x}: {v_experimental}")
print(f"Error porcentual: {error:.4f}%")


x_vals = np.linspace(x - 2*h, x + 2*h, 100)
y_vals = [polinomio(x_val) for x_val in x_vals]
derivada_y_vals = [derivada_teorica(x_val) for x_val in x_vals]

# parte de la grafica
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Polinomio', color='blue')
plt.plot(x_vals, derivada_y_vals, label='Derivada teórica', color='red', linestyle='--')
plt.axvline(x, color='green', linestyle=':', label=f'Punto x = {x}')
plt.title('Polinomio y su derivada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()