import numpy as np
from funciones.base import funcion
class optimizador:
    def __init__(self,f,epsilon,iter=100):
        self.funcion=self.validate_function(f)
        self.epsilon=epsilon
        self.iteraciones=iter
    def validate_function(self, f):
        if isinstance(f, funcion):
            return f.get_function()
        else:
            return f