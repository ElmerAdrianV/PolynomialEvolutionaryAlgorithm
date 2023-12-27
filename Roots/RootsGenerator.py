import sys
import os

# Get the current script's directory (RootsGenerator.py's directory)
script_directory = os.path.dirname(os.path.realpath(__file__))

# Calculate the project directory path by going up one level from the script directory
project_directory = os.path.abspath(os.path.join(script_directory, ".."))

# Add the project directory to the Python path
sys.path.append(project_directory)

# Now, you can import from AbstractClasses
from AbstractClasses.ChromosomeGenerator import ChromosomeGenerator
import random

class RootsGenerator(ChromosomeGenerator):
    def __init__(self, limit_inf=-10, limit_sup=10, degree=4):
        """
        Initialize the roots generator.
        Input:
            degree: Degree of the polynomial.
        """
        self.limit_inf = limit_inf
        self.limit_sup = limit_sup
        self.degree = degree

    def generate(self):
        """
        Get a set of roots.
        Output:
            A list of roots. It's suppose that one of the roots is 0, to h so the list will have degree -1 elements.
        """
        # Add 0 as a root
        return [0]+[random.uniform(self.limit_inf, self.limit_sup) for _ in range(self.degree-1)]
    def generate_chromosome(self, i):
        return random.uniform(self.limit_inf, self.limit_sup)
