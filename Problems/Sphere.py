import numpy as np
import numpy.typing as npt
from Problems.Problem import Problem


class Sphere(Problem):
    def __init__(self, dimensions: int):
        super().__init__(dimensions)

    def fitness(self, candidate: npt.ArrayLike) -> float:
        return float(np.sum(np.power(candidate, 2), dtype=float))
