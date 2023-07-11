import numpy as np
import numpy.typing as npt

from Initializers.Initializer import Initializer


class RandomInitializer(Initializer):
    def __init__(self, dimensions: int):
        super().__init__(dimensions)

    def next(self, n: int, lower_bound: npt.ArrayLike, upper_bound: npt.ArrayLike) -> npt.ArrayLike:
        rand_value = np.random.random(self.dimensions)
        return rand_value * (upper_bound - lower_bound) + lower_bound
