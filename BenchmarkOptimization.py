import time

from Initializers.RandomInitializer import RandomInitializer
from Logging.FileLogger import FileLogger
from Optimizers.RandomWalk import RandomWalk
from Problems.Sphere import Sphere

if __name__ == "__main__":
    dimensions = 2
    iterations = 10000
    problem = Sphere(dimensions)
    logger = FileLogger(iterations, iterations, 0, "random_walk_fitness.csv")
    initializer = RandomInitializer(dimensions)

    start = time.time()
    optimizer = RandomWalk(problem, logger, initializer)
    print(f'Starting Best Fitness: {optimizer.bestFitness}')
    for i in range(iterations):
        optimizer.optimize()
    end = time.time()

    print(f'Best Fitness Found: {optimizer.bestFitness}')
    print(f'Elapsed Time: {end - start}')