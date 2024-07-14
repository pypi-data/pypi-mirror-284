from .funciones.base import funcion
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
class optimizador_univariable(optimizador):
    def __init__(self,x_inicial,xlimite ,f, epsilon, iter=100):
        super().__init__(f, epsilon, iter)
        self.valor_inicial=x_inicial
        self.limite=xlimite
    
    def optimize(self):
        raise NotImplementedError("Subclasses should implement this method.")

class optimizador_multivariable(optimizador):
    def __init__(self,variables ,f, epsilon, iter=100):
        super().__init__(f, epsilon, iter)
        self.variables=variables

class by_regions_elimination(optimizador_univariable):
    def __init__(self, x_inicial, xlimite, f, epsilon, iter=100):
        super().__init__(x_inicial, xlimite, f, epsilon, iter)
class derivative_methods(optimizador_univariable):
    def __init__(self, x_inicial, xlimite, f, epsilon, iter=100):
        super().__init__(x_inicial, xlimite, f, epsilon, iter)

class direct_methods(optimizador_multivariable):
    def __init__(self, variables, f, epsilon, iter=100):
        super().__init__(variables, f, epsilon, iter)

class gradient_methods(optimizador_multivariable):
    def __init__(self, variables, f, epsilon, iter=100):
        super().__init__(variables, f, epsilon, iter)