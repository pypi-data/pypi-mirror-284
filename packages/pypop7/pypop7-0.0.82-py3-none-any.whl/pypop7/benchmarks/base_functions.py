"""Online documentation:
    https://pypop.readthedocs.io/en/latest/benchmarks.html#base-functions
"""
import numpy as np  # engine for numerical computing


# helper function
def squeeze_and_check(x, size_gt_1=False):
    """Squeeze the input `x` into 1-d `numpy.ndarray`.
        And check whether its number of dimensions == 1. If not, raise a TypeError.
        Optionally, check whether its size > 1. If not, raise a TypeError.
    """
    x = np.squeeze(x)
    if (x.ndim == 0) and (x.size == 1):
        x = np.array([x])
    if x.ndim != 1:
        raise TypeError(f'The number of dimensions should == 1 (not {x.ndim}) after numpy.squeeze(x).')
    if size_gt_1 and not (x.size > 1):
        raise TypeError(f'The size should > 1 (not {x.size}) after numpy.squeeze(x).')
    if x.size == 0:
        raise TypeError(f'the size should != 0.')
    return x


# helper class
class BaseFunction(object):
    """Class for all base functions.
    """
    def __init__(self):
        pass


def sphere(x):
    """**Sphere** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i=1}^{n}x_i^2$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    y = np.sum(np.square(squeeze_and_check(x)))
    return y


class Sphere(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return sphere(x)


def cigar(x):
    """**Cigar** test function.

       .. note:: It's LaTeX formulation is `$x_1^2 + 10^6 \sum_{i = 2}^{n} x_i^2$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.square(squeeze_and_check(x, True))
    y = x[0] + (10.0 ** 6) * np.sum(x[1:])
    return y


