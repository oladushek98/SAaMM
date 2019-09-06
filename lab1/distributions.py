import numpy as np

from utils import calculate_mathematical_characteristics


class SequenceMixin:
    SEQUENCE = []

    def __init__(self, seq):
        self.sequence_setter(seq)

    @classmethod
    def sequence_setter(cls, seq):
        cls.SEQUENCE = seq


class UniformDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def sequence(self):
        return [self.a + (self.b - self.a) * item for item in SequenceMixin.SEQUENCE]

    @property
    def mean(self):
        return (self.a + self.b) / 2

    @property
    def dispersion(self):
        return ((self.b - self.a) ** 2) / 12

    @property
    def square_dev(self):
        return np.array(self.sequence).std()


class GaussDistribution:

    def __init__(self, n):
        self.n = n


class ExponentialDistribution:

    def __init__(self, lamb):
        self.lamb = lamb

    @property
    def sequence(self):
        return [-np.log(item) / self.lamb for item in SequenceMixin.SEQUENCE]
