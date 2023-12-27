from abc import  abstractmethod
from AbstractClasses.AbstractGenerator import AbstractGenerator
class ChromosomeGenerator(AbstractGenerator):
    @abstractmethod
    def generate_chromosome(self, i):
        """
            Generates a chromosome with the given chromosome type
            i: the ith chromosome to generate
        """
        pass
