import numpy.typing as npt


class Initializer:
    def __init__(self, dimensions: int):
        self.dimensions = dimensions

    def next(self, n: int, lower_bound: npt.ArrayLike, upper_bound: npt.ArrayLike) -> npt.ArrayLike:
        pass
