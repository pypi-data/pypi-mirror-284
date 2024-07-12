import numpy as np  # engine for numerical computing

from pypop7.optimizers.de.de import DE  # abstract class of all differential evolution (DE)
from pypop7.optimizers.de.cde import CDE


class CODE(CDE):
    """COmposite Differential Evolution (CODE).

    Parameters
    ----------
    problem : `dict`
              problem arguments with the following common settings (`keys`):
                * 'fitness_function' - objective function to be **minimized** (`func`),
                * 'ndim_problem'     - number of dimensionality (`int`),
                * 'upper_boundary'   - upper boundary of search range (`array_like`),
                * 'lower_boundary'   - lower boundary of search range (`array_like`).
    options : `dict`
              optimizer options with the following common settings (`keys`):
                * 'max_function_evaluations' - maximum of function evaluations (`int`, default: `np.inf`),
                * 'max_runtime'              - maximal runtime to be allowed (`float`, default: `np.inf`),
                * 'seed_rng'                 - seed for random number generation needed to be *explicitly* set (`int`);
              and with the following particular setting (`key`):
                * 'n_individuals' - population size (`int`, default: `100`).

    Examples
    --------
    Use the optimizer to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.de.code import CODE
       >>> problem = {'fitness_function': rosenbrock,  # define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5*numpy.ones((2,)),
       ...            'upper_boundary': 5*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # set optimizer options
       ...            'seed_rng': 0}
       >>> code = CODE(problem, options)  # initialize the optimizer class
       >>> results = code.optimize()  # run the optimization process
       >>> # return the number of function evaluations and best-so-far fitness
       >>> print(f"CODE: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       CODE: 5000, 0.01052980838183792

    Attributes
    ----------
    n_individuals : `int`
                    number of offspring, aka offspring population size.

    References
    ----------
    Wang, Y., Cai, Z., and Zhang, Q. 2011.
    Differential evolution with composite trial vector generation strategies and control parameters.
    IEEE Transactions on Evolutionary Computation, 15(1), pp.55–66.
    https://doi.org/10.1109/TEVC.2010.2087271
    """
    def __init__(self, problem, options):
        CDE.__init__(self, problem, options)
        self.is_bound = options.get('is_bound', False)
        self._pool = [[1.0, 0.1], [1.0, 0.9], [0.8, 0.2]]  # a pool of two control parameters (f, cr)

    def bound(self, x=None):
        if not self.is_bound:
            return x
        for k in range(self.n_individuals):
            idx = np.array(x[k] < self.lower_boundary)
            if idx.any():
                x[k][idx] = np.minimum(self.upper_boundary, 2.0*self.lower_boundary - x[k])[idx]
            idx = np.array(x[k] > self.upper_boundary)
            if idx.any():
                x[k][idx] = np.maximum(self.lower_boundary, 2.0*self.upper_boundary - x[k])[idx]
        return x

    def mutate(self, x=None, v=None):
        x1 = np.empty((self.n_individuals, self.ndim_problem))
        x2 = np.empty((self.n_individuals, self.ndim_problem))
        x3 = np.empty((self.n_individuals, self.ndim_problem))
        # randomly select from the parameter candidate pool
        base = np.arange(self.n_individuals)
        f_p = self.rng_optimization.choice(self._pool, (self.n_individuals, 3))
        for k in range(self.n_individuals):
            base_k = [i for i in base if i != k]
            r = self.rng_optimization.choice(base_k, (3,), False)
            x1[k] = x[r[0]] + f_p[k, 0, 0]*(x[r[1]] - x[r[2]])  # rand/1/bin
            r = self.rng_optimization.choice(base_k, (5,), False)
            x2[k] = (x[r[0]] + self.rng_optimization.random()*(x[r[1]] - x[r[2]]) +
                     f_p[k, 1, 0]*(x[r[3]] - x[r[4]]))  # rand/2/bin
            r = self.rng_optimization.choice(base_k, (3,), False)
            x3[k] = (x[k] + self.rng_optimization.random()*(x[r[0]] - x[k]) +
                     f_p[k, 2, 0]*(x[r[1]] - x[r[2]]))  # current-to-rand/1
        return x1, x2, x3, f_p

    def crossover(self, x_mu=None, x=None, p_cr=None):
        x_cr = np.copy(x)
        for k in range(self.n_individuals):
            j_r = self.rng_optimization.integers(self.ndim_problem)
            for i in range(self.ndim_problem):
                if (i == j_r) or (self.rng_optimization.random() < p_cr[k]):
                    x_cr[k, i] = x_mu[k, i]
        return x_cr

    def select(self, x=None, y=None, x_cr=None, args=None):
        yyy = []  # to store all fitnesses
        for k in range(self.n_individuals):
            if self._check_terminations():
                break
            yy = self._evaluate_fitness(x_cr[k], args)
            yyy.append(yy)
            if yy < y[k]:
                x[k], y[k] = x_cr[k], yy
        return x, y, yyy

    def iterate(self, x=None, y=None, v=None, args=None):
        yy = []  # to store all fitnesses
        x1, x2, x3, f_p = self.mutate(x)
        x1 = self.bound(self.crossover(x1, x, f_p[:, 0, 1]))
        x2 = self.bound(self.crossover(x2, x, f_p[:, 1, 1]))
        x3 = self.bound(x3)
        x, y, yy_1 = self.select(x, y, x1, args)
        x, y, yy_2 = self.select(x, y, x2, args)
        x, y, yy_3 = self.select(x, y, x3, args)
        yy.extend(yy_1)
        yy.extend(yy_2)
        yy.extend(yy_3)
        self._n_generations += 1
        return x, y, yy

    def optimize(self, fitness_function=None, args=None):
        fitness = DE.optimize(self, fitness_function)
        x, y, _ = self.initialize(args)
        yy = y
        while not self._check_terminations():
            self._print_verbose_info(fitness, yy)
            x, y, yy = self.iterate(x, y, None, args)
        return self._collect(fitness, yy)
