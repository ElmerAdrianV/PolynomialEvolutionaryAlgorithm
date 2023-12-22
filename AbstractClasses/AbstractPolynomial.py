from abc import ABC, abstractmethod


class AbstractPolynomial(ABC):
    def __init__(self, chromosomeType, degree=4):
        pass

    #@abstractmethod
    #def graph_polyn(self, plot=False):
    #    pass

    @abstractmethod
    def evaluate(self):
        pass

