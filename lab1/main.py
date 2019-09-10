from constants import HIST_INTERVALS, A, R0, M, AU, BU, EXP_N
from distributions import UniformDistribution, SequenceMixin, ExponentialDistribution, GammaDistribution, \
    TriangularDistribution
from lemer import LemerGenerator
from utils import (create_hist, calculate_mathematical_characteristics,
                   checks_on_circumstantial_evidence)

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
    sequence = res.sequence
    create_hist(sequence, HIST_INTERVALS)

    characteristics = calculate_mathematical_characteristics(sequence)
    print('Lemer Generator Results:')
    print(f'Math expectation = {characteristics.math_exp}')
    print(f'Dispersion = {characteristics.dispersion}')
    print(f'Mean square deviation = {characteristics.square_dev}')
    print()

    checks_on_circumstantial_evidence(sequence)
    print()

    temp = SequenceMixin(sequence)

    # Uniform Distribution
    uniform = UniformDistribution(AU, BU)
    create_hist(uniform.sequence, HIST_INTERVALS)
    print('Uniform Distribution Results:')
    print(f'Math expectation = {uniform.mean}')
    print(f'Dispersion = {uniform.dispersion}')
    print(f'Mean square deviation = {uniform.square_dev}')
    print()

    # Exponential Distribution
    exp = ExponentialDistribution(EXP_N)
    create_hist(exp.sequence, HIST_INTERVALS)
    characteristics = calculate_mathematical_characteristics(exp.sequence)
    print('Exponential Distribution:')
    print(f'Math expectation = {characteristics.math_exp}')
    print(f'Dispersion = {characteristics.dispersion}')
    print(f'Mean square deviation = {characteristics.square_dev}')
    print()

    # Gamma Distribution
    gamma = GammaDistribution(EXP_N, 45)
    create_hist(gamma.sequence, HIST_INTERVALS)
    print('Gamma Distribution:')
    print(f'Math expectation = {gamma.mean}')
    print(f'Dispersion = {gamma.dispersion}')
    print(f'Mean square deviation = {gamma.square_dev}')
    print()

    # Triangular Distribution
    triangle = TriangularDistribution(7, 12)
    create_hist(triangle.sequence, HIST_INTERVALS)
    characteristics = calculate_mathematical_characteristics(triangle.sequence)
    print('Triangular Distribution:')
    print(f'Math expectation = {characteristics.math_exp}')
    print(f'Dispersion = {characteristics.dispersion}')
    print(f'Mean square deviation = {characteristics.square_dev}')
    print()
