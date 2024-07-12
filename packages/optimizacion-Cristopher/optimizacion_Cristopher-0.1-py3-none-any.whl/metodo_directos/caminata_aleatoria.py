import numpy as np

class OptimizadorRandomWalk:
  
    pass
    def __init__(self, funcion, x0, epsilon, max_iter):
        self.funcion = funcion
        self.x0 = np.array(x0)
        self.epsilon = epsilon
        self.max_iter = max_iter

    def generacion_aleatoria(self, xk):
        return xk + np.random.uniform(-self.epsilon, self.epsilon, size=xk.shape)

    def optimizar1(self):
        """
        Realiza el proceso de optimización utilizando el método de Random Walk.

        Returns:
            numpy.ndarray: El mejor punto encontrado durante la optimización.
        """
        x_mejor = self.x0
        xk = self.x0
        contador_iteraciones = 0

        while contador_iteraciones < self.max_iter:
            xk1 = self.generacion_aleatoria(xk)
            if self.funcion(xk1) < self.funcion(x_mejor):
                x_mejor = xk1
            xk = xk1
            contador_iteraciones += 1

        return x_mejor
