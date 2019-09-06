from constants import HIST_INTERVALS, A, R0, M, AU, BU
from distributions import UniformDistribution, SequenceMixin
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

    a = A
    r0 = R0
    m = M

    res = LemerGenerator(a, r0, m)
    sequence = res.sequence
    create_hist(sequence, HIST_INTERVALS)

    characteristics = calculate_mathematical_characteristics(sequence)
    print(f'Math expectation = {characteristics.math_exp}')
    print(f'Dispersion = {characteristics.dispersion}')
    print(f'Mean square deviation = {characteristics.square_dev}')
    print()

    checks_on_circumstantial_evidence(sequence)

    temp = SequenceMixin(sequence)

    uniform = UniformDistribution(AU, BU)
    create_hist(uniform.sequence, HIST_INTERVALS)
    print(uniform.mean, uniform.dispersion, uniform.square_dev)
