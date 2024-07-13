import numpy as np
from ..univariable import optimizador_univariable

class by_regions_elimination(optimizador_univariable):
    def __init__(self, x_inicial, xlimite, f, epsilon, iter=100):
        super().__init__(x_inicial, xlimite, f, epsilon, iter)
