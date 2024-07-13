from .base import optimizador
class optimizador_multivariable(optimizador):
    def __init__(self,variables ,f, epsilon, iter=100):
        super().__init__(f, epsilon, iter)
        self.variables=variables