class Cigar(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return cigar(x)


def discus(x):
    """**Discus** (also called **Tablet**) test function.

       .. note:: It's LaTeX formulation is `$10^6 x_1^2 + \sum_{i = 2}^{n} x_i^2$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.square(squeeze_and_check(x, True))
    y = (10.0 ** 6) * x[0] + np.sum(x[1:])
    return y


class Discus(BaseFunction):  # also called Tablet
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return discus(x)


def cigar_discus(x):
    """**Cigar-Discus** test function.

       .. note:: It's LaTeX formulation is `$\begin{cases} x_1^2 + 10^4 \sum_{i = 1}^{n}x_i^2 + 10^6 x_n^2, \mbox{if}~n = 2 \\ x_1^2 + 10^4 \sum_{i = 2}^{n}x_i^2 + 10^6 x_n^2, \mbox{otherweise} \end{cases}$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.square(squeeze_and_check(x, True))
    if x.size == 2:
        y = x[0] + (10.0 ** 4) * np.sum(x) + (10.0 ** 6) * x[-1]
    else:
        y = x[0] + (10.0 ** 4) * np.sum(x[1:-1]) + (10.0 ** 6) * x[-1]
    return y


class CigarDiscus(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return cigar_discus(x)


def ellipsoid(x):
    """**Ellipsoid** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{n} 10^{\frac{6(i- 1)}{n - 1}} x_i^2$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.square(squeeze_and_check(x, True))
    y = np.dot(np.power(10.0, 6.0 * np.linspace(0.0, 1.0, x.size)), x)
    return y


class Ellipsoid(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return ellipsoid(x)


def different_powers(x):
    """**Different-Powers** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{ n} \left | x_i \right | ^{\frac{2 + 4(i - 1)}{n - 1}}$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.abs(squeeze_and_check(x, True))
    y = np.sum(np.power(x, 2.0 + 4.0 * np.linspace(0.0, 1.0, x.size)))
    return y


class DifferentPowers(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return different_powers(x)


def schwefel221(x):
    """**Schwefel221** test function.

       .. note:: It's LaTeX formulation is `$\max(\left | x_1 \right |, \cdots, \left | x_n \right |)$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    y = np.max(np.abs(squeeze_and_check(x)))
    return y


class Schwefel221(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return schwefel221(x)


def step(x):
    """**Step** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{n} (\lfloor x_i + 0.5 \rfloor)^2$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    y = np.sum(np.square(np.floor(squeeze_and_check(x) + 0.5)))
    return y


class Step(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return step(x)


def schwefel222(x):
    """**Schwefel222** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{n} \left | x_i \right | + \prod_{i = 1}^{n} \left | x_i \right |$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.abs(squeeze_and_check(x))
    y = np.sum(x) + np.prod(x)
    return y


class Schwefel222(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return schwefel222(x)


def rosenbrock(x):
    """**Rosenbrock** test function.

       .. note:: It's LaTeX formulation is `$100 \sum_{i = 1}^{n -1} (x_i^2 - x_{i + 1})^2 + \sum_{i = 1}^{n - 1} (x_i - 1)^2$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x, True)
    y = 100.0 * np.sum(np.square(x[1:] - np.square(x[:-1]))) + np.sum(np.square(x[:-1] - 1.0))
    return y


class Rosenbrock(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return rosenbrock(x)


def schwefel12(x):
    """**Schwefel12** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{n} (\sum_{j = 1}^{i} x_j)^2$`. Its dimensionality should `> 1`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x, True)
    x = [np.sum(x[:i + 1]) for i in range(x.size)]
    y = np.sum(np.square(x))
    return y


class Schwefel12(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return schwefel12(x)


def exponential(x):
    """**Exponential** test function.

       .. note:: It's LaTeX formulation is `$-e^{-0.5 \sum_{i = 1}^{n} x_i^2}$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x)
    y = -np.exp(-0.5 * np.sum(np.square(x)))
    return y


class Exponential(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return exponential(x)


def griewank(x):
    """**Griewank** test function.

       .. note:: It's LaTeX formulation is `$\frac{1}{4000} \sum_{i = 1}^{n} x_i^2 - \prod_{i = 1}^{n} \cos(\frac{x_i}{i ^ {0.5}}) + 1$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x)
    y = np.sum(np.square(x)) / 4000.0 - np.prod(np.cos(x / np.sqrt(np.arange(1, x.size + 1)))) + 1.0
    return y


class Griewank(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return griewank(x)


def bohachevsky(x):
    """**Bohachevsky** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{ n - 1} (x_i^2 + 2 x_{i + 1}^2 - 0.3\cos(3\pi x_i) - 0.4\cos(4\pi x_{i + 1}) + 0.7)$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x, y = squeeze_and_check(x), 0.0
    for i in range(x.size - 1):
        y += np.square(x[i]) + 2.0 * np.square(x[i + 1]) - 0.3 * np.cos(3.0 * np.pi * x[i]) - \
             0.4 * np.cos(4.0 * np.pi * x[i + 1]) + 0.7
    return y


class Bohachevsky(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return bohachevsky(x)


def ackley(x):
    """**Ackley** test function.

       .. note:: It's LaTeX formulation is `$20 e^{-0.2 \sqrt{\frac{1}{n} \sum_{i = 1}^{n} x_i^2}} - e^{\frac{1}{n} \sum_{i = 1}^{n} \cos(2 \pi x_i)} + 20 + e$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x)
    y = -20.0 * np.exp(-0.2 * np.sqrt(np.sum(np.square(x)) / x.size)) - \
        np.exp(np.sum(np.cos(2.0 * np.pi * x)) / x.size) + 20.0 + np.exp(1)
    return y


class Ackley(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return ackley(x)


def rastrigin(x):
    """**Rastrigin** test function.

       .. note:: It's LaTeX formulation is `$10 n + \sum_{i = 1}^{n} (x_i^2 - 10 \cos(2 \pi x_i))$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x)
    y = 10.0 * x.size + np.sum(np.square(x) - 10.0 * np.cos(2.0 * np.pi * x))
    return y


class Rastrigin(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return rastrigin(x)


def scaled_rastrigin(x):
    """**Scaled-Rastrigin** test function.

       .. note:: It's LaTeX formulation is `$10 n + \sum_{i = 1}^{n} ((10^{\frac{i - 1}{n - 1}} x_i)^2 -10\cos(2\pi 10^{\frac{i - 1}{n - 1}} x_i))$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x, w = squeeze_and_check(x), np.power(10.0, np.linspace(0.0, 1.0, x.size))
    x *= w
    y = 10.0 * x.size + np.sum(np.square(x) - 10.0 * np.cos(2.0 * np.pi * x))
    return y


class ScaledRastrigin(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return scaled_rastrigin(x)


def skew_rastrigin(x):
    """**Skew-Rastrigin** test function.

       .. note:: It's LaTeX formulation is `$10 n + \sum_{i = 1}^{n} (y_i^2 - 10\cos(2\pi y_i))$, with $y_i = \begin{cases} 10 x_i, \mbox{if}~x_i > 0 \\ x_i, \mbox{otherweise} \end{cases}$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = squeeze_and_check(x)
    for i in range(x.size):
        if x[i] > 0.0:
            x[i] *= 10.0
    y = rastrigin(x)
    return y


class SkewRastrigin(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return skew_rastrigin(x)


def levy_montalvo(x):
    """**Levy-Montalvo** test function.

       .. note:: It's LaTeX formulation is `$(10 \sin^2(\pi (1.25 + 0.25x_1)) + (0.25(x_n + 1))^2) \sum_{i = 1}^{n - 1} (0.25(x_i + 1))^2 (1 + 10 \sin^2 (\pi (1.25 + 0.25x_{i + 1})))$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x, y = 1.0 + 0.25 * (squeeze_and_check(x) + 1.0), 0.0
    for i in range(x.size - 1):
        y += np.square(x[i] - 1.0) * (1.0 + 10.0 * np.square(np.sin(np.pi * x[i + 1])))
    y += 10.0 * np.square(np.sin(np.pi * x[0])) + np.square(x[-1] - 1.0)
    return (np.pi / x.size) * y


class LevyMontalvo(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return levy_montalvo(x)


def michalewicz(x):
    """**Michalewicz** test function.

       .. note:: It's LaTeX formulation is `$-\sum_{i = 1}^{n}\sin(x_i)(\sin(\frac{ix_i^2}{\pi}))^{20}$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x, y = squeeze_and_check(x), 0.0
    for i in range(x.size):
        y -= np.sin(x[i]) * np.power(np.sin((i + 1) * np.square(x[i]) / np.pi), 20)
    return y


class Michalewicz(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return michalewicz(x)


def salomon(x):
    """**Salomon** test function.

       .. note:: It's LaTeX formulation is `$1 - \cos(2\pi\sqrt{\sum_{i=1}^{n}x_i^2}) + 0.1 \sqrt{\sum_{i=1}^{n}x_i^2}$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x = np.sqrt(np.sum(np.square(squeeze_and_check(x))))
    return 1.0 - np.cos(2.0 * np.pi * x) + 0.1 * x


class Salomon(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return salomon(x)


def shubert(x):
    """**Shubert** test function.

       .. note:: It's LaTeX formulation is `$\prod_{i=1}^{n} \sum_{j=1}^{5} j\cos((j+1) x_i j)$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x, y = squeeze_and_check(x), 1.0
    for i in range(x.size):
        yy = 0.0
        for j in range(1, 6):
            yy += j * np.cos((j + 1) * x[i] + j)
        y *= yy
    return y


class Shubert(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return shubert(x)


def schaffer(x):
    """**Schaffer** test function.

       .. note:: It's LaTeX formulation is `$\sum_{i = 1}^{n - 1} (x_i^2 + x_{i+1}^2)^{0.25} (\sin^2(50(x_i^2 + x_{i+1}^2)^{0.1}) + 1)$`.

    Parameters
    ----------
    x : ndarray
        input vector.

    Returns
    -------
    y : float
        scalar fitness.
    """
    x, y = squeeze_and_check(x), 0
    for i in range(x.size - 1):
        xx = np.power(x[i], 2) + np.power(x[i + 1], 2)
        y += np.power(xx, 0.25) * (np.power(np.sin(50 * np.power(xx, 0.1)), 2) + 1)
    return y


class Schaffer(BaseFunction):
    def __call__(self, x):
        """

        Parameters
        ----------
        x : ndarray
            input vector.
    
        Returns
        -------
        y : float
            scalar fitness.
        """
        return schaffer(x)
