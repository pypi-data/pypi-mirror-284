import sympy as sp

class OptimizacionSecante:
    def __init__(self, funcion, a, b, epsilon):
        self.funcion = funcion
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.derivada = self._calcular_derivada()

    def _calcular_derivada(self):
        x = sp.Symbol('x')
        f = self.funcion(x)
        f_prime = sp.diff(f, x)
        f_prime_func = sp.lambdify(x, f_prime)
        return f_prime_func

    def optimizar(self):

        x1 = self.a
        x2 = self.b

        while True:
            f_prime_x1 = self.derivada(x1)
            f_prime_x2 = self.derivada(x2)

            z = x2 - f_prime_x2 / ((f_prime_x2 - f_prime_x1) / (x2 - x1))
            f_prime_z = self.derivada(z)

            if abs(f_prime_z) <= self.epsilon:
                return z
            elif f_prime_z < 0:
                x1 = z
            else:
                x2 = z





