from ..derivate.derivate import derivative_methods
import numpy as np
class secante(derivative_methods):
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
    def calculozensecante(self,x2,x1):
        numerador=self.primeraderivadanumerica(x2)
        denominador=((self.primeraderivadanumerica(x2) - self.primeraderivadanumerica (x1)))/(x2-x1)
        op=numerador/denominador
        return x2 - op

    def optimize(self):
        a = np.random.uniform(self.valor_inicial, self.limite)
        b = np.random.uniform(self.valor_inicial, self.limite)
        while(self.primeraderivadanumerica(a) > 0):
            a = np.random.uniform(self.valor_inicial, self.limite)
        
        while (self.primeraderivadanumerica(b) < 0): 
            b = np.random.uniform(self.valor_inicial, self.valor_inicial)
        x1=a
        x2=b
        z = self.calculozensecante(x2,x1)
        while(self.primeraderivadanumerica(z) > self.epsilon): 
            if self.primeraderivadanumerica(z) < 0: 
                x1=z
                z=0
                z = self.calculozensecante(x2,x1)
            if self.primeraderivadanumerica(z) > 0: 
                x2=z
                z=0
                z = self.calculozensecante(x2,x1)
        return (x1 + x2)/2