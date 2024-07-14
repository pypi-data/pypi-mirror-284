from ..baseopt import by_regions_elimination
import numpy as np
class goldensearch(by_regions_elimination):
    def __init__(self, x_inicial, x_limite, f, epsilon):
        super().__init__(x_inicial, x_limite, f, epsilon)
    
    def findregions(self,x1, x2, fx1, fx2, a, b):
        if fx1 > fx2:
            return x1, b
        if fx1 < fx2:
            return a, x2
        return x1, x2 
    def w_to_x(self,w, a, b):
        return w * (b - a) + a 

    def optimize(self):
        a,b=self.valor_inicial,self.limite
        phi = (1 + np.sqrt(5)) / 2 - 1
        aw, bw = 0, 1
        Lw = 1
        k = 1
        while Lw > self.epsilon:
            w2 = aw + phi * Lw
            w1 = bw - phi * Lw
            aw, bw = self.findregions(w1, w2, self.funcion(self.w_to_x(w1, a, b)), self.funcion(self.w_to_x(w2, a, b)), aw, bw)
            k += 1
            Lw = bw - aw
        return (self.w_to_x(aw, a, b) + self.w_to_x(bw, a, b)) / 2
