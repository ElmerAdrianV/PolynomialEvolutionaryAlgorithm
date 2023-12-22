# Path: AlgoritmoEvolutivoPolinomios/v1/coeficientes/CoefficientGenerator.py
import numpy as np
import random
import threading
import time

class Generator_Coefficients_Thread(threading.Thread):
    def __init__(self, limit_inf=-10, limit_sup=10,n = 100000, degree=4):
        """
        Generate  a set of n coefficients of a polynomial of degree (degree) with degre - 1 random roots
        between -10 and 10 and 0 root to serve as population in the mutation in a genetic algorithm
        Input:
            n: number of coefficients to generate
            degree: degree of the polynomial
        """
        threading.Thread.__init__(self)
        self.limit_inf = limit_inf
        self.limit_sup = limit_sup
        self.n = n
        self.degree = degree
        

    def run(self):
        for i in range(self.n):
            # Generate {degree} random roots between -10 and 10
            roots = [random.uniform(self.limit_inf, self.limit_sup) for _ in range(self.degree-1)]+[0]
            # Calculate the coefficients of the polynomial
            coefficients = np.poly(roots)
            # Save each coefficient in a separate file
            for j in range(self.degree - 1, 0, -1):
                with open(f"coef_{j}.csv", 'a') as f:
                    f.write(str(coefficients[j]))
                    f.write('\n')


class CoefficientGenerator:
    def __init__(self, num_threads=4, coefficients_per_thread=100000, degree=4):
        """
        Initialize the coefficient generator.
        Input:
            num_threads: Number of threads to use for coefficient generation.
            coefficients_per_thread: Number of coefficients to generate per thread.
            degree: Degree of the polynomial.
        """
        self.num_threads = num_threads
        self.coefficients_per_thread = coefficients_per_thread
        self.degree = degree

    def generate_coefficients(self):
        # Create and start threads
        threads = []
        for _ in range(self.num_threads):
            thread = Generator_Coefficients_Thread(self.coefficients_per_thread, self.degree)
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    start_time = time.time()
    generator = CoefficientGenerator(num_threads=16, coefficients_per_thread=500000, degree=4)
    generator.generate_coefficients()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Generation took {elapsed_time:.2f} seconds")



