import numpy as np  # engine for numerical computing

from pypop7.optimizers.es.es import ES  # abstract class of all Evolution Strategies (ES) classes


class RES(ES):
    """Rechenberg's (1+1)-Evolution Strategy with 1/5th success rule (RES).

    `"Given all variances and covariances, the normal (Gaussian) distribution has the largest entropy of all
    distributions."---[Hansen, N., 2023] <https://arxiv.org/abs/1604.00772>`_

    .. note:: `RES` is the first evolution strategy with self-adaptation of the *global* step-size (designed
       by Rechenberg, one 2002 recipient of `IEEE Evolutionary Computation Pioneer Award
       <https://cis.ieee.org/awards/past-recipients#EvolutionaryComputationPioneerAward>`_), originally
       proposed for experimental optimization. As theoretically investigated in his *seminal* Ph.D.
       dissertation at Technical University of Berlin, the existence of narrow **evolution window** explains
       the necessarity of *global* step-size adaptation to maximize the local convergence progress, if possible.
       Note that a similar theoretical study was independently conducted in the automatic control community
       (`[Schumer&Steiglitz, 1968, IEEE-TAC] <https://ieeexplore.ieee.org/abstract/document/1098903>`_).

       Since there is only one parent and only one offspring for each generation (iteration), `RES` generally
       shows limited *exploration* ability for large-scale black-box optimization. Therefore, it is
       recommended to first attempt more advanced ES variants (e.g., `LMCMA`, `LMMAES`) for large-scale
       black-box optimization. Here we include `RES` (AKA two-membered ES) mainly for *benchmarking* and
       *theoretical* purposes. Interestingly, owing to its popularity, sometimes `RES` is still used now,
       such as, `[Williams&Li, 2024, NeurIPS] <https://tinyurl.com/4vdphufe>`_.

       `"As a control mechanism in practice, the 1/5th success rule has been mostly superseded by more
       sophisticated methods. However, its conceptual insight remains remarkably valuable."---[Hansen et al.,
       2015] <https://link.springer.com/chapter/10.1007%2F978-3-662-43505-2_44>`_

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
                * 'sigma'    - initial global step-size, aka mutation strength (`float`),
                * 'mean'     - initial (starting) point, aka mean of Gaussian search distribution (`array_like`),

                  * If not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`.

                * 'lr_sigma' - learning rate of global step-size self-adaptation (`float`, default:
                  `1.0/np.sqrt(problem['ndim_problem'] + 1.0)`).

    Examples
    --------
    Use the black-box optimizer `RES` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy  # engine for numerical computing
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.es.res import RES
       >>> problem = {'fitness_function': rosenbrock,  # to define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5.0*numpy.ones((2,)),
       ...            'upper_boundary': 5.0*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # to set optimizer options
       ...            'seed_rng': 2022,
       ...            'mean': 3.0*numpy.ones((2,)),
       ...            'sigma': 3.0}  # global step-size may need to be tuned for optimality
       >>> res = RES(problem, options)  # to initialize the black-box optimizer class
       >>> results = res.optimize()  # to run its optimization/evolution process
       >>> print(f"RES: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       RES: 5000, 0.0001

    For its correctness checking of Python coding, please refer to `this code-based repeatability report
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/es/_repeat_res.py>`_
    for all details. For *pytest*-based automatic testing, please see `test_res.py
    <https://github.com/Evolutionary-Intelligence/pypop/blob/main/pypop7/optimizers/es/test_res.py>`_.

    Attributes
    ----------
    best_so_far_x : `array_like`
                    final best-so-far solution found during entire optimization.
    best_so_far_y : `array_like`
                    final best-so-far fitness found during entire optimization.
    lr_sigma      : `float`
                    learning rate of global step-size self-adaptation.
    mean          : `array_like`
                    initial (starting) point, aka mean of Gaussian search distribution.
    sigma         : `float`
                    final global step-size, aka mutation strength (updated during optimization).

    References
    ----------
    Auger, A., Hansen, N., López-Ibáñez, M. and Rudolph, G., 2022.
    `Tributes to Ingo Rechenberg (1934--2021).
    <https://dl.acm.org/doi/10.1145/3511282.3511283>`_
    ACM SIGEVOlution, 14(4), pp.1-4.

    Agapie, A., Solomon, O. and Giuclea, M., 2021.
    `Theory of (1+1) ES on the RIDGE.
    <https://ieeexplore.ieee.org/abstract/document/9531957>`_
    IEEE Transactions on Evolutionary Computation, 26(3), pp.501-511.

    Hansen, N., Arnold, D.V. and Auger, A., 2015.
    `Evolution strategies.
    <https://link.springer.com/chapter/10.1007%2F978-3-662-43505-2_44>`_
    In Springer Handbook of Computational Intelligence (pp. 871-898). Springer, Berlin, Heidelberg.

    Kern, S., Müller, S.D., Hansen, N., Büche, D., Ocenasek, J. and Koumoutsakos, P., 2004.
    `Learning probability distributions in continuous evolutionary algorithms–a comparative review.
    <https://link.springer.com/article/10.1023/B:NACO.0000023416.59689.4e>`_
    Natural Computing, 3, pp.77-112.

    Beyer, H.G. and Schwefel, H.P., 2002.
    `Evolution strategies–A comprehensive introduction.
    <https://link.springer.com/article/10.1023/A:1015059928466>`_
    Natural Computing, 1(1), pp.3-52.

    Rechenberg, I., 2000.
    `Case studies in evolutionary experimentation and computation.
    <https://www.sciencedirect.com/science/article/pii/S0045782599003813>`_
    Computer Methods in Applied Mechanics and Engineering, 186(2-4), pp.125-140.

    Rechenberg, I., 1989.
    `Evolution strategy: Nature’s way of optimization.
    <https://link.springer.com/chapter/10.1007/978-3-642-83814-9_6>`_
    In Optimization: Methods and Applications, Possibilities and Limitations (pp. 106-126).
    Springer, Berlin, Heidelberg.

    Rechenberg, I., 1984.
    `The evolution strategy. A mathematical model of Darwinian evolution.
    <https://link.springer.com/chapter/10.1007/978-3-642-69540-7_13>`_
    In Synergetics—from Microscopic to Macroscopic Order (pp. 122-132). Springer, Berlin, Heidelberg.

    Rechenberg, I., 1973.
    Evolutionsstrategie: Optimierung technischer systeme nach prinzipien der biologischen evolution.
    Frommann-Holzboog Verlag, Stuttgart.
    (Note that this **seminal** Ph.D. dissertation is not read by us since it was originally written
    in German. Here we still add it owing to its historically significant contributions to
    evolutionary computation and black-box optimization.)

    Schumer, M.A. and `Steiglitz, K. <https://www.cs.princeton.edu/~ken/>`_, 1968.
    `Adaptive step size random search.
    <https://ieeexplore.ieee.org/abstract/document/1098903>`_
    IEEE Transactions on Automatic Control, 13(3), pp.270-276.
    """
    def __init__(self, problem, options):
        options['n_parents'] = 1  # mandatory setting
        options['n_individuals'] = 1  # mandatory setting
        ES.__init__(self, problem, options)
        if self.lr_sigma is None:
            self.lr_sigma = 1.0 / np.sqrt(self.ndim_problem + 1.0)
        assert self.lr_sigma > 0, f'`self.lr_sigma` = {self.lr_sigma}, but should > 0.'

    def initialize(self, args=None, is_restart=False):
        mean = self._initialize_mean(is_restart)  # mean of Gaussian search distribution
        y = self._evaluate_fitness(mean, args)  # fitness
        best_so_far_y = np.copy(y)
        self._list_initial_mean.append(np.copy(mean))
        return mean, y, best_so_far_y

    def iterate(self, args=None, mean=None):  # to sample and evaluate only one offspring
        x = mean + self.sigma * self.rng_optimization.standard_normal((self.ndim_problem,))
        y = self._evaluate_fitness(x, args)
        return x, y

    def restart_reinitialize(self, args=None, mean=None, y=None, best_so_far_y=None, fitness=None):
        if not self.is_restart:
            return mean, y, best_so_far_y
        self._list_fitness.append(best_so_far_y)
        is_restart_1, is_restart_2 = self.sigma < self.sigma_threshold, False
        if len(self._list_fitness) >= self.stagnation:
            is_restart_2 = (self._list_fitness[-self.stagnation] - self._list_fitness[-1]) < self.fitness_diff
        is_restart = bool(is_restart_1) or bool(is_restart_2)
        if is_restart:
            self._print_verbose_info(fitness, y, True)
            if self.verbose:
                print(' ....... *** restart *** .......')
            self._n_restart += 1
            self._list_generations.append(self._n_generations)  # for each restart
            self._n_generations = 0
            self.sigma = np.copy(self._sigma_bak)
            mean, y, best_so_far_y = self.initialize(args, True)
            self._list_fitness = [best_so_far_y]
        return mean, y, best_so_far_y

    def optimize(self, fitness_function=None, args=None):  # for all generations (iterations)
        fitness = ES.optimize(self, fitness_function)
        mean, y, best_so_far_y = self.initialize(args)
        while not self.termination_signal:
            self._print_verbose_info(fitness, y)
            x, y = self.iterate(args, mean)
            self._n_generations += 1
            if self._check_terminations():
                break
            self.sigma *= np.power(np.exp(float(y < best_so_far_y) - 0.2), self.lr_sigma)
            if y <= best_so_far_y:
                mean, best_so_far_y = x, y
            mean, y, best_so_far_y = self.restart_reinitialize(args, mean, y, best_so_far_y, fitness)
        return self._collect(fitness, y, mean)
