import numpy as np  # engine for numerical computing

from pypop7.optimizers.es.es import ES  # abstract class of all Evolution Strategies (ES) classes


class LMMAES(ES):
    """Limited-Memory Matrix Adaptation Evolution Strategy (LMMAES).

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
              and with the following particular settings (`keys`):
                * 'sigma'             - initial global step-size, aka mutation strength (`float`),
                * 'mean'              - initial (starting) point, aka mean of Gaussian search distribution
                  (`array_like`),

                  * if not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`).

                * 'n_evolution_paths' - number of evolution paths (`int`, default:
                  `4 + int(3*np.log(problem['ndim_problem']))`),
                * 'n_individuals'     - number of offspring, aka offspring population size (`int`, default:
                  `4 + int(3*np.log(problem['ndim_problem']))`),
                * 'n_parents'         - number of parents, aka parental population size (`int`, default:
                  `int(options['n_individuals']/2)`),
                * 'c_s'               - learning rate of evolution path update (`float`, default:
                  `2.0*options['n_individuals']/problem['ndim_problem']`).

    Examples
    --------
    Use the black-box optimizer `LMMAES` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy  # engine for numerical computing
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.es.lmmaes import LMMAES
       >>> problem = {'fitness_function': rosenbrock,  # to define problem arguments
       ...            'ndim_problem': 200,
       ...            'lower_boundary': -5.0*numpy.ones((200,)),
       ...            'upper_boundary': 5.0*numpy.ones((200,))}
       >>> options = {'max_function_evaluations': 500000,  # to set optimizer options
       ...            'seed_rng': 0,
       ...            'mean': 3.0*numpy.ones((200,)),
       ...            'sigma': 3.0}  # global step-size may need to be tuned for optimality
       >>> lmmaes = LMMAES(problem, options)  # to initialize the optimizer class
       >>> results = lmmaes.optimize()  # to run the optimization/evolution process
       >>> print(f"LMMAES: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       LMMAES: 500000, 78.4967

    For its correctness checking of Python coding, please refer to `this code-based repeatability report
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/es/_repeat_lmmaes.py>`_
    for all details. For *pytest*-based automatic testing, please see `test_lmmaes.py
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/es/test_lmmaes.py>`_.

    Attributes
    ----------
    c_s               : `float`
                        learning rate of evolution-path update (should `> 0.0`).
    mean              : `array_like`
                        initial (starting) point, aka mean of Gaussian search distribution.
    n_evolution_paths : `int`
                        number of evolution paths (should `> 1`).
    n_individuals     : `int`
                        number of offspring, aka offspring population size.
    n_parents         : `int`
                        number of parents, aka parental population size.
    sigma             : `float`
                        final global step-size, aka mutation strength.

    References
    ----------
    Loshchilov, I., Glasmachers, T. and Beyer, H.G., 2019.
    `Large scale black-box optimization by limited-memory matrix adaptation.
    <https://ieeexplore.ieee.org/abstract/document/8410043>`_
    IEEE Transactions on Evolutionary Computation, 23(2), pp.353-358.

    Please refer to the *official* Python version from Prof. Glasmachers:
    https://www.ini.rub.de/upload/editor/file/1604950981_dc3a4459a4160b48d51e/lmmaes.py
    """
    def __init__(self, problem, options):
        ES.__init__(self, problem, options)
        n_evolution_paths = 4 + int(3*np.log(self.ndim_problem))
        self.n_evolution_paths = options.get('n_evolution_paths', n_evolution_paths)
        self.c_s, self._c_c = None, None
        self._s_1, self._s_2 = None, None
        self._c_d = 1.0/(self.ndim_problem*np.power(1.5, np.arange(self.n_evolution_paths)))

    def initialize(self, is_restart=False):
        self.c_s = self.options.get('c_s', 2.0*self.n_individuals/self.ndim_problem)
        _s_1 = 1.0 - self.c_s
        if _s_1 < 0.0:  # undefined in the original paper
            _s_1 = 0.5
        self._s_1 = _s_1
        _s_2 = self._mu_eff*self.c_s*(2.0 - self.c_s)
        if _s_2 < 0.0:  # undefined in the original paper
            _s_2 = np.square(0.5)
        self._s_2 = np.sqrt(_s_2)
        self._c_c = self.n_individuals/(self.ndim_problem*np.power(4.0, np.arange(self.n_evolution_paths)))
        z = np.empty((self.n_individuals, self.ndim_problem))  # Gaussian noise for mutation
        d = np.empty((self.n_individuals, self.ndim_problem))  # search directions
        mean = self._initialize_mean(is_restart)  # mean of Gaussian search distribution
        s = np.zeros((self.ndim_problem,))  # evolution path
        tm = np.zeros((self.n_evolution_paths, self.ndim_problem))  # transformation matrix (M)
        y = np.empty((self.n_individuals,))  # fitness (no evaluation)
        self._list_initial_mean.append(np.copy(mean))
        return z, d, mean, s, tm, y

    def iterate(self, z=None, d=None, mean=None, tm=None, y=None, args=None):
        for k in range(self.n_individuals):
            if self._check_terminations():
                return z, d, y
            z[k] = self.rng_optimization.standard_normal((self.ndim_problem,))
            d[k] = z[k]
            for j in range(np.minimum(self._n_generations, self.n_evolution_paths)):
                d[k] = (1.0 - self._c_d[j])*d[k] + self._c_d[j]*tm[j]*np.dot(tm[j], d[k])
            y[k] = self._evaluate_fitness(mean + self.sigma*d[k], args)
        return z, d, y

    def _update_distribution(self, z=None, d=None, mean=None, s=None, tm=None, y=None):
        order = np.argsort(y)[:self.n_parents]
        d_w = np.dot(self._w[:self.n_parents], d[order])
        z_w = np.dot(self._w[:self.n_parents], z[order])
        # update distribution mean
        mean += self.sigma*d_w
        # update evolution path (p_c, s) and low-rank transformation matrix (tm)
        s = self._s_1*s + self._s_2*z_w
        for k in range(self.n_evolution_paths):  # rank-m
            _tm_1 = 1.0 - self._c_c[k]
            if _tm_1 < 0.0:  # undefined in the original paper
                _tm_1 = 0.5
            _tm_2 = self._mu_eff*self._c_c[k]*(2.0 - self._c_c[k])
            if _tm_2 < 0.0:  # undefined in the original paper
                _tm_2 = np.square(0.5)
            tm[k] = _tm_1*tm[k] + np.sqrt(_tm_2)*z_w
        # update global step-size
        self.sigma *= np.exp(self.c_s/2.0*(np.sum(np.square(s))/self.ndim_problem - 1.0))
        return mean, s, tm

    def restart_reinitialize(self, z=None, d=None, mean=None, s=None, tm=None, y=None):
        if self.is_restart and ES.restart_reinitialize(self, y):
            z, d, mean, s, tm, y = self.initialize(True)
        return z, d, mean, s, tm, y

    def optimize(self, fitness_function=None, args=None):  # for all generations (iterations)
        fitness = ES.optimize(self, fitness_function)
        z, d, mean, s, tm, y = self.initialize()
        while not self.termination_signal:
            # sample and evaluate offspring population
            z, d, y = self.iterate(z, d, mean, tm, y, args)
            if self._check_terminations():
                break
            self._print_verbose_info(fitness, y)
            self._n_generations += 1
            mean, s, tm = self._update_distribution(z, d, mean, s, tm, y)
            z, d, mean, s, tm, y = self.restart_reinitialize(z, d, mean, s, tm, y)
        results = self._collect(fitness, y, mean)
        results['s'] = s
        results['tm'] = tm
        return results
