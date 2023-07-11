import numpy as np
import numpy.typing as npt


class Problem:
    def __init__(self, dimensions: int, maxevaulations: int = 10000):
        self.dimensions = dimensions
        self.lowerBound = np.zeros(dimensions)
        self.upperBound = np.ones(dimensions)
        self.lowerInit = np.zeros(dimensions)
        self.upperInit = np.ones(dimensions)
        self.maximumFitness = float("inf")
        self.minimumFitness = 0.0
        self.acceptableFitness = 1.0e-4
        # Track and increment the number of evaluations of fitness for execution based stopping criteria
        self.evaluations = 0
        self.maxEvaluations = maxevaulations

    def fitness(self, candidate: npt.ArrayLike) -> float:
        pass

    def should_continue(self):
        return self.evaluations < self.maxEvaluations
