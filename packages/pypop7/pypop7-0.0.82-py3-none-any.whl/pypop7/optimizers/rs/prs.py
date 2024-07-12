import numpy as np

from pypop7.optimizers.rs.rs import RS


class PRS(RS):
    """Pure Random Search (PRS).

    .. note:: `PRS` is one of the *simplest* and *earliest* black-box optimizers, dating back to at least
       `1950s <https://pubsonline.informs.org/doi/abs/10.1287/opre.6.2.244>`_. Although recently it
       has been successfully applied in several *relatively low-dimensional* problems (particularly
       `hyper-parameter optimization <https://www.jmlr.org/papers/v13/bergstra12a.html>`_), it generally
       suffers from the famous **curse of dimensionality** for large-scale black-box optimization,
       owing to the lack of *adaptation*, a highly desirable property for most sophisticated search
       algorithms. Therefore, it is **highly recommended** to first attempt more advanced (e.g.
       population-based) methods for large-scale black-box optimization.

       As pointed out in the well-recognized book `Probabilistic Machine Learning (written by Kevin Patrick Murphy)
       <https://probml.github.io/pml-book/book2.html>`_, *"A surprisingly effective strategy in problems where
       we know nothing about the objective is to use random search. This should always be tried as a baseline"*.

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
                * 'seed_rng'                 - seed for random number generation needed to be *explicitly* set (`int`).

    Examples
    --------
    Use the `PRS` optimizer to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.rs.prs import PRS
       >>> problem = {'fitness_function': rosenbrock,  # define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5.0*numpy.ones((2,)),
       ...            'upper_boundary': 5.0*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # set optimizer options
       ...            'seed_rng': 2022}
       >>> prs = PRS(problem, options)  # initialize the optimizer class
       >>> results = prs.optimize()  # run the optimization process
       >>> # return the number of used function evaluations and found best-so-far fitness
       >>> print(f"PRS: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       PRS: 5000, 0.11497678820610932

    For its correctness checking of coding, refer to `this code-based repeatability report
    <https://tinyurl.com/mrx2kffy>`_ for more details.

    References
    ----------
    Bergstra, J. and `Bengio, Y. <https://yoshuabengio.org/>`_, 2012.
    `Random search for hyper-parameter optimization.
    <https://www.jmlr.org/papers/v13/bergstra12a.html>`_
    Journal of Machine Learning Research, 13(10), pp.281-305.

    `Schmidhuber, J. <https://people.idsia.ch/~juergen/>`_, Hochreiter, S. and
    `Bengio, Y. <https://yoshuabengio.org/>`_, 2001.
    `Evaluating benchmark problems by random guessing.
    <https://ml.jku.at/publications/older/ch9.pdf>`_
    A Field Guide to Dynamical Recurrent Networks, pp.231-235.

    Karnopp, D.C., 1963.
    `Random search techniques for optimization problems.
    <https://www.sciencedirect.com/science/article/abs/pii/0005109863900189>`_
    Automatica, 1(2-3), pp.111-121.

    Brooks, S.H., 1959.
    `A comparison of maximum-seeking methods.
    <https://pubsonline.informs.org/doi/abs/10.1287/opre.7.4.430>`_
    Operations Research, 7(4), pp.430-457.

    Brooks, S.H., 1958.
    `A discussion of random methods for seeking maxima.
    <https://pubsonline.informs.org/doi/abs/10.1287/opre.6.2.244>`_
    Operations Research, 6(2), pp.244-251.
    """
    def __init__(self, problem, options):
        RS.__init__(self, problem, options)
        # set default: 1 -> uniformly distributed random sampling
        self._sampling_type = options.get('_sampling_type', 1)
        if self._sampling_type not in [0, 1]:  # 0 -> normally distributed random sampling
            info = 'For currently {:s}, only support uniformly or normally distributed random sampling.'
            raise ValueError(info.format(self.__class__.__name__))
        elif self._sampling_type == 0:
            self.sigma = options.get('sigma')  # initial global step-size (fixed during optimization)
            assert self.sigma is not None

    def _sample(self, rng):
        if self._sampling_type == 0:
            x = self.x + self.sigma*rng.standard_normal(size=(self.ndim_problem,))
        else:
            x = rng.uniform(self.initial_lower_boundary, self.initial_upper_boundary)
        return x

    def initialize(self):
        if self.x is None:
            x = self._sample(self.rng_initialization)
        else:
            x = np.copy(self.x)
        assert len(x) == self.ndim_problem
        return x

    def iterate(self):  # individual-based sampling
        return self._sample(self.rng_optimization)
