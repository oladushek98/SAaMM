import typing
import numpy as np

from collections import namedtuple
from enum import Enum
from matplotlib import pyplot as plt

from constants import LEMER_N, HIST_INTERVALS, LEMER


class ParamErrors(Enum):
    NOT_PRIME = 'should be prime'
    NOT_LESS = 'should be less then 2^N - 1'
    NOT_ENOUGH_ONES = 'should consist more 1s in binary form'


def create_hist(sequence, intervals):
    plt.hist(sequence, intervals)
    plt.show()


def calculate_mathematical_characteristics(sequence) -> typing.NamedTuple:
    array = np.array(sequence)

    m = array.mean()
    d = array.var()
    sig = array.std()

    Characteristics = namedtuple('Characteristics', ['math_exp', 'dispersion', 'square_dev'])

    return Characteristics(m, d, sig)


def checks_on_circumstantial_evidence(sequence):
    pairs_list = [(sequence[i], sequence[i + 1]) for i in range(0, len(sequence), 2)]
    k_list = list(filter(lambda pair: pow(pair[0], 2) + pow(pair[1], 2) < 1, pairs_list))
    k = len(k_list)

    print(f'Got ratio: {2 * k / LEMER_N}')
    print(f'Need ration: {np.pi / 4}')


def show_info(obj, dist):

    create_hist(obj.sequence, HIST_INTERVALS)

    math_exp, dispersion, square_dev = calculate_mathematical_characteristics(obj.sequence)

    if dist == LEMER:
        print(f'{dist} Generator Results:')
    else:
        print(f'{dist} Distribution:')
    print(f'Math expectation = {math_exp}')
    print(f'Dispersion = {dispersion}')
    print(f'Mean square deviation = {square_dev}')
    print()


def calculate_period(sequence):
    xv = sequence[-1]
    values = []
    for i in range(len(sequence)):
        if sequence[i] == xv:
            if len(values) >= 2:
                break
            values.append(i)
    try:
        p = values[1] - values[0]
        print(f'Period = {p}')
    except IndexError:
        print('No period here!')

    try:
        for i in range(len(sequence)):
            if sequence[i] == sequence[i + p]:
                print(f'Aperiodic length = {i + p}')
                break
    except (IndexError, UnboundLocalError) as e:
        print('No aperiodic length')
