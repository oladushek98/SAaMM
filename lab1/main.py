from constants import (A, R0, M, AU, BU, EXP_N,
                       LEMER, UNIFORM, EXPONENTIAL, GAMMA, TRIANGULAR, SIMPSON, GAUSSIAN_N, GAUSS, LEMER_N)
from distributions import (UniformDistribution, SequenceMixin, ExponentialDistribution, GammaDistribution,
                           TriangularDistribution, SimpsonDistribution, GaussDistribution)
from lemer import LemerGenerator
from utils import (checks_on_circumstantial_evidence, show_info, calculate_period)

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

    lemer = LemerGenerator(a, r0, m, LEMER_N)
    show_info(lemer, LEMER)

    checks_on_circumstantial_evidence(lemer.sequence)
    print()
    calculate_period(lemer.sequence)
    print()

    temp = SequenceMixin(lemer.sequence)

    # Uniform Distribution
    uniform = UniformDistribution(AU, BU)
    show_info(uniform, UNIFORM)

    # Gaussian Distribution
    gauss = GaussDistribution(GAUSSIAN_N, 1, 0.5)
    show_info(gauss, GAUSS)

    # Exponential Distribution
    exp = ExponentialDistribution(EXP_N)
    show_info(exp, EXPONENTIAL)

    # Gamma Distribution
    gamma = GammaDistribution(4, 5)
    show_info(gamma, GAMMA)

    # Triangular Distribution
    triangle = TriangularDistribution(7, 12)
    show_info(triangle, TRIANGULAR)

    # Simpson Distribution
    simpson = SimpsonDistribution(7, 12)
    show_info(simpson, SIMPSON)

    xv = lemer.sequence[-1]
    lst = []
    for i in range(len(lemer.sequence)):
        if lemer.sequence[i] == xv:
            if len(lst) >= 2:
                break
            lst.append(i)
    p = lst[1] - lst[0]
    print(p)
