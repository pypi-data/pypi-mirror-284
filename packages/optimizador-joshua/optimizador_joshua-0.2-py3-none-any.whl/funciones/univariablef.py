import numpy as np
from numpy.core.multiarray import array as array
from .base import funcion
class univariablefunction(funcion):
    def __init__(self, name):
        super().__init__(name)
    
    def funcion1(self, x):
        self._validate_input(x)
        return (x**2) + (54/x)

    def funcion2(self, x):
        self._validate_input(x)
        return (x**3) + (2*x) - 3

    def funcion3(self, x):
        self._validate_input(x)
        return (x**4) + (x**2) - 33

    def funcion4(self, x):
        self._validate_input(x)
        return (3 * (x**4)) - (8 * (x**3)) - (6 * (x**2)) + 12 * x

    def _validate_input(self, x):
        if isinstance(x, (list, tuple, set, np.ndarray)):
            raise ValueError("x must not be an array, list, or tuple. It must be a scalar number.")
    
    def get_function(self):
        func = getattr(self, self.name.lower(), None)
        if func is None:
            raise ValueError(f"Function '{self.name}' is not defined in the class.")
        return func