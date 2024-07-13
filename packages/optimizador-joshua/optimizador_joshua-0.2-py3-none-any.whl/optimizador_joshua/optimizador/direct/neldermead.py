from optimizador.direct.directmethods import direct_methods
import numpy as np
class neldermead(direct_methods):
    def __init__(self, variables,gamma,beta, f, epsilon, iter=100):
        super().__init__(variables, f, epsilon, iter)
        self.variables= np.array(variables)
        self.gamma=gamma
        self.beta=beta
    
    def delta1(self,N, scale):
        num = np.sqrt(N + 1) + N - 1
        den = N * np.sqrt(2)
        op = num / den
        return op * scale

    def delta2(self,N, scale):
        num = np.sqrt(N + 1) - 1
        den = N * np.sqrt(2)
        op = num / den
        return op * scale

    def create_simplex(self,initial_point, scale=1.0):
        n = len(initial_point)
        simplex = [np.array(initial_point, dtype=float)] 
        d1 = self.delta1(n, scale)
        d2 = self.delta2(n, scale)
        for i in range(n):
            point = np.array(simplex[0], copy=True)  
            for j in range(n):
                if j == i: 
                    point[j] += d1
                else:
                    point[j] += d2
            simplex.append(point)
        
        simplex_final = np.array(simplex)

        return np.round(simplex_final, 4)
    def findpoints(self,points):
        evaluaciones = [self.funcion(p) for p in points]
        worst = np.argmax(evaluaciones)
        best = np.argmin(evaluaciones)
        indices = list(range(len(evaluaciones)))
        indices.remove(worst)
        second_worst = indices[np.argmax([evaluaciones[i] for i in indices])]
        if second_worst == best:
            indices.remove(best)
            second_worst = indices[np.argmax([evaluaciones[i] for i in indices])]
        return best, second_worst, worst
    def xc_calculation(self,x, indexs):
        m = x[indexs]
        centro = []
        for i in range(len(m[0])):
            suma = sum(p[i] for p in m)
            v = suma / len(m)
            centro.append(v)
        return np.array(centro)
    def stopcondition(self,simplex, xc):
        value = 0
        n = len(simplex)
        for i in range(n):
            value += (((self.funcion(simplex[i]) - self.funcion(xc))**2) / (n + 1))
        return np.sqrt(value)
    def optimize(self):
        cont = 1
        mov = []
        simplex = self.create_simplex(self.variables)
        mov.append(simplex)
        best, secondworst, worst = self.findpoints(simplex)
        indices = [best, secondworst, worst]
        indices.remove(worst)
        centro = self.xc_calculation(simplex, indices)
        x_r = (2 * centro) - simplex[worst]
        x_new = x_r
        if self.funcion(x_r) < self.funcion(simplex[best]): 
            x_new = ((1 + self.gamma) * centro) - (self.gamma * simplex[worst])
        elif self.funcion(x_r) >= self.funcion(simplex[worst]):
            x_new = ((1 - self.beta) * centro) + (self.beta * simplex[worst])
        elif self.funcion(simplex[secondworst]) < self.funcion(x_r) and self.funcion(x_r) < self.funcion(simplex[worst]):
            x_new = ((1 - self.beta) * centro) - (self.beta * simplex[worst])
        simplex[worst] = x_new
        mov.append(np.copy(simplex))
        stop = self.stopcondition(simplex, centro)
        while stop >= self.epsilon:
            stop = 0
            best, secondworst, worst = self.findpoints(simplex)
            indices = [best, secondworst, worst]
            indices.remove(worst)
            centro = self.xc_calculation(simplex, indices)
            x_r = (2 * centro) - simplex[worst]
            x_new = x_r
            if self.funcion(x_r) < self.funcion(simplex[best]):
                x_new = ((1 + self.gamma) * centro) - (self.gamma * simplex[worst])
            elif self.funcion(x_r) >= self.funcion(simplex[worst]):
                x_new = ((1 - self.beta) * centro) + (self.beta * simplex[worst])
            elif self.funcion(simplex[secondworst]) < self.funcion(x_r) and self.funcion(x_r) < self.funcion(simplex[worst]):
                x_new = ((1 + self.beta) * centro) - (self.beta * simplex[worst])
            simplex[worst] = x_new
            stop = self.stopcondition(simplex, centro)
            #print(stop)
            #mov.append(np.copy(simplex))
            cont+=1
        return simplex[best]
    