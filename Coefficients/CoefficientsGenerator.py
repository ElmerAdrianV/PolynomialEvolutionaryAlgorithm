# coefficients/CoefficientsGenerator.py
import sys
import os

# Get the current script's directory (CoefficientssGenerator.py's directory)
script_directory = os.path.dirname(os.path.realpath(__file__))

# Calculate the project directory path by going up one level from the script directory
project_directory = os.path.abspath(os.path.join(script_directory, ".."))

# Add the project directory to the Python path
sys.path.append(project_directory)


import random
import csv
import numpy as np
from AbstractClasses import AbstractGenerator

class CoefficientsGenerator(AbstractGenerator):
    def __init__(self, root_dir="/Users/elmeradrianv/dogfood/AlgoritmoEvolutivoPolinomios/v1/coefficients/", length_database=400000, degree=4):
        """
        Initialize the coefficient generator.
        Input:
            root_dir: Directory containing the coefficient files.
            length_database: Number of coefficients in each file.
            degree: Degree of the polynomial.
        """
        self.degree = degree
        self.length_database = length_database
        self.coef_files = []

        for file_number in range(1, self.degree):
            file_path = f"coef_{file_number}.csv"
            with open(root_dir + file_path, "r") as file:
                reader_i = csv.reader(file)
                lines_i = list(reader_i)
                self.coef_files.append(np.array(lines_i, dtype=float))

    def generate(self):
        """
        Generate a set of coefficients from the coefficient files.
        Output:
            A list of coefficients. It's suppose that one of the
            indepent coefficients is 0, so the list will have degree -1 elements.
        """
        coefficients = []
        for file_number in range(1, self.degree):
            k = random.randint(1, self.length_database)
            coefficient = self.get_coefficient(k, self.coef_files[file_number - 1])
            coefficients.append(coefficient)
        return coefficients

    def get_coefficient(self, k, coef_file):
        """
        Get the k-th coefficient from the given file.
        Input:
            k: Index of the coefficient to get.
            coef_file: Coefficient file.
        Output:
            The k-th coefficient.
        """
        if k < 0 or k >= len(coef_file):
            raise IndexError("Invalid line index")

        coefficient = coef_file[k, 0]

        return coefficient
    
