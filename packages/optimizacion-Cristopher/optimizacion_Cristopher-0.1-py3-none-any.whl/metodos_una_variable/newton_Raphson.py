class OptimizacionNewton:


    def __init__(self, func, x0, epsilon):
        self.func = func
        self.x = x0
        self.epsilon = epsilon
        self.h = 1e-5  # Pequeño incremento para calcular las derivadas usando diferencias finitas

    def dfunc(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)

    def ddfunc(self, x):
        return (self.func(x + self.h) - 2 * self.func(x) + self.func(x - self.h)) / (self.h ** 2)

    def optimizar(self):
        k = 1
        while True:
            f_prima = self.dfunc(self.x)
            f_doble_prima = self.ddfunc(self.x)
            x_nuevo = self.x - f_prima / f_doble_prima
            f_prima_nuevo = self.dfunc(x_nuevo)
            
            if abs(f_prima_nuevo) < self.epsilon:
                break
            
            self.x = x_nuevo
            k += 1
        
        return self.x
