import sys
import os

# Get the current script's directory (RootsGenerator.py's directory)
script_directory = os.path.dirname(os.path.realpath(__file__))

# Calculate the project directory path by going up one level from the script directory
project_directory = os.path.abspath(os.path.join(script_directory, ".."))

# Add the project directory to the Python path
sys.path.append(project_directory)

from AbstractClasses.AbstractGenerator import AbstractGenerator
from Roots.RootsGenerator import RootsGenerator
from Coefficients.CoefficientsGenerator import CoefficientsGenerator
from Polynomials.Polynomial import Polynomial

class PolynomialsGenerator(AbstractGenerator):
    def __init__(self, chromosome_type="Roots", heuristic_type="Random"):
        """
            Class generator of a population of polynomials with a given chromosome type and heuristic type
            Input:
                chromosomeType: type of chromosome to use between the following options:
                    - "Roots"
                    - "Coefficients"
                heuristic_type: type of heuristic to use between the following options:
                
        """
        self.chromosome_type = chromosome_type

        if chromosome_type == "Roots":
            self.chromosome_generator = RootsGenerator()
        elif chromosome_type == "Coefficients":
            self.chromosome_generator = CoefficientsGenerator()
        
        self.heuristic_type = heuristic_type

    def generates(self, count):
        """
            Generates a population of polynomials with the given chromosome type and heuristic type
            Input:
                count: number of polynomials to generate
            Output:
                polynomials: list of polynomials generated
        """

        polynomials = []
        for _ in range(count):
            polynomial = self.generate()
            polynomials.append(polynomial)
        return polynomials

    def generate(self):
        """
            Generates a polynomial with the given chromosome type and heuristic type
        """
        chromosomes = self.chromosome_generator.generate()
        return  Polynomial(self.heuristic_type, self.chromosome_type,chromosomes)
        
