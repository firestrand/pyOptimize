import numpy.typing as npt
from Logging.FitnessLogger import FitnessLogger
from Problems.Problem import Problem


class Optimizer(Problem):
    def __init__(self, problem: Problem, fitnesslogger: FitnessLogger):
        super().__init__(dimensions=0)
        self.name = ""
        self.problem = problem
        self.fitnessLogger = fitnesslogger
        self.iteration = 0

    def default_parameters(self) -> npt.ArrayLike:
        return []

    def optimize(self):
        pass
