import numpy as np

from pypop7.optimizers.ds.ds import DS


class GPS(DS):
    """Generalized Pattern Search (GPS).

    .. note:: `"To converge to a local minimum, certain conditions must be met. The set of directions must
        be a positive spanning set, which means that we can construct any point using a nonnegative
        linear combination of the directions. A positive spanning set ensures that at least one of the
        directions is a descent direction from a location with a nonzero gradient."---[Kochenderfer&Wheeler, 2019]
        <https://algorithmsbook.com/optimization/files/chapter-7.pdf>`_

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
                * 'sigma' - initial global step-size (`float`, default: `1.0`),
                * 'x'     - initial (starting) point (`array_like`),

                  * if not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`.

                * 'gamma' - decreasing factor of step-size (`float`, default: `0.5`).

    Examples
    --------
    Use the optimizer to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.ds.gps import GPS
       >>> problem = {'fitness_function': rosenbrock,  # define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5*numpy.ones((2,)),
       ...            'upper_boundary': 5*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # set optimizer options
       ...            'seed_rng': 2022,
       ...            'x': 3*numpy.ones((2,)),
       ...            'sigma': 0.1,
       ...            'verbose_frequency': 500}
       >>> gps = GPS(problem, options)  # initialize the optimizer class
       >>> results = gps.optimize()  # run the optimization process
       >>> # return the number of function evaluations and best-so-far fitness
       >>> print(f"GPS: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       GPS: 5000, 0.6182686369768672

    Attributes
    ----------
    gamma : `float`
            decreasing factor of step-size.
    sigma : `float`
            final global step-size (changed during optimization).
    x     : `array_like`
            initial (starting) point.

    References
    ----------
    Kochenderfer, M.J. and Wheeler, T.A., 2019.
    Algorithms for optimization.
    MIT Press.
    https://algorithmsbook.com/optimization/files/chapter-7.pdf
    (See Algorithm 7.6 (Page 106) for details.)

    Regis, R.G., 2016.
    On the properties of positive spanning sets and positive bases.
    Optimization and Engineering, 17(1), pp.229-262.
    https://link.springer.com/article/10.1007/s11081-015-9286-x

    Torczon, V., 1997.
    On the convergence of pattern search algorithms.
    SIAM Journal on Optimization, 7(1), pp.1-25.
    https://epubs.siam.org/doi/abs/10.1137/S1052623493250780
    """
    def __init__(self, problem, options):
        DS.__init__(self, problem, options)
        self.gamma = options.get('gamma', 0.5)  # decreasing factor of step-size (γ)

    def initialize(self, args=None, is_restart=False):
        x = self._initialize_x(is_restart)  # initial point
        y = self._evaluate_fitness(x, args)  # fitness
        # set random directions
        d = self.rng_initialization.standard_normal(size=(self.ndim_problem + 1, self.ndim_problem))
        i_d = [i for i in range(d.shape[0])]  # index of used directions
        return x, y, d, i_d

    def iterate(self, x=None, d=None, i_d=None, args=None):
        improved, best_so_far_y, fitness = False, self.best_so_far_y, []
        for i in range(d.shape[0]):
            if self._check_terminations():
                return i_d, fitness
            x = self.best_so_far_x + self.sigma*d[i_d[i]]  # opportunistic
            y = self._evaluate_fitness(x, args)
            fitness.append(y)
            if y < best_so_far_y:
                improved = True
                i_d = [i_d[i]] + i_d[:i] + i_d[(i + 1):]  # dynamic ordering
                break
        if not improved:
            self.sigma *= self.gamma  # alpha
        return i_d, fitness

    def restart_reinitialize(self, args=None, x=None, y=None, d=None, i_d=None, fitness=None):
        self._fitness_list.append(self.best_so_far_y)
        is_restart_1, is_restart_2 = self.sigma < self.sigma_threshold, False
        if len(self._fitness_list) >= self.stagnation:
            is_restart_2 = (self._fitness_list[-self.stagnation] - self._fitness_list[-1]) < self.fitness_diff
        is_restart = bool(is_restart_1) or bool(is_restart_2)
        if is_restart:
            self._print_verbose_info(fitness, y)
            self.sigma = np.copy(self._sigma_bak)
            x, y, d, i_d = self.initialize(args, is_restart)
            self._fitness_list = [self.best_so_far_y]
            self._n_generations = 0
            self._n_restart += 1
            if self.verbose:
                print(' ....... *** restart *** .......')
        return x, y, d, i_d

    def optimize(self, fitness_function=None, args=None):
        fitness = DS.optimize(self, fitness_function)
        x, y, d, i_d = self.initialize(args)
        while True:
            self._print_verbose_info(fitness, y)
            i_d, y = self.iterate(x, d, i_d, args)
            if self._check_terminations():
                break
            self._n_generations += 1
            if self.is_restart:
                x, y, d, i_d = self.restart_reinitialize(args, x, y, d, i_d, fitness)
        return self._collect(fitness, y)
