import numpy as np
from scipy.optimize import minimize_scalar

class OptimizadorGradienteConjugado:
    def __init__(self, funcion, x0, epsilon1, epsilon2, epsilon3, max_iter):

        self.funcion = funcion
        self.x0 = np.array(x0)
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.epsilon3 = epsilon3
        self.max_iter = max_iter

    def aproximar_gradiente(self, xk):

        gradiente_aprox = np.zeros_like(xk)
        h = 1e-6
        for i in range(len(xk)):
            xk1 = xk.copy()
            xk1[i] += h
            gradiente_aprox[i] = (self.funcion(xk1) - self.funcion(xk)) / h
        return gradiente_aprox

    def buscar_lambda(self, xk, sk):

        lambda_ = 1.0
        while True:
            xk1 = xk + lambda_ * sk
            if self.funcion(xk1) < self.funcion(xk) - self.epsilon1 * lambda_ * np.dot(self.aproximar_gradiente(xk), sk):
                break
            lambda_ *= 0.5  # Reducir el tamaño del paso
        return lambda_

    def optimizar(self):
  
        xk = self.x0
        k = 0

        gradiente_xk = self.aproximar_gradiente(xk)
        sk = -gradiente_xk

        while k < self.max_iter:
            lambda_k = self.buscar_lambda(xk, sk)
            xk1 = xk + lambda_k * sk

            if np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) <= self.epsilon2 or np.linalg.norm(self.aproximar_gradiente(xk1)) <= self.epsilon3:
                break

            gradiente_xk1 = self.aproximar_gradiente(xk1)
            beta_k = np.dot(gradiente_xk1, gradiente_xk1) / np.dot(gradiente_xk, gradiente_xk)
            sk = -gradiente_xk1 + beta_k * sk

            xk = xk1
            gradiente_xk = gradiente_xk1
            k += 1

        return xk

# Ejemplo de uso:
def funcion_ejemplo(x):
    return x[0]**2 + x[1]**2  # Ejemplo de función

x0 = [1, 1]  # Punto inicial
epsilon1 = 1e-6  # Primera condición de terminación
epsilon2 = 1e-6  # Segunda condición de terminación
epsilon3 = 1e-6  # Tercera condición de terminación
max_iter = 1000  # Número máximo de iteraciones

optimizador = OptimizadorGradienteConjugado(funcion_ejemplo, x0, epsilon1, epsilon2, epsilon3, max_iter)
resultado = optimizador.optimizar()
print(f"El valor óptimo es: {resultado}")
