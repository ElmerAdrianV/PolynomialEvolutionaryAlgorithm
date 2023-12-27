from abc import ABC, abstractmethod

class ChromosomeGenerator(ABC):
    @abstractmethod
    def generate(self):
        """
            Generates a set of chromosomes
        """
        pass
    @abstractmethod
    def generate_chromosome(self):
        """
            Generates a chromosome with the given chromosome type
        """
        pass
