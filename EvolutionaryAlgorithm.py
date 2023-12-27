import sys
import os

# Get the current script's directory 
script_directory = os.path.dirname(os.path.realpath(__file__))

# Calculate the project directory path by going up one level from the script directory
project_directory = os.path.abspath(os.path.join(script_directory, ".."))

# Add the project directory to the Python path
sys.path.append(project_directory)

# imports
import random
from Polynomials.PolynomialsGenerator import PolynomialsGenerator
from Polynomials.Polynomial import Polynomial

class PolynomialEvolutionaryAlgorithm:
    def __init__(self, n,  chromosome_type="Roots", heuristic_type="HVSymetry", degree=4):
        self.n = n
        self.population = []
        self.best_fitness = 0
        self.best_polynomial = None
        self.best_type = None
        self.chromosome_type = chromosome_type
        self.heuristic_type = heuristic_type
        self.degree = degree
        self.polynomial_generator = PolynomialsGenerator(chromosome_type,heuristic_type, degree)
        pre_population = self.polynomial_generator.generates(n)
        for polynomial in pre_population:
            self.population.append([polynomial.global_fitness, polynomial.chromosomes, "Original"])
        
    def evaluate(self, chromosomes):
        p = Polynomial(self.heuristic_type,self.chromosome_type,chromosomes)
        return p.global_fitness

    def mutate(self, chromosomes):
        if self.chromosome_type == "Roots":
            mutate_range = range(0,self.degree)
        else:
            mutate_range = range(1,self.degree)

        for i in mutate_range:
            if random.random() < 0.2:
                chromosomes[i] = self.polynomial_generator.generate_chromosome(i)
        return chromosomes

    def crossover(self, chromosomes1, chromosomes2):
        if self.chromosome_type == "Roots":
            split_index = random.randint(1, self.degree-1)
        else: 
            # Coefficients, suppose that the last coefficient is the constant 0 
            # and the first coefficient is the coefficient of the highest degree equals to 1
            split_index = random.randint(2, self.degree-2)
        new_chromosomes = chromosomes1[:split_index] + chromosomes2[split_index:]
        return new_chromosomes

    def evolve(self):
        for i in range(self.n):
            if random.random() < 0.8:
                type_new_chromosomes = "Crossover"
                parent1 = random.choice(self.population)[1]
                parent2 = random.choice(self.population)[1]
                new_chromosomes = self.crossover(parent1, parent2)
            else:
                type_new_chromosomes = "Mutation"
                parent = random.choice(self.population)[1]
                new_chromosomes = self.mutate(parent)
            self.population.append([self.evaluate(new_chromosomes), new_chromosomes, type_new_chromosomes ])
        self.update_best()

    def update_best(self):
        self.population.sort()
        self.best_fitness = self.population[-1][0]
        self.best_polynomial = self.population[-1][1]
        self.best_type = self.population[-1][2]
        self.population = self.population[ -self.n : ]