import numpy as np

class BusquedaPorPatrones:
    
    def __init__(self, funcion, x0, deltas, alpha, epsilon):
        self.funcion = funcion
        self.x = np.array(x0)
        self.deltas = np.array(deltas)
        self.alpha = alpha
        self.epsilon = epsilon
        self.N = len(x0)
        self.k = 0

    def movimiento_exploratorio(self):
        x_c = np.copy(self.x)
        for i in range(self.N):
            f = self.funcion(self.x)
            x_p = np.copy(self.x)
            x_n = np.copy(self.x)
            x_p[i] += self.deltas[i]
            x_n[i] -= self.deltas[i]
            f_p = self.funcion(x_p)
            f_n = self.funcion(x_n)
            f_min = min(f, f_p, f_n)
            if f_min == f_p:
                self.x = x_p
            elif f_min == f_n:
                self.x = x_n
        return not np.array_equal(x_c, self.x)

    def movimiento_patron(self, x_prev):
        
        return self.x + (self.x - x_prev)

    def optimizar(self):
  
        x_prev = np.copy(self.x)
        while True:
            if not self.movimiento_exploratorio():
                if np.linalg.norm(self.deltas) < self.epsilon:
                    return self.x
                self.deltas /= self.alpha
                continue
            
            self.k += 1
            x_p = self.movimiento_patron(x_prev)
            x_prev = np.copy(self.x)
            self.x = x_p

            if self.funcion(self.x) < self.funcion(x_prev):
                x_prev = np.copy(self.x)
            else:
                self.x = x_prev
                if np.linalg.norm(self.deltas) < self.epsilon:
                    return self.x
                self.deltas /= self.alpha

