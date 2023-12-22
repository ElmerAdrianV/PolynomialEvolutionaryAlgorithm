from abc import ABC, abstractmethod


class AbstractPolynomial(ABC):
    def __init__(self, chromosomes, deg=4):
        self.deg = deg
        self.chromosomes = chromosomes
        self.global_fitness = self.evaluate()

    #@abstractmethod
    #def graph_polyn(self, plot=False):
    #    pass

    @abstractmethod
    def evaluate(self):
        pass

