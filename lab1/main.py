from constants import HIST_INTERVALS, A, R0, M
from lemer import LemerGenerator
from utils import create_hist, calculate_mathematical_characteristics


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
