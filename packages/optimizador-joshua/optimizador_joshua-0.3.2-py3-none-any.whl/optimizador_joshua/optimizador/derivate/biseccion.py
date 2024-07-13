import numpy as np
from ..derivate.derivate import derivative_methods
class biseccion(derivative_methods):
    def __init__(self, x_inicial, xlimite, f, epsilon, iter=100):
        super().__init__(x_inicial, xlimite, f, epsilon, iter)
    def primeraderivadanumerica(self, x_actual):
        delta = 0.0001
        numerador = self.funcion(x_actual + delta) - self.funcion(x_actual - delta) 
        return numerador / (2 * delta)

    def segundaderivadanumerica(self, x_actual):
        delta = 0.0001
        numerado = self.funcion(x_actual + delta) - (2 * self.funcion(x_actual)) + self.funcion(x_actual - delta)
        return numerado / (delta**2)
    
    def optimize(self):
        a = np.random.uniform(self.valor_inicial, self.limite)
        b = np.random.uniform(self.valor_inicial, self.limite)
        while(self.primeraderivadanumerica(a) > 0):
            a = np.random.uniform(self.valor_inicial, self.limite)
        
        while (self.primeraderivadanumerica(b) < 0): 
            b = np.random.uniform(self.valor_inicial, self.valor_inicial)
        x1=a
        x2=b
        z = ((x2+x1)/2)
        #print(primeraderivadanumerica(x1,f))
        while(self.primeraderivadanumerica(z) > self.epsilon):
            #print(z)
            if self.primeraderivadanumerica(z) < 0: 
                x1=z
                z=0
                z = int((x2+x1)/2)
            elif self.primeraderivadanumerica(z) > 0: 
                x2=z
                z=0
                z = ((x2+x1)/2)
        return (x1 + x2)/2