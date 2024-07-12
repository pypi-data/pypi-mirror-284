import numpy as np  # engine for numerical computing

from pypop7.optimizers.nes import NES  # abstract class of all Natural Evolution Strategies (NES)


class VKDCMA(NES):
    """Projection-based Covariance Matrix Adaptation (VKDCMA).

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
                * 'mean'          - initial (starting) point, aka mean of Gaussian search distribution (`array_like`),

                  * if not given, it will draw a random sample from the uniform distribution whose search range is
                    bounded by `problem['lower_boundary']` and `problem['upper_boundary']`.

                * 'n_individuals' - number of offspring, aka offspring population size (`int`, default:
                  `4 + int(3*np.log(problem['ndim_problem']))`),
                * 'n_parents'     - number of parents, aka parental population size (`int`, default:
                  `int(options['n_individuals']/2)`).

    Examples
    --------
    Use the optimizer to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.nes.vkdcma import VKDCMA
       >>> problem = {'fitness_function': rosenbrock,  # define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5*numpy.ones((2,)),
       ...            'upper_boundary': 5*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # set optimizer options
       ...            'seed_rng': 2022,
       ...            'mean': 3*numpy.ones((2,)),
       ...            'sigma': 0.1}  # the global step-size may need to be tuned for better performance
       >>> vkdcma = VKDCMA(problem, options)  # initialize the optimizer class
       >>> results = vkdcma.optimize()  # run the optimization process
       >>> # return the number of function evaluations and best-so-far fitness
       >>> print(f"VKDCMA: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       VKDCMA: 5000, 1.7960753151742513e-13

    For its correctness checking of coding, refer to `this code-based repeatability report
    <https://tinyurl.com/mrxvx4hk>`_ for more details.

    Attributes
    ----------
    mean          : `array_like`
                    initial (starting) point, aka mean of Gaussian search distribution.
    n_individuals : `int`
                    number of offspring, aka offspring population size.
    n_parents     : `int`
                    number of parents, aka parental population size.
    sigma         : `float`
                    final global step-size, aka mutation strength.

    References
    ----------
    Akimoto, Y. and Hansen, N., 2016, September.
    `Online model selection for restricted covariance matrix adaptation.
    <https://link.springer.com/chapter/10.1007/978-3-319-45823-6_1>`_
    In Parallel Problem Solving from Nature. Springer International Publishing.

    Akimoto, Y. and Hansen, N., 2016, July.
    `Projection-based restricted covariance matrix adaptation for high dimension.
    <https://dl.acm.org/doi/abs/10.1145/2908812.2908863>`_
    In Proceedings of Annual Genetic and Evolutionary Computation Conference 2016 (pp. 197-204). ACM.

    Akimoto, Y., Nagata, Y., Ono, I. and Kobayashi, S., 2012.
    `Theoretical foundation for CMA-ES from information geometry perspective.
    <https://doi.org/10.1007/s00453-011-9564-8>`_
    Algorithmica, 64, pp.698-716.

    Akimoto, Y., Nagata, Y., Ono, I. and Kobayashi, S., 2010.
    `Bidirectional relation between CMA evolution strategies and natural evolution strategies.
    <https://doi.org/10.1007/978-3-642-15844-5_16>`_
    In International Conference on Parallel Problem Solving from Nature (pp. 154-163). Springer Berlin Heidelberg.

    See the official Python version from Prof. Akimoto:
    https://gist.github.com/youheiakimoto/2fb26c0ace43c22b8f19c7796e69e108
    """

    def _get_m(self, d_x, d, v, s):
        dx_d = d_x / d
        v_dxd = np.dot(v[:self.k_a], dx_d)
        return np.sum(dx_d * dx_d) - np.sum((v_dxd * v_dxd) * (s[:self.k_a] / (s[:self.k_a] + 1.0)))

    def _get_lr(self, k):
        c_1 = 2.0 / (self.ndim_problem * (k + 1.0) + self.ndim_problem + 2.0 * (k + 2.0) + self._mu_eff)
        c_mu = min(1.0 - c_1, 2.0 * (self._mu_eff - 2.0 + 1.0 / self._mu_eff) / (
                self.ndim_problem * (k + 1) + 4.0 * (k + 2.0) + self._mu_eff))
        return c_1, c_mu, np.sqrt(c_1)

    def _get_det(self, d, s):
        return 2.0 * np.sum(np.log(d)) + np.sum(np.log(1.0 + s[:self.k_a]))

    def __init__(self, problem, options):
        NES.__init__(self, problem, options)
        self.options = options
        self.k, self.k_a, self.k_i = 0, 0, 0
        self.c_s, self.d_s = 0.3, np.sqrt(self.ndim_problem)
        self._injection = False
        self.c_1, self.c_mu, self.c_c = None, None, None
        self.l_s, self.l_d, self.l_c = None, None, None
        self.e_s, self.e_d, self.e_c = None, None, None

    def initialize(self, is_restart=False):
        self.k, self.k_a, self.k_i = 0, 0, 0
        self.l_s = np.log(self.sigma)
        self.l_d = 2.0 * np.log(np.ones((self.ndim_problem,)))
        self.l_c = np.zeros((self.ndim_problem,))
        self.e_s = np.zeros((1,))
        self.e_d = np.zeros((self.ndim_problem,))
        self.e_c = np.zeros((self.ndim_problem,))
        self.c_1, self.c_mu, self.c_c = self._get_lr(self.k)
        self.c_s, self.d_s = 0.3, np.sqrt(self.ndim_problem)
        self._injection = False
        d = np.ones((self.ndim_problem,))
        p_s = 0
        v = np.zeros((self.k, self.ndim_problem))
        s = np.zeros((self.ndim_problem,))
        p_c = np.zeros((self.ndim_problem,))
        d_x = np.zeros((self.ndim_problem,))
        u = np.zeros((self.ndim_problem, self.k + self.n_parents + 1))
        mean = self._initialize_mean(is_restart)  # mean of Gaussian search distribution
        x = np.zeros((self.n_individuals, self.ndim_problem))
        y = np.zeros((self.n_individuals,))
        return d, p_s, v, s, p_c, d_x, u, mean, x, y

    def iterate(self, d=None, p_s=None, v=None, s=None, p_c=None, d_x=None,
                u=None, mean=None, x=None, y=None, args=None):
        k, k_a = self.k, self.k_a
        z = (self.rng_optimization.standard_normal((self.n_individuals, self.ndim_problem)) + np.dot(
            self.rng_optimization.standard_normal((self.n_individuals, k_a)) * np.sqrt(
                s[:k_a]), v[:k_a])) * d
        if self._injection:
            zz = (np.linalg.norm(self.rng_optimization.standard_normal((self.ndim_problem,))) / np.sqrt(
                self._get_m(d_x, d, v, s))) * d_x
            z[0], z[1] = zz, -zz
        x = mean + self.sigma * z
        for i in range(self.n_individuals):
            if self._check_terminations():
                return d, p_s, v, s, p_c, d_x, u, mean, x, y
            y[i] = self._evaluate_fitness(x[i], args)
        order = np.argsort(y)
        s_z = z[order[:self.n_parents]]
        d_x = np.dot(self._w, s_z)
        mean += self.sigma * d_x
        if self._injection:
            p_s += self.c_s * ((np.where(order == 1)[0][0] - np.where(order == 0)[0][0]) / (
                    self.n_individuals - 1.0) - p_s)
            self.sigma *= np.exp(p_s / self.d_s)
            h_s = p_s < 0.5
        else:
            self._injection, h_s = True, True
        p_c = (1.0 - self.c_c) * p_c + h_s * np.sqrt(self.c_c * (2.0 - self.c_c) * self._mu_eff) * d_x
        if self.c_mu == 0.0:
            r_u = k_a + 1
            alpha = np.sqrt(abs(1.0 - self.c_mu - self.c_1 + self.c_1 * (
                    1.0 - h_s) * self.c_c * (2.0 - self.c_c)))
            u[:, :k_a] = (v[:k_a].T * (np.sqrt(s[:k_a]) * alpha))
            u[:, r_u - 1] = np.sqrt(self.c_1) * (p_c / d)
        elif self.c_1 == 0.0:
            r_u = k_a + self.n_parents
            alpha = np.sqrt(abs(1.0 - self.c_mu - self.c_1 + self.c_1 * (
                    1.0 - h_s) * self.c_c * (2.0 - self.c_c)))
            u[:, :k_a] = (v[:k_a].T * (np.sqrt(s[:k_a]) * alpha))
            u[:, k_a:r_u] = np.sqrt(self.c_mu) * np.sqrt(self._w) * (s_z / d).T
        else:
            r_u = k_a + self.n_parents + 1
            alpha = np.sqrt(abs(1.0 - self.c_mu - self.c_1 + self.c_1 * (
                    1.0 - h_s) * self.c_c * (2.0 - self.c_c)))
            u[:, :k_a] = (v[:k_a].T * (np.sqrt(s[:k_a]) * alpha))
            u[:, k_a:r_u - 1] = np.sqrt(self.c_mu) * np.sqrt(self._w) * (s_z / d).T
            u[:, r_u - 1] = np.sqrt(self.c_1) * (p_c / d)
        if self.ndim_problem > r_u:
            dd, right = np.linalg.eigh(np.dot(u[:, :r_u].T, u[:, :r_u]))
            i_e = np.argsort(dd)[::-1]
            gamma = 0 if r_u <= k else dd[i_e[k:]].sum() / (self.ndim_problem - k)
            self.k_a = k_a = min(int(np.sum(dd >= 0)), k)
            s[:k_a] = (dd[i_e[:k_a]] - gamma) / (alpha * alpha + gamma)
            v[:k_a] = (np.dot(u[:, :r_u], right[:, i_e[:k_a]]) / np.sqrt(dd[i_e[:k_a]])).T
        else:
            dd, left = np.linalg.eigh(np.dot(u[:, :r_u], u[:, :r_u].T))
            i_e = np.argsort(dd)[::-1]
            gamma = 0 if r_u <= k else dd[i_e[k:]].sum() / (self.ndim_problem - k)
            self.k_a = k_a = min(int(np.sum(dd >= 0)), k)
            s[:k_a] = (dd[i_e[:k_a]] - gamma) / (alpha * alpha + gamma)
            v[:k_a] = left[:, i_e[:k_a]].T
        d *= np.sqrt((alpha * alpha + np.sum(u[:, :r_u] * u[:, :r_u], axis=1)) / (
                1.0 + np.dot(s[:k_a], v[:k_a] * v[:k_a])))
        e = np.exp(self._get_det(d, s) / self.ndim_problem / 2.0)
        d, p_c = d / e, p_c / e
        self.k_i += 1
        self.e_s = np.log(self.sigma) - self.l_s
        l_s_c = self.e_s / (0.5 * min(1.0, self.n_individuals / self.ndim_problem) / 3.0)
        self.l_s = np.log(self.sigma)
        self.e_d = 2.0 * np.log(d) + np.log(1.0 + np.dot(s[:self.k], v[:self.k] ** 2)) - self.l_d
        l_d_c = self.e_d / (self.c_mu + self.c_1)
        self.l_d = 2.0 * np.log(d) + np.log(1.0 + np.dot(s[:self.k], v[:self.k] ** 2))
        self.e_c = np.log(1.0 + s) - self.l_c
        l_l_c = self.e_c / (self.c_mu + self.c_1)
        self.l_c = np.log(1.0 + s)
        k_i = (self.k_i > (2.0 * self.ndim_problem - 1.0)) * (self.k < (self.ndim_problem - 1.0)) * np.all(
            (1.0 + s[:self.k]) > 30.0) * (np.abs(l_s_c) < 0.1) * np.all(np.abs(l_d_c) < 1.0)
        k_d = (self.k > 0) * (1.0 + s[:self.k] < 30.0) * (l_l_c[:self.k] < 0.0)
        if (self.k_i > (2 * self.ndim_problem - 1)) and k_i:
            self.k_a = k
            self.k = new_k = min(max(int(np.ceil(self.k * 1.414)), self.k + 1), (self.ndim_problem - 1))
            v = np.vstack((v, np.zeros((new_k - k, self.ndim_problem))))
            u = np.empty((self.ndim_problem, new_k + self.n_parents + 1))
            (self.c_1, self.c_mu, self.c_c) = self._get_lr(self.k)
            self.k_i = 0
        elif self.k_i > k * (2 * self.ndim_problem - 1) and np.any(k_d):
            keep = np.logical_not(k_d)
            new_k = max(np.count_nonzero(keep), 0)
            v = v[keep]
            s[:new_k] = (s[:keep.shape[0]])[keep]
            s[new_k:] = 0
            self.k = self.k_a = new_k
            (self.c_1, self.c_mu, self.c_c) = self._get_lr(self.k)
        e = np.exp(self._get_det(d, s) / self.ndim_problem / 2.0)
        d, p_c = d / e, p_c / e
        return d, p_s, v, s, p_c, d_x, u, mean, x, y

    def restart_reinitialize(self, d=None, p_s=None, v=None, s=None, p_c=None,
                             d_x=None, u=None, mean=None, x=None, y=None):
        if self.is_restart and NES.restart_reinitialize(self, y):
            d, p_s, v, s, p_c, d_x, u, mean, x, y = self.initialize(True)
        return d, p_s, v, s, p_c, d_x, u, mean, x, y

    def optimize(self, fitness_function=None, args=None):  # for all generations (iterations)
        fitness = NES.optimize(self, fitness_function)
        d, p_s, v, s, p_c, d_x, u, mean, x, y = self.initialize()
        while not self.termination_signal:
            d, p_s, v, s, p_c, d_x, u, mean, x, y = self.iterate(d, p_s, v, s, p_c, d_x, u, mean, x, y, args)
            if self._check_terminations():
                break
            self._print_verbose_info(fitness, y)
            self._n_generations += 1
            d, p_s, v, s, p_c, d_x, u, mean, x, y = self.restart_reinitialize(d, p_s, v, s, p_c, d_x, u, mean, x, y)
        results = self._collect(fitness, y, mean)
        results['d'] = d
        return results
