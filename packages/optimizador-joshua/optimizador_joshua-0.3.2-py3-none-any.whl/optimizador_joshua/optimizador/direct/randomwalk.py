from ..direct.directmethods import direct_methods
import numpy as np
class random_walk(direct_methods):
    def __init__(self, variables, f, epsilon, iter=100):
        super().__init__(variables, f, epsilon, iter)
    
    def step_calculation(self,x):
        x_n=np.array(x)
        mu=0
        stddev=1
        random_value = np.random.normal(mu, stddev)
        return x_n + random_value

    def optimize(self):
        x=np.array(self.variables)
        xmejor=x
        cont=0
        while(self.iteraciones > cont):
            x_nuevo=self.step_calculation(x)
            if self.funcion(x_nuevo)< self.funcion(xmejor):
                xmejor=x_nuevo
            cont+=1
        return xmejor