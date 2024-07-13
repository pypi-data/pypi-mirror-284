import numpy as np
from ..multivariable import optimizador_multivariable
class direct_methods(optimizador_multivariable):
    def __init__(self, variables, f, epsilon, iter=100):
        super().__init__(variables, f, epsilon, iter)