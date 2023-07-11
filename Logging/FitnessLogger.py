import math
import unittest


class FitnessLogger:
    def __init__(self, iterations: int, intervals: int, offset: float):
        self.iterations = iterations
        self.intervals = min(intervals, self.iterations)
        self.stride = int(self.iterations / self.intervals)
        self.offset = int(offset * self.stride)
        self.maxIntervals = int(math.ceil((self.iterations - self.offset) / self.stride))
        self.fitnessHistory = []

    def add(self, iteration: int, fitness: float, feasible: bool):
        if (iteration - self.offset) % self.stride == 0:
            index = (iteration - self.offset) // self.stride
            if index < self.maxIntervals:
                self.log(index, fitness, feasible)

    def log(self, index: int, fitness: float, feasible: bool):
        pass


class TestFitnessLogger(unittest.TestCase):
    def test_init_intervals_when_gt_iterations_then_correct(self):
        fitnessLogger = FitnessLogger(10, 30, 0)
        self.assertEqual(10, fitnessLogger.intervals)

    def test_init_stride_correct(self):
        fitnessLogger = FitnessLogger(10, 3, 0)
        self.assertEqual(3, fitnessLogger.stride)

    def test_init_offset_correct(self):
        fitnessLogger = FitnessLogger(10, 3, 3)
        self.assertEqual(9, fitnessLogger.offset)

    def test_init_maxInterval_correct(self):
        fitnessLogger = FitnessLogger(10, 3, 0)
        self.assertEqual(4, fitnessLogger.maxIntervals)
