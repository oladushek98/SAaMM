import typing
import numpy as np

from collections import namedtuple
from enum import Enum
from matplotlib import pyplot as plt


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
