import numpy as np
from .base import funcion
class restriction_functions(funcion):
    def __init__(self, name, espaciobusqueda: np.array):
        super().__init__(name, espaciobusqueda)

    def rosenbrock_constrained_cubic_line(self, x): 
        return np.array([(1 - x[0])**2 + 100 * (x[1] - (x[0]**2))**2])

    def rosenbrock_constrained_cubic_line_restriction(self, x):
        return (((x[0] - 1)**3 - x[1] + 1)) >= 0 and (x[0] + x[1] - 2) <= 0
        
    def rosenbrock_constrained_disk(self, x): 
        return np.array([(1 - x[0])**2 + 100 * (x[1] - (x[0]**2))**2])

    def rosenbrock_constrained_disk_restriction(self, x):
        return (x[0]**2 + x[1]**2)

    def mishras_bird_constrained(self, x):
        return np.sin(x[1]) * np.exp((1 - np.cos(x[0]))**2) + np.cos(x[0]) * np.exp((1 - np.sin(x[1]))**2) + (x[0] - x[1])**2

    def mishras_bird_constrained_restriction(self, x):
        return (x[0] + 5)**2 + (x[1] + 5)**2 < 25

    def townsend_function_modified(self, x):
        return -(np.cos((x[0] - 0.1) * x[1]))**2 - x[0] * np.sin(3 * x[0] + x[1])

    def townsend_function_modified_restriction(self, x):
        t = np.arctan2(x[1], x[0])
        op1 = x[0]**2 + x[1]**2
        op2 = (2 * np.cos(t) - 0.5 * np.cos(2 * t) - 0.25 * np.cos(3 * t) - 0.125 * np.cos(4 * t))**2 + (2 * np.sin(t))**2
        return op1 < op2

    def gomez_levy_function_modified(self, x):
        return 4 * x[0]**2 - 2.1 * x[0]**4 + (1 / 3) * x[0]**6 + x[0] * x[1] - 4 * x[1]**2 + 4 * x[1]**4

    def gomez_levy_function_modified_restriction(self, x):
        return -np.sin(4 * np.pi * x[0]) + 2 * np.sin(2 * np.pi * x[1])**2 <= 1.5

    def simionescu_function(self, x):
        return 0.1 * (x[0] * x[1])

    def simionescu_function_restriction(self, x):
        r_T = 1
        r_S = 0.2
        n = 8
        angulo = np.arctan2(x[1], x[0]) 
        cosine_term = np.cos(n * angulo)
        op = (r_T + r_S * cosine_term) ** 2
        return x[0]**2 + x[1]**2 - op

    def get_function(self):
        func = getattr(self, self.name.lower(), None)
        if func is None:
            raise ValueError(f"Function '{self.name}' is not defined in the class.")
        return func
    def get_limitesup(self):
        return self.limiteinf[0]
    
    def get_limiteinf(self):
        return self.limitesup[1]