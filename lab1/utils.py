from matplotlib import pyplot as plt


def create_hist(sequence, intervals):
    plt.hist(sequence, intervals)
    plt.show()
