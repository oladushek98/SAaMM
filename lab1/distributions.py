import numpy as np


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
    def math_exp(self):
        return (self.a + self.b) / 2

    @property
    def dispersion(self):
        return ((self.b - self.a) ** 2) / 12

    @property
    def square_dev(self):
        return np.array(self.sequence).std()


class GaussDistribution:

    def __init__(self, n, mean, std):
        self.n = n
        self.mean = mean
        self.std = std

    @property
    def sequence(self):
        return [self.mean + self.std * np.sqrt(12 / self.n) * (sum(SequenceMixin.SEQUENCE[i:i + self.n]) - self.n / 2)
                for i in range(0, len(SequenceMixin.SEQUENCE), self.n)]

    @property
    def math_exp(self):
        return self.mean

    @property
    def dispersion(self):
        return np.array(self.sequence).var()

    @property
    def square_dev(self):
        return self.std


class ExponentialDistribution:

    def __init__(self, lamb):
        self.lamb = lamb

    @property
    def sequence(self):
        return [-np.log(item) / self.lamb for item in SequenceMixin.SEQUENCE]


class GammaDistribution:

    def __init__(self, tett, lamb):
        self.tett = tett
        self.lamb = lamb

    @property
    def sequence(self):
        return [-(sum(np.log(SequenceMixin.SEQUENCE[:i]))) / self.lamb for i in range(self.tett)]

    @property
    def math_exp(self):
        return self.tett / self.lamb

    @property
    def dispersion(self):
        return self.tett / (self.lamb ** 2)

    @property
    def square_dev(self):
        return np.array(self.sequence).std()


class TriangularDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def sequence(self):
        right_list = [self.a + (self.b - self.a) * max(SequenceMixin.SEQUENCE[i], SequenceMixin.SEQUENCE[i + 1])
                      for i in range(0, len(SequenceMixin.SEQUENCE), 2)
                      if SequenceMixin.SEQUENCE[i] < SequenceMixin.SEQUENCE[i + 1]]
        left_list = [self.a + (self.b - self.a) * min(SequenceMixin.SEQUENCE[i], SequenceMixin.SEQUENCE[i + 1])
                     for i in range(0, len(SequenceMixin.SEQUENCE), 2)
                     if SequenceMixin.SEQUENCE[i] + SequenceMixin.SEQUENCE[i + 1] < 1]

        return right_list + left_list


class SimpsonDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.uniform = UniformDistribution(self.a / 2, self.b / 2)

    @property
    def sequence(self):
        return list(map(sum, zip(self.uniform.sequence[::2], self.uniform.sequence[1::2])))
