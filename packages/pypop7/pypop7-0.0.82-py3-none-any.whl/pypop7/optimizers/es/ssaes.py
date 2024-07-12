import numpy as np  # engine for numerical computing

from pypop7.optimizers.es.es import ES  # abstract class of all evolution strategies (ES)


class SSAES(ES):
    """Schwefel's Self-Adaptation Evolution Strategy (SSAES).

    .. note:: `SSAES` adapts all the **individual** step-sizes (aka coordinate-wise standard deviations)
       on-the-fly, proposed by Schwefel (one recipient of `IEEE Evolutionary Computation Pioneer Award
       2002 <https://tinyurl.com/456as566>`_ and `IEEE Frank Rosenblatt Award 2011
       <https://en.wikipedia.org/wiki/IEEE_Frank_Rosenblatt_Award>`_). Since it often needs a *relatively
       large* population (e.g., larger than number of dimensionality) for reliable self-adaptation, `SSAES`
       suffers easily from *slow* convergence for large-scale black-box optimization. Therefore, it is
       recommended to first attempt more advanced ES variants (e.g., `LMCMA`, `LMMAES`) for large-scale
       black-box optimization. Here we include `SSAES` mainly for *benchmarking* and *theoretical* purpose.
       Currently the `restart` process is not implemented owing to its typically slow convergence.

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
                * 'sigma'          - initial global step-size, aka mutation strength (`float`),
                * 'mean'           - initial (starting) point, aka mean of Gaussian search distribution (`array_like`),

                  * if not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`.

                * 'n_individuals'  - number of offspring, aka offspring population size (`int`, default:
                  `5*problem['ndim_problem']`),
                * 'n_parents'      - number of parents, aka parental population size (`int`, default:
                  `int(options['n_individuals']/4)`),
                * 'lr_sigma'       - learning rate of global step-size self-adaptation (`float`, default:
                  `1.0/np.sqrt(problem['ndim_problem'])`),
                * 'lr_axis_sigmas' - learning rate of individual step-sizes self-adaptation (`float`, default:
                  `1.0/np.power(problem['ndim_problem'], 1.0/4.0)`).

    Examples
    --------
    Use the black-box optimizer `SSAES` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy  # engine for numerical computing
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.es.ssaes import SSAES
       >>> problem = {'fitness_function': rosenbrock,  # to define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5.0*numpy.ones((2,)),
       ...            'upper_boundary': 5.0*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # to set optimizer options
       ...            'seed_rng': 2022,
       ...            'mean': 3.0*numpy.ones((2,)),
       ...            'sigma': 3.0}  # global step-size may need to be tuned for optimality
       >>> ssaes = SSAES(problem, options)  # to initialize the black-box optimizer class
       >>> results = ssaes.optimize()  # to run the optimization/evolution process
       >>> print(f"SSAES: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       SSAES: 5000, 0.0002

    For its correctness checking of coding, refer to `this code-based repeatability report
    <https://tinyurl.com/zsmsyh2x>`_ for more details.

    Attributes
    ----------
    best_so_far_x  : `array_like`
                     final best-so-far solution found during entire optimization.
    best_so_far_y  : `array_like`
                     final best-so-far fitness found during entire optimization.
    lr_axis_sigmas : `float`
                     learning rate of individual step-sizes self-adaptation.
    lr_sigma       : `float`
                     learning rate of global step-size self-adaptation.
    mean           : `array_like`
                     initial (starting) point, aka mean of Gaussian search distribution.
    n_individuals  : `int`
                     number of offspring, aka offspring population size.
    n_parents      : `int`
                     number of parents, aka parental population size.
    sigma          : `float`
                     initial global step-size, aka mutation strength.
    _axis_sigmas   : `array_like`
                     final individuals step-sizes (updated during optimization).

    References
    ----------
    Hansen, N., Arnold, D.V. and Auger, A., 2015.
    `Evolution strategies.
    <https://link.springer.com/chapter/10.1007%2F978-3-662-43505-2_44>`_
    In Springer Handbook of Computational Intelligence (pp. 871-898). Springer, Berlin, Heidelberg.

    Beyer, H.G. and Schwefel, H.P., 2002.
    `Evolution strategies–A comprehensive introduction.
    <https://link.springer.com/article/10.1023/A:1015059928466>`_
    Natural Computing, 1(1), pp.3-52.

    Schwefel, H.P., 1988.
    `Collective intelligence in evolving systems.
    <https://link.springer.com/chapter/10.1007/978-3-642-73953-8_8>`_
    In Ecodynamics (pp. 95-100). Springer, Berlin, Heidelberg.

    Schwefel, H.P., 1984.
    `Evolution strategies: A family of non-linear optimization techniques based on imitating
    some principles of organic evolution.
    <https://link.springer.com/article/10.1007/BF01876146>`_
    Annals of Operations Research, 1(2), pp.165-167.
    """
    def __init__(self, problem, options):
        if options.get('n_individuals') is None:
            options['n_individuals'] = 5*problem.get('ndim_problem')
        if options.get('n_parents') is None:
            options['n_parents'] = int(options['n_individuals']/4)
        ES.__init__(self, problem, options)
        if self.lr_sigma is None:
            self.lr_sigma = 1.0/np.sqrt(self.ndim_problem)  # learning rate of global step-size self-adaptation
        assert self.lr_sigma > 0, f'`self.lr_sigma` = {self.lr_sigma}, but should > 0.'
        # set learning rate of individual step-sizes self-adaptation
        self.lr_axis_sigmas = options.get('lr_axis_sigmas', 1.0/np.power(self.ndim_problem, 1.0/4.0))
        assert self.lr_axis_sigmas > 0, f'`self.lr_axis_sigmas` = {self.lr_axis_sigmas}, but should > 0.'
        self._axis_sigmas = self.sigma*np.ones((self.ndim_problem,))  # individual step-sizes

    def initialize(self):
        x = np.empty((self.n_individuals, self.ndim_problem))  # offspring population
        mean = self._initialize_mean()  # mean of Gaussian search distribution
        sigmas = np.empty((self.n_individuals, self.ndim_problem))  # individual step-sizes for all offspring
        y = np.empty((self.n_individuals,))  # fitness (no evaluation)
        return x, mean, sigmas, y

    def iterate(self, x=None, mean=None, sigmas=None, y=None, args=None):
        for k in range(self.n_individuals):  # sample offspring population
            if self._check_terminations():
                return x, sigmas, y
            sigma = self.lr_sigma*self.rng_optimization.standard_normal()
            axis_sigmas = self.lr_axis_sigmas*self.rng_optimization.standard_normal((self.ndim_problem,))
            sigmas[k] = self._axis_sigmas*np.exp(axis_sigmas)*np.exp(sigma)
            x[k] = mean + sigmas[k]*self.rng_optimization.standard_normal((self.ndim_problem,))
            y[k] = self._evaluate_fitness(x[k], args)
        return x, sigmas, y

    def optimize(self, fitness_function=None, args=None):  # for all generations (iterations)
        fitness = ES.optimize(self, fitness_function)
        x, mean, sigmas, y = self.initialize()
        while True:
            x, sigmas, y = self.iterate(x, mean, sigmas, y, args)
            if self._check_terminations():
                break
            order = np.argsort(y)[:self.n_parents]
            self._axis_sigmas = np.mean(sigmas[order], axis=0)
            mean = np.mean(x[order], axis=0)
            self._print_verbose_info(fitness, y)
            self._n_generations += 1
        results = self._collect(fitness, y, mean)
        results['_axis_sigmas'] = self._axis_sigmas
        return results
