from Logging.FitnessLogger import FitnessLogger


class FileLogger(FitnessLogger):
    def __init__(self, iterations: int, intervals: int, offset: float, file_path: str):
        super().__init__(iterations, intervals, offset)
        self.filePath = file_path
        # write header
        with open(self.filePath, "w") as file:
            file.write("Iteration, Fitness, Feasible\n")

    def log(self, index: int, fitness: float, feasible: bool = True):
        with open(self.filePath, "a") as file:
            file.write(f'{index}, {fitness}, {feasible}\n')
