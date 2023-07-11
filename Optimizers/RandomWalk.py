import time
import unittest
from typing import Optional

import numpy as np
import numpy.typing as npt

from Initializers.Initializer import Initializer
from Initializers.RandomInitializer import RandomInitializer
from Logging.FileLogger import FileLogger
from Logging.FitnessLogger import FitnessLogger
from Optimizers.Optimizer import Optimizer
from Problems.Problem import Problem
from Problems.Sphere import Sphere


class RandomWalk(Optimizer):
    def __init__(self, problem: Problem, fitness_logger: FitnessLogger, initializer: Optional[Initializer] = None):
        super().__init__(problem, fitness_logger)
        self.name: str = "RandomWalk"
        # Check Initializer and default
        if initializer is None:
            self.initializer = RandomInitializer(self.problem.dimensions)
        else:
            self.initializer = initializer

        # Initialize starting value as best
        self.best: npt.ArrayLike = self.initializer.next(self.iteration, self.problem.lowerInit, self.problem.upperInit)
        self.bestFitness: float = self.problem.fitness(self.best)

    def optimize(self):
        # Increment iteration value
        self.iteration += 1
        # Use initializer for next position
        new_value = self.initializer.next(self.iteration, self.problem.lowerBound, self.problem.upperBound)
        new_fitness = self.problem.fitness(new_value)
        # If current is better replace best
        if self.bestFitness > new_fitness:
            self.best = new_value
            self.bestFitness = new_fitness
        # Log current fitness
        self.fitnessLogger.add(self.iteration, self.bestFitness, True)

class TestRandomWalkOptimizer(unittest.TestCase):
    def test_init_when_none_initializer_then_random_initializer(self):
        dimensions = 2
        iterations = 10000
        problem = Sphere(dimensions)
        logger = FitnessLogger(iterations, 1, 0)
        initializer = None
        optimizer = RandomWalk(problem, logger, initializer)
        self.assertIsNotNone(optimizer.initializer)

    def test_optimize_improves(self):
        dimensions = 2
        iterations = 10000
        problem = Sphere(dimensions)
        logger = FitnessLogger(iterations, 1, 0)
        initializer = None
        optimizer = RandomWalk(problem, logger, initializer)
        starting_fitness = optimizer.bestFitness
        # should find an improved fitness in 100 iterations
        for i in range(100):
            optimizer.optimize()
        self.assertEqual(100, optimizer.iteration)
        self.assertTrue(starting_fitness > optimizer.bestFitness)



