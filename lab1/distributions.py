import numpy as np

from lemer import LemerGenerator
from constants import A, R0, M


class SequenceMixin:
    SEQUENCE = []
    LEN = 0

    def __init__(self, seq):
        self.sequence_setter(seq)

    @classmethod
    def sequence_setter(cls, seq):
        cls.SEQUENCE = seq
        cls.LEN = len(seq)


class UniformDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def sequence(self):
        return [self.a + (self.b - self.a) * item for item in SequenceMixin.SEQUENCE]


class GaussDistribution:

    def __init__(self, n, mean, std):
        self.n = n
        self.mean = mean
        self.std = std

    @property
    def sequence(self):
        return [
                self.mean + self.std * np.sqrt(12 / self.n) *
                (sum(SequenceMixin.SEQUENCE[i:i + self.n]) - self.n / 2)
                for i in range(0, SequenceMixin.LEN, self.n)
        ]


class ExponentialDistribution:

    def __init__(self, lamb):
        self.lamb = lamb

    @property
    def sequence(self):
        return [-np.log(item) / self.lamb for item in SequenceMixin.SEQUENCE]


class GammaDistribution(LemerGenerator):

    def __init__(self, tett, lamb, length=1000):
        super().__init__(A, R0, M, length * tett)
        self.tett = tett
        self.lamb = lamb
        self.lemer_sequence = super().sequence

    @property
    def sequence(self):
        def vector(x):
            if self.tett == 1:
                return x
            result = 1
            for i in range(self.lemer_sequence.index(x), self.lemer_sequence.index(x) + self.tett):
                result *= self.lemer_sequence[i - (self.tett - 1)]

            return result

        return list(map(lambda x: -1 / self.lamb * np.log(vector(x)), self.lemer_sequence))


class TriangularDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def sequence(self):
        right_list = [
            self.a + (self.b - self.a) * max(SequenceMixin.SEQUENCE[i], SequenceMixin.SEQUENCE[i + 1])
            for i in range(0, SequenceMixin.LEN, 2)
            if SequenceMixin.SEQUENCE[i] < SequenceMixin.SEQUENCE[i + 1]
        ]
        left_list = [
            self.a + (self.b - self.a) * min(SequenceMixin.SEQUENCE[i], SequenceMixin.SEQUENCE[i + 1])
            for i in range(0, SequenceMixin.LEN, 2)
            if SequenceMixin.SEQUENCE[i] + SequenceMixin.SEQUENCE[i + 1] < 1
        ]

        return right_list + left_list


class SimpsonDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.uniform = UniformDistribution(self.a / 2, self.b / 2)

    @property
    def sequence(self):
        return list(map(sum, zip(self.uniform.sequence[::2], self.uniform.sequence[1::2])))
