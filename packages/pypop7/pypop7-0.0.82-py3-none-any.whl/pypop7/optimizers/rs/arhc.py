import numpy as np

from pypop7.optimizers.rs.rhc import RHC


class ARHC(RHC):
    """Annealed Random Hill Climber (ARHC).

    .. note:: The search performance of `ARHC` depends **heavily** on the *temperature* setting of the annealing
       process. However, its proper setting is a **non-trivial** task, since it may vary among different problems
       and even between different optimization stages for the problem at hand. Therefore, it is **highly recommended**
       to first attempt more advanced (e.g. population-based) methods for large-scale black-box optimization.

       Here we include it mainly for *benchmarking* purpose.

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
                * 'sigma'             - initial global step-size (`float`),
                * 'temperature'       - annealing temperature (`float`),
                * 'x'                 - initial (starting) point (`array_like`),

                  * if not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`, when `init_distribution`
                    is `1`. Otherwise, *standard normal* distributed random sampling is used.

                * 'init_distribution' - random sampling distribution for starting-point initialization (`int`,
                  default: `1`). Only when `x` is not set *explicitly*, it will be used.

                  * `1`: *uniform* distributed random sampling only for starting-point initialization,
                  * `0`: *standard normal* distributed random sampling only for starting-point initialization.

    Examples
    --------
    Use the optimizer to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.rs.arhc import ARHC
       >>> problem = {'fitness_function': rosenbrock,  # define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5*numpy.ones((2,)),
       ...            'upper_boundary': 5*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # set optimizer options
       ...            'seed_rng': 2022,
       ...            'x': 3*numpy.ones((2,)),
       ...            'sigma': 0.1,
       ...            'temperature': 1.5}
       >>> arhc = ARHC(problem, options)  # initialize the optimizer class
       >>> results = arhc.optimize()  # run the optimization process
       >>> # return the number of used function evaluations and found best-so-far fitness
       >>> print(f"ARHC: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       ARHC: 5000, 0.0002641143073543329

    For its correctness checking of coding, refer to `this code-based repeatability report
    <https://tinyurl.com/2s3v8z7h>`_ for more details.

    Attributes
    ----------
    init_distribution : `int`
                        random sampling distribution for starting-point initialization.
    sigma             : `float`
                        global step-size (fixed during optimization).
    temperature       : `float`
                        annealing temperature.
    x                 : `array_like`
                        initial (starting) point.

    References
    ----------
    https://probml.github.io/pml-book/book2.html    (See CHAPTER 6.7 Derivative-free optimization)

    Russell, S. and Norvig P., 2021.
    Artificial intelligence: A modern approach (Global Edition).
    Pearson Education.
    http://aima.cs.berkeley.edu/    (See CHAPTER 4: SEARCH IN COMPLEX ENVIRONMENTS)

    Hoos, H.H. and Stützle, T., 2004.
    Stochastic local search: Foundations and applications.
    Elsevier.
    https://www.elsevier.com/books/stochastic-local-search/hoos/978-1-55860-872-6

    https://github.com/pybrain/pybrain/blob/master/pybrain/optimization/hillclimber.py
    """
    def __init__(self, problem, options):
        RHC.__init__(self, problem, options)
        self.temperature = options.get('temperature')  # annealing temperature
        assert self.temperature is not None
        self._parent_x, self._parent_y = np.copy(self.best_so_far_x), np.copy(self.best_so_far_y)

    def iterate(self):  # sampling via mutating the parent individual
        noise = self.rng_optimization.standard_normal(size=(self.ndim_problem,))
        return self._parent_x + self.sigma*noise  # mutation based on Gaussian-noise perturbation

    def _evaluate_fitness(self, x, args=None):
        y = RHC._evaluate_fitness(self, x, args)
        # update parent solution and fitness
        diff = y - self._parent_y
        if (diff < 0) or (self.rng_optimization.random() < np.exp(-diff/self.temperature)):  # annealing
            self._parent_x, self._parent_y = np.copy(x), y
        return y
