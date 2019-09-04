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
