import numpy as np
from scipy.optimize import minimize_scalar

class Cauchy:
    def __init__(self, funcion, x0, epsilon1, epsilon2, max_iter):
        self.funcion = funcion
        self.x0 = np.array(x0)
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.max_iter = max_iter

    def aproximar_gradiente(self, xk):
        """Aproxima el gradiente numéricamente."""
        gradiente_aprox = np.zeros_like(xk)
        h = 1e-6
        for i in range(len(xk)):
            xk1 = xk.copy()
            xk1[i] += h
            gradiente_aprox[i] = (self.funcion(xk1) - self.funcion(xk)) / h
        return gradiente_aprox

    def buscar_alpha(self, xk, gradiente_xk):
        """Busca el tamaño de paso óptimo usando la búsqueda de línea."""
        def f(alpha):
            return self.funcion(xk - alpha * gradiente_xk)

        res = minimize_scalar(f)
        return res.x

    def optimizar(self):
        xk = self.x0
        k = 0

        while k < self.max_iter:
            gradiente_xk = self.aproximar_gradiente(xk)
            if np.linalg.norm(gradiente_xk) <= self.epsilon1:
                break

            alpha_k = self.buscar_alpha(xk, gradiente_xk)
            xk1 = xk - alpha_k * gradiente_xk

            if np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) <= self.epsilon2:
                break

            xk = xk1
            k += 1

        return xk


