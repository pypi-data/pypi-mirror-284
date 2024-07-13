import numpy as np
import warnings
class funcion:
    def __init__(self,name,espaciobussqueda:np.array):
        self.name=name
        self.limiteinf=espaciobussqueda[0]
        self.limitesup=espaciobussqueda[1]
        self.espacio=espaciobussqueda
        self.validate_search_space()
        self.validate_search_space()
    def validate_search_space(self):
        if len(self.espacio) != 2:
            raise ValueError("Search space must be an array of two elements")
        func_name = self.name.lower()
        search_spaces = {
        'himmelblau': [-5, 5, -5, 5],
        'rastrigin': [-5.12, 5.12, -5.12, 5.12],
        'beale': [-4.5, 4.5, -4.5, 4.5],
        'goldstein': [-2, 2, -2, 2],
        'boothfunction': [-10, 10, -10, 10],
        'bukin_n6': [-15, -5, -3, 3],
        'schaffer_n2': [-100, 100, -100, 100],
        'schaffer_n4': [-100, 100, -100, 100],
        'styblinski_tang': [-5, 5, -5, 5],
        'rosenbrock_constrained_cubic_line': [-1.5, 1.5, -0.5, 2.5],
        'rosenbrock_constrained_disk': [-1.5, 1.5, -1.5, 1.5],
        'mishras_bird_constrained': [-10, 0, -6.5, 0],
        'townsend_modified': [-2.25, 2.25, -2.25, 1.75],
        'gomez_levy_modified': [-1, 0.75, -1, 1],
        'simionescu_function': [-1.25, 1.25, -1.25, 1.25]
    }
        
        if func_name in search_spaces:
            x_min, x_max, y_min, y_max = search_spaces[func_name]
            if not (x_min <= self.limiteinf[0] <= x_max and y_min <= self.limitesup[0] <= y_max):
                warning_msg = f"Warning: Search space is outside the predefined range for function {func_name}."
                warnings.warn(warning_msg)
    
    def get_function(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def get_limitesup(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def get_limiteinf(self):
        raise NotImplementedError("Subclasses should implement this method.")
