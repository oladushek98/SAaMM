import sympy

from constants import LEMER_N
from utils import ParamErrors
from utils import find_ones_in_binary


class LemerGenerator:

    def __init__(self, a: int, r0: int, m: int):
        self.a = a
        self.m = m

        if r0 >= (pow(2, LEMER_N) - 1):
            raise self.ParametersInitializingException(r0, ParamErrors.NOT_LESS.value, 'R0')
        elif not sympy.isprime(r0):
            raise self.ParametersInitializingException(r0, ParamErrors.NOT_PRIME.value, 'R0')
        # elif not find_ones_in_binary(r0):
        #     raise self.ParametersInitializingException(r0, ParamErrors.NOT_ENOUGH_ONES.value, 'R0')
        else:
            self.r0 = r0

    @property
    def sequence(self):
        sequence = []
        rn_1 = self.r0
        for _ in range(LEMER_N):
            rn = (rn_1 * self.a) % self.m
            rn_1 = rn
            r = rn / self.m
            sequence.append(r)

        return sequence

    class ParametersInitializingException(Exception):

        def __init__(self, param, mes, param_name):
            super().__init__()
            self.mes = mes
            self.param = param
            self.param_name = param_name

        def __str__(self):
            return f'Parameter "{self.param_name}" of value {self.param} does\'t meet the requirement: {self.mes}'
