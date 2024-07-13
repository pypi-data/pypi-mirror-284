import numpy as np
from numpy.core.multiarray import array as array
from .base import funcion
class objetive_function(funcion):
    def __init__(self, name, espaciobussqueda: np.array):
        super().__init__(name, espaciobussqueda)
    def himmelblau(self, p):
        return (p[0]**2 + p[1] - 11)**2 + (p[0] + p[1]**2 - 7)**2
    
    def sphere(self, x):
        return np.sum(np.square(x))

    def rastrigin(self, x, A=10):
        self.limite=float(5.12)
        n = len(x)
        return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

    def rosenbrock(self, x):
        return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

    def beale(self, x):
        self.limite=4.5
        return ((1.5 - x[0] + x[0] * x[1])**2 +
                (2.25 - x[0] + x[0] * x[1]**2)**2 +
                (2.625 - x[0] + x[0] * x[1]**3)**2)
    
    def goldstein(self, x):
        self.limite=2
        part1 = (1 + (x[0] + x[1] + 1)**2 * 
                 (19 - 14 * x[0] + 3 * x[0]**2 - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1]**2))
        part2 = (30 + (2 * x[0] - 3 * x[1])**2 * 
                 (18 - 32 * x[0] + 12 * x[0]**2 + 48 * x[1] - 36 * x[0] * x[1] + 27 * x[1]**2))
        return part1 * part2

    def boothfunction(self, x):
        self.limite=10
        return (x[0] + 2 * x[1] - 7)**2 + (2 * x[0] + x[1] - 5)**2

    def bunkinn6(self, x):
        return 100 * np.sqrt(np.abs(x[1] - 0.001 * x[0]**2)) + 0.01 * np.abs(x[0] + 10)

    def matyas(self, x):
        return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]

    def levi(self, x):
        part1 = np.sin(3 * np.pi * x[0])**2
        part2 = (x[0] - 1)**2 * (1 + np.sin(3 * np.pi * x[1])**2)
        part3 = (x[1] - 1)**2 * (1 + np.sin(2 * np.pi * x[1])**2)
        return part1 + part2 + part3
    
    def threehumpcamel(self, x):
        return 2 * x[0]**2 - 1.05 * x[0]**4 + (x[0]**6) / 6 + x[0] * x[1] + x[1]**2

    def easom(self, x):
        return -np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - np.pi)**2 - (x[1] - np.pi)**2)

    def crossintray(self, x):
        op = np.abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2) / np.pi)))
        return -0.0001 * (op + 1)**0.1

    def eggholder(self, x):
        op1 = -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[0] / 2 + (x[1] + 47))))
        op2 = -x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))
        return op1 + op2

    def holdertable(self, x):
        op = np.abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2) / np.pi)))
        return -op

    def mccormick(self, x):
        return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5 * x[0] + 2.5 * x[1] + 1

    def schaffern2(self, x):
        self.limite=100
        numerator = np.sin(x[0]**2 - x[1]**2)**2 - 0.5
        denominator = (1 + 0.001 * (x[0]**2 + x[1]**2))**2
        return 0.5 + numerator / denominator

    def schaffern4(self, x):
        self.limite=100
        num = np.cos(np.sin(np.abs(x[0]**2 - x[1]**2))) - 0.5
        den = (1 + 0.001 * (x[0]**2 + x[1]**2))**2
        return 0.5 + num / den

    def styblinskitang(self, x):
        self.limite=5
        return np.sum(x**4 - 16 * x**2 + 5 * x) / 2
    
    def shekel(self, x, a=None, c=None):
        if a is None:# Esto lo hice para que el usuario pueda meter los pesos que guste, si no se ponen estos
            a = np.array([
                [4.0, 4.0, 4.0, 4.0],
                [1.0, 1.0, 1.0, 1.0],
                [8.0, 8.0, 8.0, 8.0],
                [6.0, 6.0, 6.0, 6.0],
                [3.0, 7.0, 3.0, 7.0],
                [2.0, 9.0, 2.0, 9.0],
                [5.0, 5.0, 3.0, 3.0],
                [8.0, 1.0, 8.0, 1.0],
                [6.0, 2.0, 6.0, 2.0],
                [7.0, 3.6, 7.0, 3.6]
            ])
        if c is None:
            c = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])#Lo mismo que con a
        
        m = len(c)
        s = 0
        for i in range(m):
            s -= 1 / (np.dot(x - a[i, :2], x - a[i, :2]) + c[i])#Esta es la sumatoria dado m, que seria el numero de terminos en la suma
        return s
    def get_function(self):
        func = getattr(self, self.name.lower(), None)
        if func is None:
            raise ValueError(f"Function '{self.name}' is not defined in the class.")
        return func
    
    def get_limitesup(self):
        return self.limiteinf[0]
    
    def get_limiteinf(self):
        return self.limitesup[1]