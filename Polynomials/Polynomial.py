import sys
import os

# Get the current script's directory 
script_directory = os.path.dirname(os.path.realpath(__file__))

# Calculate the project directory path by going up one level from the script directory
project_directory = os.path.abspath(os.path.join(script_directory, ".."))

# Add the project directory to the Python path
sys.path.append(project_directory)

from AbstractClasses.AbstractPolynomial import AbstractPolynomial
from HeuristicFunctions.HeuristicFunctions import HeuristicFunctions
import numpy as np

class Polynomial(AbstractPolynomial):
    def __init__(self, heuristic_type, chromosome_type="Roots", chromosomes=None, degree=4, ):
        self.degree = degree
        self.chromosome_type = chromosome_type
        self.chromosomes = chromosomes
        self.heuristic_type = heuristic_type
        self.heuristic_function = HeuristicFunctions(heuristic_type)
        self.global_fitness = 0
        self.x_values = None
        self.y_values = None
        self.evaluate()
        self.obtain_graph()

     
    # In mathematics, a the graph of a function 'f' is represented as a set of ordered pairs (x, y),
    # where f(x) = y. In the common case where 'x' and 'f(x)' are real numbers, 
    # these pairs are Cartesian coordinates of points in a plane and often form a curve.
    # this method returns the x and y values of the polynomial
    def obtain_graph(self):
        # If the polynomial degree is smaller than or equal to 1, the
        # limits will automatically be set to (-15,15), or to a
        # displacement by these amounts from the root, respectively:
        if len(self.roots)==0:
            low_lim=-15
            upp_lim=15
        elif len(self.roots)==1:
            low_lim=self.roots[0]-15
            upp_lim=self.roots[0]+15
        # Otherwise the limits will be set according to the smallest and
        # highest roots (plus/minus a displacement of 10% of the
        # difference):
        else:
            smallest=min(self.roots)
            largest=max(self.roots)
            if largest - smallest > 10**-5: 
                diff=largest-smallest
            else:
                diff = largest
            low_lim=smallest-diff*0.1
            upp_lim=largest+diff*0.1
        # Creates a list of 50 evenly-spaced x-values between the two
        # specified limits:
        x_values=np.linspace(low_lim,upp_lim)
        y_values=[]
        for x in x_values:
            y_values.append(self.polynomial_function_evaluate(x))
        return x_values,y_values
    
    # Returns the result of evaluating the polynomial at the value
    # specified in the argument:
    def polynomial_function_evaluate(self,val):
        res=0
        for i in range(0,len(self.coefficients)):
            res=res+self.coefficients[i]*val**i
        return res

    def evaluate(self):
        """
            Evaluates the polynomial using the heuristic function
        """
        self.global_fitness = self.heuristic_function.evaluate(self)
        
