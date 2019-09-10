import typing
import numpy as np

from collections import namedtuple
from enum import Enum
from matplotlib import pyplot as plt

from constants import LEMER_N, HIST_INTERVALS


class ParamErrors(Enum):
    NOT_PRIME = 'should be prime'
    NOT_LESS = 'should be less then 2^N - 1'
    NOT_ENOUGH_ONES = 'should consist more 1s in binary form'


def create_hist(sequence, intervals):
    plt.hist(sequence, intervals)
    plt.show()


def find_ones_in_binary(param):
    binary = bin(param)[2:]
    count = 0
    for _ in binary:
        if _ == '1':
            count += 1

    return True if float(count/len(binary) >= 0.8) else False


def calculate_mathematical_characteristics(sequence) -> typing.NamedTuple:
    array = np.array(sequence)

    m = array.mean()
    d = array.var()
    sig = array.std()

    Characteristics = namedtuple('Characteristics', ['math_exp', 'dispersion', 'square_dev'])

    result = Characteristics(m, d, sig)

    return result


def checks_on_circumstantial_evidence(sequence):
    pairs_list = [(sequence[i], sequence[i + 1]) for i in range(0, len(sequence), 2)]
    k_list = list(filter(lambda pair: pow(pair[0], 2) + pow(pair[1], 2) < 1, pairs_list))
    k = len(k_list)

    print(f'Got ratio: {2 * k / LEMER_N}')
    print(f'Need ration: {np.pi / 4}')


def show_info(obj, dist):

    create_hist(obj.sequence, HIST_INTERVALS)

    try:
        math_exp, dispersion, square_dev = obj.math_exp, obj.dispersion, obj.square_dev
    except AttributeError:
        math_exp, dispersion, square_dev = calculate_mathematical_characteristics(obj.sequence)
    finally:
        if dist == 'Lemer':
            print(f'{dist} Generator Results:')
        else:
            print(f'{dist} Distribution')
        print(f'Math expectation = {math_exp}')
        print(f'Dispersion = {dispersion}')
        print(f'Mean square deviation = {square_dev}')
        print()
