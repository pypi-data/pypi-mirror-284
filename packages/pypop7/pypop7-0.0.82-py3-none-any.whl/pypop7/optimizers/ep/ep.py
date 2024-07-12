import numpy as np  # engine for numerical computing

from pypop7.optimizers.core.optimizer import Optimizer  # abstract class of all black-box optimizers (BBO)


class EP(Optimizer):
    """Evolutionary Programming (EP).

    This is the **abstract** class for all `EP` classes. Please use any of its instantiated subclasses to
    optimize the black-box problem at hand.

    .. note:: `EP` is one of three classical families of evolutionary algorithms (EAs), proposed originally by Lawrence
       J. Fogel (both the recipient of IEEE Evolutionary Computation Pioneer Award 1998 and IEEE Frank Rosenblatt Award
       2006). When used for continuous BBO, most of modern `EP` versions share similarities (e.g., self-adaptation)
       with `ES <https://pypop.readthedocs.io/en/latest/es/es.html>`_, another of three representative EAs.

       For an introduction to pioneer contributions of Laurence J. Fogel to evolutionary computation, please refer to
       `[Evolutionary Intelligence, 2008] <https://link.springer.com/article/10.1007/s12065-007-0006-0>`_ and
       `[ECJ 2007] <https://direct.mit.edu/evco/article-abstract/15/2/iii/1264/In-Memoriam-Laurence-J-Fogel>`_. For
       some interesting applications of `EP`, please refer to e.g., `[Fogel et al., 2004, PIEEE]
       <https://ieeexplore.ieee.org/abstract/document/1360168>`_, just to name a few.

    Parameters
    ----------
    problem : dict
              problem arguments with the following common settings (`keys`):
                * 'fitness_function' - objective function to be **minimized** (`func`),
                * 'ndim_problem'     - number of dimensionality (`int`),
                * 'upper_boundary'   - upper boundary of search range (`array_like`),
                * 'lower_boundary'   - lower boundary of search range (`array_like`).
    options : dict
              optimizer options with the following common settings (`keys`):
                * 'max_function_evaluations' - maximum of function evaluations (`int`, default: `np.inf`),
                * 'max_runtime'              - maximal runtime to be allowed (`float`, default: `np.inf`),
                * 'seed_rng'                 - seed for random number generation needed to be *explicitly* set (`int`);
              and with the following particular settings (`keys`):
                * 'sigma'         - initial global step-size, aka mutation strength (`float`),
                * 'n_individuals' - number of offspring, aka offspring population size (`int`, default: `100`).

    Attributes
    ----------
    n_individuals : `int`
                    number of offspring, aka offspring population size.
    sigma         : `float`
                    initial global step-size, aka mutation strength.

    Methods
    -------

    References
    ----------
    Lee, C.Y. and Yao, X., 2004.
    Evolutionary programming using mutations based on the Lévy probability distribution.
    IEEE Transactions on Evolutionary Computation, 8(1), pp.1-13.
    https://ieeexplore.ieee.org/document/1266370

    Yao, X., Liu, Y. and Lin, G., 1999.
    Evolutionary programming made faster.
    IEEE Transactions on Evolutionary Computation, 3(2), pp.82-102.
    https://ieeexplore.ieee.org/abstract/document/771163

    Fogel, D.B., 1999.
    An overview of evolutionary programming.
    In Evolutionary Algorithms (pp. 89-109). Springer, New York, NY.
    https://link.springer.com/chapter/10.1007/978-1-4612-1542-4_5

    Fogel, D.B. and Fogel, L.J., 1995, September.
    An introduction to evolutionary programming.
    In European Conference on Artificial Evolution (pp. 21-33). Springer, Berlin, Heidelberg.
    https://link.springer.com/chapter/10.1007/3-540-61108-8_28

    Fogel, D.B., 1994.
    An introduction to simulated evolutionary optimization.
    IEEE Transactions on Neural Networks, 5(1), pp.3-14.
    https://ieeexplore.ieee.org/abstract/document/265956

    Fogel, D.B., 1994.
    Evolutionary programming: An introduction and some current directions.
    Statistics and Computing, 4(2), pp.113-129.
    https://link.springer.com/article/10.1007/BF00175356

    Bäck, T. and Schwefel, H.P., 1993.
    An overview of evolutionary algorithms for parameter optimization.
    Evolutionary Computation, 1(1), pp.1-23.
    https://direct.mit.edu/evco/article-abstract/1/1/1/1092/An-Overview-of-Evolutionary-Algorithms-for
    """
    def __init__(self, problem, options):
        Optimizer.__init__(self, problem, options)
        if self.n_individuals is None:
            self.n_individuals = 100  # number of offspring, aka offspring population size
        self.sigma = options.get('sigma')  # initial global step-size, aka mutation strength
        self._n_generations = 0  # number of generations
        self._printed_evaluations = 0  # only for printing

    def initialize(self):
        raise NotImplementedError

    def iterate(self):
        raise NotImplementedError

    def _print_verbose_info(self, fitness, y, is_print=False):
        if y is not None and self.saving_fitness:
            if not np.isscalar(y):
                fitness.extend(y)
            else:
                fitness.append(y)
        if self.verbose:
            is_verbose = self._printed_evaluations != self.n_function_evaluations  # to avoid repeated printing
            is_verbose_1 = (not self._n_generations % self.verbose) and is_verbose
            is_verbose_2 = self.termination_signal > 0 and is_verbose
            is_verbose_3 = is_print and is_verbose
            if is_verbose_1 or is_verbose_2 or is_verbose_3:
                info = '  * Generation {:d}: best_so_far_y {:7.5e}, min(y) {:7.5e} & Evaluations {:d}'
                print(info.format(self._n_generations, self.best_so_far_y, np.min(y), self.n_function_evaluations))
                self._printed_evaluations = self.n_function_evaluations

    def _collect(self, fitness=None, y=None):
        self._print_verbose_info(fitness, y)
        results = Optimizer._collect(self, fitness)
        results['_n_generations'] = self._n_generations
        return results
