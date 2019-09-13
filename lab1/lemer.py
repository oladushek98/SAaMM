import sympy

from utils import ParamErrors


class LemerGenerator:

    def __init__(self, a: int, r0: int, m: int, n):
        self.a = a
        self.m = m
        self.lemer_n = n

        # all checks are optional
        if r0 >= (pow(2, self.lemer_n) - 1):
            raise self.ParametersInitializingException(r0, ParamErrors.NOT_LESS.value, 'R0')
        elif not sympy.isprime(r0):
            raise self.ParametersInitializingException(r0, ParamErrors.NOT_PRIME.value, 'R0')
        else:
            self.r0 = r0

    @property
    def sequence(self):
        sequence = []
        rn_1 = self.r0

        for _ in range(self.lemer_n):
            rn = (rn_1 * self.a) % self.m
            rn_1 = rn
            r = rn / self.m
            sequence.append(r)

        if self.lemer_n % 2 != 0:
            sequence.append(sum((sequence[-1], sequence[-3], sequence[-5])) / 3)

        return sequence

    class ParametersInitializingException(Exception):

        def __init__(self, param, mes, param_name):
            super().__init__()
            self.mes = mes
            self.param = param
            self.param_name = param_name

        def __str__(self):
            return f'Parameter "{self.param_name}" of value {self.param} does\'t meet the requirement: {self.mes}'
