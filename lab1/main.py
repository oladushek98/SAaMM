from constants import HIST_INTERVALS
from lemer import LemerGenerator
from utils import create_hist


if __name__ == '__main__':

    print('Enter A:')
    a = int(input())
    print('Enter R0:')
    r0 = int(input())
    print('Enter M:')
    m = int(input())

    res = LemerGenerator(a, r0, m)
    sequence = res.sequence
    create_hist(sequence, HIST_INTERVALS)
