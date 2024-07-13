from ..byregions.byregions import by_regions_elimination
class fibonacci(by_regions_elimination):
    def __init__(self, x_inicial, x_limite, f, iter=100):
        super().__init__(x_inicial, x_limite, f, iter)
    def findregions(self,rangomin,rangomax,x1,x2):
        if self.funcion(x1)> self.funcion(x2):
            rangomin=rangomin
            rangomax=x2
        elif self.funcion(x1)< self.funcion(x2):
            rangomin=x1
            rangomax=rangomax
        elif self.funcion(x1)== self.funcion(x2):
            rangomin=x1
            rangomax=x2
        return rangomin,rangomax

    def fibonacci_iterativo(self,n):
        fibonaccie = [0, 1]
        for i in range(2, n):
            fibonaccie.append(fibonaccie[i-1] + fibonaccie[i-2])
        return fibonaccie

    def calculo_lk(self,fibonacci,n,k):
        indice1=n - (k + 1)
        indice2= n + 1
        return fibonacci[indice1]/ fibonacci[indice2]

    def optimize(self):
        a,b=self.valor_inicial,self.limite
        n=self.iteraciones
        l=b-a
        seriefibonacci=self.fibonacci_iterativo(n*10)
        #calculo de lk
        k=2
        lk=self.calculo_lk(seriefibonacci,n,k)
        x1=a+lk
        x2=b-lk
        while k != n:
            if k % 2 == 0:
                evalx1=self.funcion(x1)
                a,b=self.findregions(a,b,evalx1,x2)
                #print(" Valor actual de a y b = {} , {}".format(a,b))
            else:
                evalx2=self.funcion(x2)
                a,b=self.findregions(a,b,x1,evalx2)
                #print(" Valor actual de a y b = {} , {}".format(a,b))
            k+=1
        
        return (a+b)/2