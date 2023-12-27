import EvolutionaryAlgorithm

test = EvolutionaryAlgorithm.PolynomialEvolutionaryAlgorithm(10)
test.population.sort()
print(test.population)
i = 0
while test.best_fitness < 0.95  and i < 1000000:
    test.evolve()
    i += 1
    print("generation:",i, ". BF", round(test.best_fitness,7), ". BP", test.best_polynomial, ". TB", test.best_type, ".")


