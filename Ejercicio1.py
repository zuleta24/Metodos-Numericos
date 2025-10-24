import sympy as sp

# Definir la variable simbólica x
x = sp.symbols('x')

# Solicitar los puntos al usuario (asumiendo valores numéricos)
x0 = float(input("Ingrese x0: "))
y0 = float(input("Ingrese y0: "))
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

# Calcular las bases de Lagrange (l0, l1, l2)
l0 = ((x - x1) / (x0 - x1)) * ((x - x2) / (x0 - x2))
l1 = ((x - x0) / (x1 - x0)) * ((x - x2) / (x1 - x2))
l2 = ((x - x0) / (x2 - x0)) * ((x - x1) / (x2 - x1))

# Construir el polinomio de Lagrange
P = y0 * l0 + y1 * l1 + y2 * l2

# Expandir el polinomio
P_expanded = sp.expand(P)

# Imprimir el polinomio expandido
print("El polinomio de Lagrange expandido es:")
print(P_expanded)