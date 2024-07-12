class FibonacciOptimization:
    """
    Implementación del método de optimización utilizando la sucesión de Fibonacci para encontrar el mínimo de una función en un intervalo dado.

    Args:
        func (callable): Función objetivo que se desea minimizar.
        a (float): Extremo izquierdo del intervalo inicial.
        b (float): Extremo derecho del intervalo inicial.
        n (int): Número máximo de iteraciones.

    Attributes:
        func (callable): Función objetivo que se desea minimizar.
        a (float): Extremo izquierdo del intervalo actual.
        b (float): Extremo derecho del intervalo actual.
        L (float): Longitud actual del intervalo [a, b].
        n (int): Número máximo de iteraciones.
        k (int): Contador de iteraciones.

    Methods:
        fibonacci(n):
            Calcula el n-ésimo número de la sucesión de Fibonacci.
        optimize():
            Aplica el método de optimización utilizando la sucesión de Fibonacci para encontrar el mínimo de la función en el intervalo [a, b].
    """

    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.L = b - a
        self.n = n
        self.k = 2

    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la sucesión de Fibonacci.

        Args:
            n (int): Índice del número de Fibonacci que se desea calcular.

        Returns:
            int: El valor del n-ésimo número de Fibonacci.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[-1] + fib[-2])
            return fib[n]

    def optimize(self):
        """
        Aplica el método de optimización utilizando la sucesión de Fibonacci para encontrar el mínimo de la función en el intervalo [a, b].

        Returns:
            float: El punto donde se estima que se encuentra el mínimo de la función.
        """
        while self.k <= self.n:
            Lk_star = (self.fibonacci(self.n - self.k + 1) / self.fibonacci(self.n + 1)) * self.L
            x1 = self.a + Lk_star
            x2 = self.b - Lk_star

            f_x1 = self.func(x1)
            f_x2 = self.func(x2)

            if f_x1 < f_x2:
                self.b = x2
            else:
                self.a = x1

            self.L = self.b - self.a

            self.k += 1

        return (self.a + self.b) / 2
