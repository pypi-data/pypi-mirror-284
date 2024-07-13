from optimizador.derivate.derivate import derivative_methods
class newton_raphson(derivative_methods):
    def __init__(self, x_inicial, xlimite=1, f=None, epsilon=0.1, iter=100):
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
        k = 1
        x_actual = self.valor_inicial
        #print(f"Iteración {k}: x_actual = {x_actual}")
        
        xderiv = self.primeraderivadanumerica(x_actual)
        xderiv2 = self.segundaderivadanumerica(x_actual)
        xsig = x_actual - (xderiv / xderiv2)
        
        while abs(self.primeraderivadanumerica(xsig)) > self.epsilon:
            x_actual = xsig
            xderiv = self.primeraderivadanumerica(x_actual)
            xderiv2 = self.segundaderivadanumerica(x_actual)
            xsig = x_actual - ((xderiv) /(xderiv2))
        
        return xsig