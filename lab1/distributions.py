import numpy as np

from lemer import LemerGenerator
# from main import sequence as SEQUENCE


class UniformDistribution:

    def __init__(self, a, b, seq):
        self.a = a
        self.b = b
        self.lemer = seq

    @property
    def sequence(self):
        return [self.a + (self.b - self.a) * item for item in self.lemer]

    @property
    def mean(self):
        return (self.a + self.b) / 2

    @property
    def dispersion(self):
        return ((self.b - self.a) ** 2) / 12

    @property
    def square_dev(self):
        return np.array(self.sequence).std()
