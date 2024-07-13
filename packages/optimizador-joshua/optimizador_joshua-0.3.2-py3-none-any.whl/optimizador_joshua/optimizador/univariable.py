from .base import optimizador
class optimizador_univariable(optimizador):
    def __init__(self,x_inicial,xlimite ,f, epsilon, iter=100):
        super().__init__(f, epsilon, iter)
        self.valor_inicial=x_inicial
        self.limite=xlimite
    
    def optimize(self):
        raise NotImplementedError("Subclasses should implement this method.")
