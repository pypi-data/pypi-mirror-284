from ..direct.directmethods import direct_methods
import numpy as np
class hooke_jeeves(direct_methods):
    def __init__(self, variables,delta ,f, epsilon, alpha=2):
        super().__init__(variables, f, epsilon)
        self.alpha=alpha
        self.delta=delta
    
    def movexploratory(self,basepoint, delta):
        nextpoint = []
        coordanatess = [basepoint]
        newvalue = True
        #Creacion de las coordenadas 
        for i in range(len(basepoint)):
            point = basepoint.copy()
            point2 = basepoint.copy()
            point[i] += delta[i]
            point2[i] -= delta[i]
            coordanatess.append(point)
            coordanatess.append(point2)
        
        #evaluacion de las coordenadas
        for coordenate in coordanatess:
            nextpoint.append(self.funcion(coordenate))
        
        #Busqueda del min 
        minum = np.argmin(nextpoint)
        if (coordanatess[minum] == basepoint).all():
            newvalue = False
        
        return coordanatess[minum], newvalue

    def patternmove(self,currentbestpoint, lastbestpoint):
        basepoint = currentbestpoint + (currentbestpoint - lastbestpoint)
        return basepoint

    def updatedelta(self,delta):
        new_delta = delta / self.alpha
        return new_delta
    def optimize(self):
        cont = 0
        x_inicial = np.array(self.variables)
        delta = np.array(self.delta)
        x_anterior = x_inicial
        x_mejor, flag = self.movexploratory(x_inicial, delta)
        while np.linalg.norm(delta) > self.epsilon:
            if flag:
                x_point = self.patternmove(x_mejor, x_anterior)
                x_mejor_nuevo, flag = self.movexploratory(x_point, delta)
            else:
                delta = self.updatedelta(delta)
                x_mejor, flag = self.movexploratory(x_mejor, delta)
                x_point = self.patternmove(x_mejor, x_anterior)
                x_mejor_nuevo, flag = self.movexploratory(x_point, delta)
            #Son dos subprocersos
            if self.funcion(x_mejor_nuevo) < self.funcion(x_mejor):
                flag = True
                x_anterior = x_mejor
                x_mejor = x_mejor_nuevo
            else:
                flag = False

            cont += 1
        print("Num de iteraciones {}".format(cont))
        return x_mejor_nuevo