class Optimization:
    """
    Implementación del método de optimización utilizando la técnica de interpolación cuadrática para encontrar el mínimo de una función en un intervalo dado.

    Args:
        func (callable): Función objetivo que se desea minimizar.
        a (float): Extremo izquierdo del intervalo inicial.
        b (float): Extremo derecho del intervalo inicial.
        epsilon (float): Tolerancia para la longitud del intervalo donde se considera que se ha encontrado el mínimo.

    Attributes:
        func (callable): Función objetivo que se desea minimizar.
        a (float): Extremo izquierdo del intervalo actual.
        b (float): Extremo derecho del intervalo actual.
        epsilon (float): Tolerancia para la longitud del intervalo donde se considera que se ha encontrado el mínimo.
        xm (float): Punto medio del intervalo [a, b].
        L0 (float): Longitud inicial del intervalo [a, b].
        L (float): Longitud actual del intervalo [a, b].

    Methods:
        optimize():
            Aplica el método de optimización utilizando la técnica de interpolación cuadrática para encontrar el mínimo de la función en el intervalo [a, b].
    """

    def __init__(self, func, a, b, epsilon):
        self.func = func
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.xm = (a + b) / 2
        self.L0 = b - a
        self.L = self.L0

    def optimize(self):
        """
        Aplica el método de optimización utilizando la técnica de interpolación cuadrática para encontrar el mínimo de la función en el intervalo [a, b].

        Returns:
            float: El punto donde se estima que se encuentra el mínimo de la función.
        """
        while abs(self.L) >= self.epsilon:
            xm = (self.a + self.b) / 2
            x1 = self.a + self.L / 4
            x2 = self.b - self.L / 4
            
            f_xm = self.func(xm)
            f_x1 = self.func(x1)
            f_x2 = self.func(x2)
            
            if f_x1 < f_xm:
                self.b = xm
                self.xm = x1
            elif f_x2 < f_xm:
                self.a = xm
                self.xm = x2
            else:
                self.a = x1
                self.b = x2
                
            self.L = self.b - self.a
        
        return self.xm
