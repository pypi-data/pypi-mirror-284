import numpy as np  # engine for numerical computing

from pypop7.optimizers.es.es import ES  # abstract class of all Evolution Strategies (ES) classes


class LMCMAES(ES):
    """Limited-Memory Covariance Matrix Adaptation Evolution Strategy (LMCMAES).

    .. note:: For perhaps better performance, please first use its lateset version called `LMCMA
       <https://pypop.readthedocs.io/en/latest/es/lmcma.html>`_. Here we include it mainly for a
       *benchmarking* purpose.

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
                * 'sigma'         - initial global step-size, aka mutation strength (`float`),
                * 'mean'          - initial (starting) point, aka mean of Gaussian search distribution (`array_like`),

                  * if not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`.

                * 'm'             - number of direction vectors (`int`, default:
                  `4 + int(3*np.log(problem['ndim_problem']))`),
                * 'n_steps'       - target number of generations between vectors (`int`, default: `options['m']`),
                * 'c_c'           - learning rate for evolution path update (`float`, default: `1.0/options['m']`).
                * 'c_1'           - learning rate for covariance matrix adaptation (`float`, default:
                  `1.0/(10.0*np.log(problem['ndim_problem'] + 1.0))`),
                * 'c_s'           - learning rate for population success rule (`float`, default: `0.3`),
                * 'd_s'           - delay rate for population success rule (`float`, default: `1.0`),
                * 'z_star'        - target success rate for population success rule (`float`, default: `0.25`),
                * 'n_individuals' - number of offspring, aka offspring population size (`int`, default:
                  `4 + int(3*np.log(problem['ndim_problem']))`),
                * 'n_parents'     - number of parents, aka parental population size (`int`, default:
                  `int(options['n_individuals']/2)`).

    Examples
    --------
    Use the black-box optimizer `LMCMAES` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy  # engine for numerical computing
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.es.lmcmaes import LMCMAES
       >>> problem = {'fitness_function': rosenbrock,  # to define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5.0*numpy.ones((2,)),
       ...            'upper_boundary': 5.0*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # to set optimizer options
       ...            'seed_rng': 2022,
       ...            'mean': 3.0*numpy.ones((2,)),
       ...            'sigma': 3.0}  # global step-size may need to be tuned for optimality
       >>> lmcmaes = LMCMAES(problem, options)  # to initialize the optimizer class
       >>> results = lmcmaes.optimize()  # to run the optimization/evolution process
       >>> print(f"LMCMAES: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       LMCMAES: 5000, 7.8681e-12

    For its correctness checking of Python coding, please refer to `this code-based repeatability report
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/es/_repeat_lmcmaes.py>`_
    for all details. For *pytest*-based automatic testing, please see `test_lmcmaes.py
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/es/test_lmcmaes.py>`_.

    Attributes
    ----------
    c_c           : `float`
                    learning rate for evolution path update.
    c_s           : `float`
                    learning rate for population success rule.
    c_1           : `float`
                    learning rate for covariance matrix adaptation.
    d_s           : `float`
                    delay rate for population success rule.
    m             : `int`
                    number of direction vectors.
    mean          : `array_like`
                    initial (starting) point, aka mean of Gaussian search distribution.
    n_individuals : `int`
                    number of offspring, aka offspring population size.
    n_parents     : `int`
                    number of parents, aka parental population size.
    n_steps       : `int`
                    target number of generations between vectors.
    sigma         : `float`
                    initial global step-size, aka mutation strength.
    z_star        : `float`
                    target success rate for population success rule.

    References
    ----------
    Loshchilov, I., 2014, July.
    `A computationally efficient limited memory CMA-ES for large scale optimization.
    <https://dl.acm.org/doi/abs/10.1145/2576768.2598294>`_
    In Proceedings of Annual Conference on Genetic and Evolutionary Computation (pp. 397-404). ACM.

    Please refer to the *official* C++ version from Loshchilov (now at NVIDIA):
    https://sites.google.com/site/lmcmaeses/
    """
    def __init__(self, problem, options):
        ES.__init__(self, problem, options)
        self.m = options.get('m', 4 + int(3*np.log(self.ndim_problem)))  # number of direction vectors
        self.n_steps = options.get('n_steps', self.m)  # target number of generations between vectors
        self.c_c = options.get('c_c', 1.0/self.m)  # learning rate for evolution path update
        self.c_1 = options.get('c_1', 1.0/(10.0*np.log(self.ndim_problem + 1.0)))
        self.c_s = options.get('c_s', 0.3)  # learning rate for population success rule (PSR)
        self.d_s = options.get('d_s', 1.0)  # damping parameter for PSR
        self.z_star = options.get('z_star', 0.25)  # target success rate for PSR
        self._a = np.sqrt(1.0 - self.c_1)
        self._c = 1.0/np.sqrt(1.0 - self.c_1)
        self._bd_1 = np.sqrt(1.0 - self.c_1)
        self._bd_2 = self.c_1/(1.0 - self.c_1)
        self._p_c_1 = 1.0 - self.c_c
        self._p_c_2 = None
        self._j = None
        self._l = None
        self._it = None
        self._rr = None  # for PSR

    def initialize(self, is_restart=False):
        mean = self._initialize_mean(is_restart)  # mean of Gaussian search distribution
        x = np.empty((self.n_individuals, self.ndim_problem))  # offspring population
        p_c = np.zeros((self.ndim_problem,))  # evolution path
        s = 0.0  # for PSR of global step-size adaptation
        vm = np.empty((self.m, self.ndim_problem))
        pm = np.empty((self.m, self.ndim_problem))
        b = np.empty((self.m,))
        d = np.empty((self.m,))
        y = np.empty((self.n_individuals,))  # fitness (no evaluation)
        self._p_c_2 = np.sqrt(self.c_c*(2.0 - self.c_c)*self._mu_eff)
        self._rr = np.arange(self.n_individuals*2, 0, -1) - 1
        self._j = [None]*self.m
        self._l = [None]*self.m
        self._it = 0
        return mean, x, p_c, s, vm, pm, b, d, y

    def _a_z(self, z=None, pm=None, vm=None, b=None):  # Algorithm 3 Az()
        x = np.copy(z)
        for t in range(self._it):
            x = self._a*x + b[self._j[t]]*np.dot(vm[self._j[t]], z)*pm[self._j[t]]
        return x

    def iterate(self, mean=None, x=None, pm=None, vm=None, y=None, b=None, args=None):
        sign, a_z = 1, np.empty((self.ndim_problem,))  # for mirrored sampling
        for k in range(self.n_individuals):
            if self._check_terminations():
                return x, y
            if sign == 1:
                z = self.rng_optimization.standard_normal((self.ndim_problem,))
                a_z = self._a_z(z, pm, vm, b)
            x[k] = mean + sign*self.sigma*a_z
            y[k] = self._evaluate_fitness(x[k], args)
            sign *= -1  # sampling in the opposite direction for mirrored sampling
        return x, y

    def _a_inv_z(self, v=None, vm=None, d=None, i=None):  # Algorithm 4 Ainvz()
        x = np.copy(v)
        for t in range(0, i):
            x = self._c*x - d[self._j[t]]*np.dot(vm[self._j[t]], x)*vm[self._j[t]]
        return x

    def _update_distribution(self, mean=None, x=None, p_c=None, s=None, vm=None,
                             pm=None, b=None, d=None, y=None, y_bak=None):
        mean_bak = np.dot(self._w, x[np.argsort(y)[:self.n_parents]])
        p_c = self._p_c_1*p_c + self._p_c_2*(mean_bak - mean)/self.sigma
        i_min = 1
        if self._n_generations < self.m:
            self._j[self._n_generations] = self._n_generations
        else:
            d_min = self._l[self._j[i_min]] - self._l[self._j[i_min - 1]]
            for j in range(2, self.m):
                d_cur = self._l[self._j[j]] - self._l[self._j[j - 1]]
                if d_cur < d_min:
                    d_min, i_min = d_cur, j
            # start from 0 if all pairwise distances exceed `self.n_steps`
            i_min = 0 if d_min >= self.n_steps else i_min
            # update indexes of evolution paths (`self._j[i_min]` is index of evolution path needed to delete)
            updated = self._j[i_min]
            for j in range(i_min, self.m - 1):
                self._j[j] = self._j[j + 1]
            self._j[self.m - 1] = updated
        self._it = np.minimum(self._n_generations + 1, self.m)
        self._l[self._j[self._it - 1]] = self._n_generations  # to update its generation
        pm[self._j[self._it - 1]] = p_c  # to add the latest evolution path
        # since `self._j[i_min]` is deleted, all vectors (from vm) depending on it need to be computed again
        for i in range(0 if i_min == 1 else i_min, self._it):
            vm[self._j[i]] = self._a_inv_z(pm[self._j[i]], vm, d, i)
            v_n = np.dot(vm[self._j[i]], vm[self._j[i]])
            bd_3 = np.sqrt(1.0 + self._bd_2*v_n)
            b[self._j[i]] = self._bd_1/v_n*(bd_3 - 1.0)
            d[self._j[i]] = 1.0/(self._bd_1*v_n)*(1.0 - 1.0/bd_3)
        if self._n_generations > 0:  # for population success rule (PSR)
            r = np.argsort(np.hstack((y, y_bak)))
            z_psr = np.sum(self._rr[r < self.n_individuals] - self._rr[r >= self.n_individuals])
            z_psr = z_psr/np.power(self.n_individuals, 2) - self.z_star
            s = (1.0 - self.c_s)*s + self.c_s*z_psr
            self.sigma *= np.exp(s/self.d_s)
        return mean_bak, p_c, s, vm, pm, b, d

    def restart_reinitialize(self, mean=None, x=None, p_c=None, s=None,
                             vm=None, pm=None, b=None, d=None, y=None):
        if self.is_restart and ES.restart_reinitialize(self, y):
            mean, x, p_c, s, vm, pm, b, d, y = self.initialize(True)
            self.d_s *= 2.0
        return mean, x, p_c, s, vm, pm, b, d, y

    def optimize(self, fitness_function=None, args=None):  # for all generations (iterations)
        fitness = ES.optimize(self, fitness_function)
        mean, x, p_c, s, vm, pm, b, d, y = self.initialize()
        while not self.termination_signal:
            y_bak = np.copy(y)
            # sample and evaluate offspring population
            x, y = self.iterate(mean, x, pm, vm, y, b, args)
            if self._check_terminations():
                break
            mean, p_c, s, vm, pm, b, d = self._update_distribution(
                mean, x, p_c, s, vm, pm, b, d, y, y_bak)
            self._print_verbose_info(fitness, y)
            self._n_generations += 1
            mean, x, p_c, s, vm, pm, b, d, y = self.restart_reinitialize(
                mean, x, p_c, s, vm, pm, b, d, y)
        results = self._collect(fitness, y, mean)
        results['p_c'] = p_c
        results['s'] = s
        return results
