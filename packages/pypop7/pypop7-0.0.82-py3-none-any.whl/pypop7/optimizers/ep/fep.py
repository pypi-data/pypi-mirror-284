import numpy as np  # engine for numerical computing

from pypop7.optimizers.ep.cep import CEP


class FEP(CEP):
    """Fast Evolutionary Programming with self-adaptive mutation of individual step-sizes (FEP).

    .. note:: `FEP` was proposed mainly by Yao et al. in 1999 (the recipient of `IEEE Evolutionary Computation Pioneer
       Award 2013 <https://tinyurl.com/456as566>`_ and `IEEE Frank Rosenblatt Award 2020 <https://tinyurl.com/yj28zxfa>`_
       ), where the classical Gaussian sampling distribution is replaced by the heavy-tailed Cachy distribution for
       better exploration on multi-modal black-box optimization problems.

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
                * 'n_individuals'  - number of offspring, aka offspring population size (`int`, default: `100`),
                * 'q'              - number of opponents for pairwise comparisons (`int`, default: `10`),
                * 'tau'            - learning rate of individual step-sizes self-adaptation (`float`, default:
                  `1.0/np.sqrt(2.0*np.sqrt(problem['ndim_problem']))`),
                * 'tau_apostrophe' - learning rate of individual step-sizes self-adaptation (`float`, default:
                  `1.0/np.sqrt(2.0*problem['ndim_problem'])`.

    Examples
    --------
    Use the optimizer `FEP` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy  # engine for numerical computing
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.ep.fep import FEP
       >>> problem = {'fitness_function': rosenbrock,  # to define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5.0*numpy.ones((2,)),
       ...            'upper_boundary': 5.0*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # to set optimizer options
       ...            'seed_rng': 2022,
       ...            'sigma': 3.0}  # global step-size may need to be tuned
       >>> fep = FEP(problem, options)  # to initialize the optimizer class
       >>> results = fep.optimize()  # to run its optimization/evolution process
       >>> # to return the number of function evaluations and the best-so-far fitness
       >>> print(f"FEP: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       FEP: 5000, 0.005781004466936902

    For its correctness checking, refer to `this code-based repeatability report
    <https://tinyurl.com/bdh7epah>`_ for more details.

    Attributes
    ----------
    best_so_far_x  : `array_like`
                     final best-so-far solution found during entire optimization.
    best_so_far_y  : `array_like`
                     final best-so-far fitness found during entire optimization.
    n_individuals  : `int`
                     number of offspring, aka offspring population size.
    q              : `int`
                     number of opponents for pairwise comparisons.
    sigma          : `float`
                     initial global step-size, aka mutation strength.
    tau            : `float`
                     self-adaptation learning rate of individual step-sizes.
    tau_apostrophe : `float`
                     self-adaptation learning rate of individual step-sizes.

    References
    ----------
    Yao, X., Liu, Y. and Lin, G., 1999.
    `Evolutionary programming made faster.
    <https://ieeexplore.ieee.org/abstract/document/771163>`_
    IEEE Transactions on Evolutionary Computation, 3(2), pp.82-102.

    Chellapilla, K. and Fogel, D.B., 1999.
    `Evolution, neural networks, games, and intelligence.
    <https://ieeexplore.ieee.org/abstract/document/784222>`_
    Proceedings of the IEEE, 87(9), pp.1471-1496.

    Bäck, T. and Schwefel, H.P., 1993.
    `An overview of evolutionary algorithms for parameter optimization.
    <https://direct.mit.edu/evco/article-abstract/1/1/1/1092/An-Overview-of-Evolutionary-Algorithms-for>`_
    Evolutionary Computation, 1(1), pp.1-23.
    """
    def __init__(self, problem, options):
        CEP.__init__(self, problem, options)

    def iterate(self, x=None, sigmas=None, y=None, xx=None, ss=None, yy=None, args=None):
        for i in range(self.n_individuals):
            if self._check_terminations():
                return x, sigmas, y, xx, ss, yy
            ss[i] = sigmas[i]*np.exp(self.tau_apostrophe*self.rng_optimization.standard_normal(
                size=(self.ndim_problem,)) + self.tau*self.rng_optimization.standard_normal(
                size=(self.ndim_problem,)))
            xx[i] = x[i] + ss[i]*self.rng_optimization.standard_cauchy(size=(self.ndim_problem,))
            yy[i] = self._evaluate_fitness(xx[i], args)
        new_x = np.vstack((xx, x))
        new_sigmas = np.vstack((ss, sigmas))
        new_y = np.hstack((yy, y))
        n_win = np.zeros((2*self.n_individuals,))  # number of win
        for i in range(2*self.n_individuals):
            for j in self.rng_optimization.choice([k for k in range(2*self.n_individuals) if k != i],
                                                  size=self.q, replace=False):
                if new_y[i] < new_y[j]:
                    n_win[i] += 1
        order = np.argsort(-n_win)[:self.n_individuals]
        x[:self.n_individuals] = new_x[order]
        sigmas[:self.n_individuals] = new_sigmas[order]
        y[:self.n_individuals] = new_y[order]
        self._n_generations += 1
        return x, sigmas, y, xx, ss, yy
