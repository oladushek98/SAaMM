from constants import (A, R0, M, AU, BU, EXP_N,
                       LEMER, UNIFORM, EXPONENTIAL, GAMMA, TRIANGULAR, SIMPSON)
from distributions import (UniformDistribution, SequenceMixin, ExponentialDistribution, GammaDistribution,
                           TriangularDistribution, SimpsonDistribution)
from lemer import LemerGenerator
from utils import (checks_on_circumstantial_evidence, show_info)

if __name__ == '__main__':

    # print('Enter A:')
    # a = int(input())
    # print('Enter R0:')
    # r0 = int(input())
    # print('Enter M:')
    # m = int(input())

    # Lemer Generator
    a = A
    r0 = R0
    m = M

    res = LemerGenerator(a, r0, m)
    show_info(res, LEMER)

    checks_on_circumstantial_evidence(res.sequence)
    print()

    temp = SequenceMixin(res.sequence)

    # Uniform Distribution
    uniform = UniformDistribution(AU, BU)
    show_info(uniform, UNIFORM)

    # Exponential Distribution
    exp = ExponentialDistribution(EXP_N)
    show_info(exp, EXPONENTIAL)

    # Gamma Distribution
    gamma = GammaDistribution(EXP_N, 45)
    show_info(gamma, GAMMA)

    # Triangular Distribution
    triangle = TriangularDistribution(7, 12)
    show_info(triangle, TRIANGULAR)

    # Simpson Distribution
    simpson = SimpsonDistribution(7, 12)
    show_info(simpson, SIMPSON)
