import random
from Polynomials import PolynomialsGenerator
from Polynomials import Polynomial

class PolynomialEvolutionaryAlgorithm:
    def __init__(self, n):
        self.n = n
        self.population = []
        self.best_fitness = 0
        self.best_polynomial = None
        self.best_type = None
        self.polynomial_generator = PolynomialsGenerator()
        self.population = self.polynomial_generator.generate(n)
        
    def evaluate(self, chromosomes):
        p = Polynomial(chromosomes)
        return p.evaluate

    def mutate(self, chromosomes):
        for i in range(4):
            if random.random() < 0.2:
                chromosomes[i] = random.uniform(-100, 100)
        return chromosomes

    def crossover(self, chromosomes1, chromosomes2):
        split_index = random.randint(1, 3)
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
            self.population.append([self.evaluate_poly(new_chromosomes), new_chromosomes, type_new_chromosomes ])
        self.update_best()

    def update_best(self):
        self.population.sort()
        self.best_fitness = self.population[-1][0]
        self.best_polynomial = self.population[-1][1]
        self.best_type = self.population[-1][2]
        self.population = self.population[ -self.n : ]