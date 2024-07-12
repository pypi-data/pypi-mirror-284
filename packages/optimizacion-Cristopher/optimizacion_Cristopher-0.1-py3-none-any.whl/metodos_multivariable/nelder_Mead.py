import numpy as np

class OptimizacionNelder:
    
    def __init__(self, funcion, x0, alpha, gamma, beta, epsilon):
        self.funcion = funcion
        self.x0 = np.array(x0)
        self.alpha = alpha
        self.gamma = gamma
        self.beta = beta
        self.epsilon = epsilon
        self.N = len(x0)
        self.simplex = self.crear_simplex_inicial()

    def crear_simplex_inicial(self):

        N = self.N
        x0 = self.x0
        alpha = self.alpha
        
        delta1 = (np.sqrt(N + 1) + N - 1) / (N * np.sqrt(2)) * alpha
        delta2 = (np.sqrt(N + 1) - 1) / (N * np.sqrt(2)) * alpha
        
        simplex = np.zeros((N + 1, N))
        simplex[0] = x0
        for i in range(1, N + 1):
            simplex[i] = x0 + delta2
            simplex[i][i - 1] = x0[i - 1] + delta1
        
        return simplex

    def optimizar(self):
  
        while True:
            valores = np.apply_along_axis(self.funcion, 1, self.simplex)
            indices_ordenados = np.argsort(valores)
            self.simplex = self.simplex[indices_ordenados]
            
            x_c = np.mean(self.simplex[:-1], axis=0)
            
            x_r = (1 + self.alpha) * x_c - self.alpha * self.simplex[-1]
            f_r = self.funcion(x_r)
            
            if f_r < valores[0]:
                x_e = (1 + self.gamma) * x_c - self.gamma * self.simplex[-1]
                f_e = self.funcion(x_e)
                if f_e < f_r:
                    self.simplex[-1] = x_e
                else:
                    self.simplex[-1] = x_r
            elif f_r < valores[-2]:
                self.simplex[-1] = x_r
            else:
                if f_r < valores[-1]:
                    x_c = (1 + self.beta) * x_c - self.beta * self.simplex[-1]
                else:
                    x_c = (1 - self.beta) * x_c + self.beta * self.simplex[-1]
                
                f_c = self.funcion(x_c)
                if f_c < valores[-1]:
                    self.simplex[-1] = x_c
                else:
                    for i in range(1, len(self.simplex)):
                        self.simplex[i] = self.simplex[0] + 0.5 * (self.simplex[i] - self.simplex[0])
            
            if np.sqrt(np.sum((valores - np.mean(valores)) ** 2) / (self.N + 1)) <= self.epsilon:
                return self.simplex[0]
