import numpy as np  # engine for numerical computing

from pypop7.optimizers.core.optimizer import Optimizer  # abstract class for all black-box optimizers (BBO)
from pypop7.optimizers.sa.sa import SA  # abstract class for all simulated annealing (SA) subclasses


class ESA(SA):
    """Enhanced Simulated Annealing (ESA).

    .. note:: `ESA` adopts a **random decomposition** strategy to alleviate the *curse of dimensionality* for
       large-scale black-box optimization. Note that it shares some similaries (i.e., axis-parallel decomposition)
       to the *Cooperative Coevolution* framework, which uses population-based sampling (rather than individual-based
       sampling of `ESA`) for each subproblem (corresponding to a search subspace).

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
                * 'p'  - subspace dimension (`int`, default: `int(np.ceil(problem['ndim_problem']/3))`),
                * 'n1' - factor to control temperature stage w.r.t. accepted moves (`int`, default: `12`),
                * 'n2' - factor to control temperature stage w.r.t. attempted moves (`int`, default: `100`).

    Examples
    --------
    Use the black-box optimizer `ESA` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy  # engine for numerical computing
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.sa.esa import ESA
       >>> problem = {'fitness_function': rosenbrock,  # define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5*numpy.ones((2,)),
       ...            'upper_boundary': 5*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # set optimizer options
       ...            'seed_rng': 2022,
       ...            'x': 3*numpy.ones((2,))}
       >>> esa = ESA(problem, options)  # initialize the optimizer class
       >>> results = esa.optimize()  # run the optimization process
       >>> # return the number of function evaluations and best-so-far fitness
       >>> print(f"ESA: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       ESA: 5000, 6.481109148014023

    For its correctness checking of coding, refer to `this code-based repeatability report
    <https://tinyurl.com/3e2k39z2>`_ for details.

    For its `pytest <https://docs.pytest.org/>`_ based testing, please refer to `this Python code
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/sa/test_esa.py>`_.

    Attributes
    ----------
    n1 : `int`
         factor to control temperature stage w.r.t. accepted moves.
    n2 : `int`
         factor to control temperature stage w.r.t. attempted moves.
    p  : `int`
         subspace dimension.

    References
    ----------
    Siarry, P., Berthiau, G., Durdin, F. and Haussy, J., 1997.
    `Enhanced simulated annealing for globally minimizing functions of many-continuous variables.
    <https://dl.acm.org/doi/abs/10.1145/264029.264043>`_
    ACM Transactions on Mathematical Software, 23(2), pp.209-228.
    """
    def __init__(self, problem, options):
        SA.__init__(self, problem, options)
        self.n1 = options.get('n1', 12)  # factor to control temperature stage w.r.t. accepted moves
        assert self.n1 > 0
        self.n2 = options.get('n2', 100)  # factor to control temperature stage w.r.t. attempted moves
        assert self.n2 > 0
        self.p = options.get('p', int(np.ceil(self.ndim_problem/3)))  # number of subspaces
        assert self.p > 0
        self.verbose = options.get('verbose', 10)
        # set parameters at current temperature stage
        self._elowst = None
        self._avgyst = 0
        self._mvokst = 0  # number of accepted moves
        self._mokst = np.zeros((self.ndim_problem,))  # numbers of accepted moves for each dimension
        self._nmvst = 0  # number of attempted moves
        self._mtotst = np.zeros((self.ndim_problem,))  # numbers of attempted moves for each dimension
        self._v = None  # step vector

    def initialize(self, args=None):
        self._v = 0.25*(self.upper_boundary - self.lower_boundary)
        if self.x is None:  # starting point
            x = self.rng_initialization.uniform(self.initial_lower_boundary, self.initial_upper_boundary)
        else:
            x = np.copy(self.x)
        assert len(x) == self.ndim_problem
        y = self._evaluate_fitness(x, args)
        self.parent_x, self.parent_y = np.copy(x), np.copy(y)
        fitness = [y]
        if self.temperature is None:
            for _ in range(49):
                if self._check_terminations():
                    break
                xx = self.rng_initialization.uniform(self.lower_boundary, self.upper_boundary)
                yy = self._evaluate_fitness(xx, args)
                if self.saving_fitness:
                    fitness.append(yy)
            self.temperature = -np.mean(fitness)/np.log(0.5)
        return fitness

    def iterate(self, p=None, args=None):
        fitness = []
        for k in p:  # without over-selecting
            if self._check_terminations():
                return fitness
            x, sign = np.copy(self.parent_x), self.rng_optimization.choice([-1, 1])
            xx = x[k] + sign*self._v[k]
            if (xx < self.lower_boundary[k]) or (xx > self.upper_boundary[k]):
                xx = x[k] - sign*self._v[k]
            x[k] = np.maximum(np.minimum(xx, self.upper_boundary[k]), self.lower_boundary[k])
            y = self._evaluate_fitness(x, args)
            if self.saving_fitness:
                fitness.append(y)
            self._avgyst += y
            self._mtotst[k] += 1
            self._nmvst += 1
            diff = self.parent_y - y
            if (diff >= 0) or (self.rng_optimization.random() < np.exp(diff/self.temperature)):
                self.parent_x, self.parent_y = np.copy(x), np.copy(y)
                self._mokst[k] += 1
                self._mvokst += 1
            if (diff >= 0) and (y < self._elowst):
                self._elowst = y
        return fitness

    def _adjust_step_vector(self):
        for k in range(self.ndim_problem):
            if self._mtotst[k] > 0:
                rok = self._mokst[k]/self._mtotst[k]
                if rok > 0.2:
                    self._v[k] *= 2.0
                elif rok < 0.05:
                    self._v[k] *= 0.5
                self._v[k] = np.minimum(self._v[k], self.upper_boundary[k] - self.lower_boundary[k])

    def _reset_parameters(self):
        self._mvokst = 0
        self._mokst = np.zeros((self.ndim_problem,))
        self._nmvst = 0
        self._mtotst = np.zeros((self.ndim_problem,))
        self._elowst = self.parent_y
        self._avgyst = 0

    def optimize(self, fitness_function=None, args=None):  # for all iterations (generations)
        fitness = Optimizer.optimize(self, fitness_function)
        y = self.initialize(args)
        self._elowst = y[0]
        self._print_verbose_info(fitness, y)
        while not self._check_terminations():
            p, n_p = self.rng_optimization.permutation(self.ndim_problem), 0
            while (self._mvokst < self.n1*self.ndim_problem) and (self._nmvst < self.n2*self.ndim_problem):
                if self._check_terminations():
                    break
                n_p += 1
                new_fitness = self.iterate(p[(self.p*(n_p - 1)):(self.p*n_p)], args)
                self._n_generations += 1
                if len(new_fitness) > 0:
                    self._print_verbose_info(fitness, new_fitness)
                if self.p*n_p >= self.ndim_problem:  # to re-partition
                    p, n_p = self.rng_optimization.permutation(self.ndim_problem), 0
            self._avgyst /= self._nmvst
            self.temperature *= np.maximum(np.minimum(self._elowst/self._avgyst, 0.9), 0.1)
            self._adjust_step_vector()
            self._reset_parameters()
        return self._collect(fitness)
