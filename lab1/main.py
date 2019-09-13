from constants import (
    A, R0, M, LEMER_N, LEMER,
    UNIFORM_A, UNIFORM_B, UNIFORM,
    GAUSSIAN_N, GAUSSIAN_MEAN, GAUSSIAN_STD, GAUSS,
    EXPONENTIAL_LAMB, EXPONENTIAL,
    GAMMA_TETT, GAMMA_LAMB, GAMMA,
    TRIANGLE_A, TRIANGLE_B, TRIANGULAR,
    SIMPSON_A, SIMPSON_B, SIMPSON,
)
from distributions import (
    UniformDistribution, SequenceMixin, ExponentialDistribution, GammaDistribution,
    TriangularDistribution, SimpsonDistribution, GaussDistribution
)
from lemer import LemerGenerator
from utils import (checks_on_circumstantial_evidence, show_info, calculate_period)

if __name__ == '__main__':

    # Lemer Generator

    lemer = LemerGenerator(A, R0, M, LEMER_N)
    show_info(lemer, LEMER)

    checks_on_circumstantial_evidence(lemer.sequence)
    print()
    calculate_period(lemer.sequence)
    print()

    temp = SequenceMixin(lemer.sequence)

    # in each distribution below params are set for the best visualisation of distribution histograms
    # lab with this values was successfully passed
    # all params were set by the educator to show right work of the algorithms
    # math characteristics are calculated by numpy functions based on real got values
    # theoretical characteristics don't satisfy the educator

    # Uniform Distribution
    uniform = UniformDistribution(UNIFORM_A, UNIFORM_B)
    show_info(uniform, UNIFORM)

    # Gaussian Distribution
    gauss = GaussDistribution(GAUSSIAN_N, GAUSSIAN_MEAN, GAUSSIAN_STD)
    show_info(gauss, GAUSS)

    # Exponential Distribution
    exp = ExponentialDistribution(EXPONENTIAL_LAMB)
    show_info(exp, EXPONENTIAL)

    # before working with this distribution put 1000-5000 as a 3rd param for a quick resul
    # length here 1000 by default
    # Gamma Distribution
    gamma = GammaDistribution(GAMMA_TETT, GAMMA_LAMB)
    show_info(gamma, GAMMA)

    # before working with this distribution put LEMER_N to a high value if start params are large
    # or to a low value in the other case
    # Triangular Distribution
    triangle = TriangularDistribution(TRIANGLE_A, TRIANGLE_B)
    show_info(triangle, TRIANGULAR)

    # Simpson Distribution
    simpson = SimpsonDistribution(SIMPSON_A, SIMPSON_B)
    show_info(simpson, SIMPSON)
