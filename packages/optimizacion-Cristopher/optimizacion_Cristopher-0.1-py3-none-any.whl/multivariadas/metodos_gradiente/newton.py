import numpy as np

class Newton:

    def __init__(self, funcion, gradiente, hessiana, x0, epsilon1, epsilon2, max_iter):
        self.funcion = funcion
        self.gradiente = gradiente
        self.hessiana = hessiana
        self.x = np.array(x0)
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.max_iter = max_iter

    def optimizar(self):

        for k in range(self.max_iter):
            grad = self.gradiente(self.x)
            hess = self.hessiana(self.x)
            
            def f_alpha(alpha):
                return self.funcion(self.x - alpha * np.linalg.inv(hess).dot(grad))
            
            alpha = self.busqueda_unidireccional(f_alpha, self.epsilon2)
            
            self.x = self.x - alpha * np.linalg.inv(hess).dot(grad)
            
            if np.linalg.norm(grad) < self.epsilon1:
                break
        
        return self.x

    def busqueda_unidireccional(self, f_alpha, epsilon2):

        alpha = 0
        step_size = 1.0
        while True:
            if f_alpha(alpha + step_size) < f_alpha(alpha):
                alpha += step_size
            elif f_alpha(alpha - step_size) < f_alpha(alpha):
                alpha -= step_size
            else:
                step_size *= epsilon2
            if step_size < epsilon2:
                break
        return alpha
