import sys
import os

# Get the current script's directory 
script_directory = os.path.dirname(os.path.realpath(__file__))

# Calculate the project directory path by going up one level from the script directory
project_directory = os.path.abspath(os.path.join(script_directory, ".."))

# Add the project directory to the Python path
sys.path.append(project_directory)

from AbstractClasses import AbstractPolynomial
import HeuristicFunctions

def Polynomial(AbstractPolynomial):
    def __init__(self, heuristic_type, chromosome_type="Roots", chromosomes=None, degree=4, ):
        self.degree = degree
        self.chromosome_type = chromosome_type
        self.chromosomes = chromosomes
        self.heuristic_type = heuristic_type
        self.heuristic_function = HeuristicFunctions(heuristic_type)
        self.global_fitness = 0
        self.evaluate()        

    def evaluate(self):
        """
            Evaluates the polynomial using the heuristic function
        """
        self.global_fitness = self.heuristic_function.evaluate(self)
        
