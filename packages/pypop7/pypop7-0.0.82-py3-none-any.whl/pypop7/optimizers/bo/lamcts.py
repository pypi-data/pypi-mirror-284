from typing import NamedTuple
from itertools import count
from collections import deque
import time

import numpy as np  # engine for numerical computing
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.svm import SVC

from pypop7.optimizers.bo.bo import BO  # abstract class of all Bayesian optimization (BO) classes
from pypop7.optimizers.es.cmaes import CMAES  # covariance matrix adaptation evolution strategy


class Sample(NamedTuple):  # basic data class for classification
    x: np.ndarray = np.empty(0)
    y: float = float('NaN')


def _remove_duplicate(x):  # for class Bag
    u, idx = np.unique(x, return_index=True, axis=0)
    return u.astype(dtype=float), idx


class Bag(object):  # basic data class for classification
    def __init__(self, x, y=np.empty(0)):
        self._ndim = x.shape[1] if isinstance(x, np.ndarray) else x
        if isinstance(x, np.ndarray):
            self.x, i = _remove_duplicate(x)
        else:
            self.x, i = np.empty((0, self._ndim)), None
        if y.size > 0:
            self.y = y.copy() if i is None else y[i]
        else:
            self.y = np.empty(0)
        self.best, self.mean = None, float('NaN')
        self._update_best()

    def __len__(self):
        return len(self.x)

    def _update_best(self):
        if self.y.size == 0:
            return
        self.mean, best = np.mean(self.y), np.argmin(self.y)
        if (self.best is None) or (self.y[best] < self.best.y):
            self.best = Sample(self.x[best], self.y[best])

    def extend(self, other):
        size_bak = len(self.x)
        self.x, idx = _remove_duplicate(np.concatenate((self.x, other.x)))
        if len(self.x) == size_bak:  # without duplicate
            return False
        if len(self.y) == size_bak:
            if other.y.size > 0:
                self.y = np.concatenate((self.y, other.y))[idx]
            elif len(self.y) > 0:
                self.y = np.concatenate((self.y, np.full((len(self.x) - len(self.y),), float('inf'))))
            self._update_best()
        return True


class KMSVM(object):  # classification class based on K-Means and SVM
    def __init__(self, lb, ub, rng):
        self._lb, self._ub = lb, ub
        self._min_lb, self._max_ub = np.min(lb), np.max(ub)
        self._diff = (self._max_ub - self._min_lb)/2.0
        self._center = (self._max_ub + self._min_lb)/2.0
        self._scaler = StandardScaler(with_mean=False, with_std=False)
        self._kmeans = KMeans(n_clusters=2, random_state=rng.integers(2**32))
        self._svm = SVC(kernel='rbf', gamma='auto', max_iter=100000,
                        random_state=rng.integers(2**32))
        self._is_fitted = False

    def _learn_labels(self, bag):
        std = bag.y.std()
        std = 1.0 if std == 0.0 else std
        y = ((bag.y - bag.y.mean())/std)*self._diff + self._center
        return self._kmeans.fit_predict(np.concatenate((bag.x, y.reshape(-1, 1)), axis=1))

    def classify(self, bag):
        labels = self._learn_labels(bag)
        if len(np.unique(labels)) <= 1:
            return np.array([], dtype=np.int)
        self._scaler.fit(bag.x)
        x = self._scaler.transform(bag.x)
        self._svm.fit(x, labels)
        self._is_fitted = self._svm.fit_status_ == 0
        if self._is_fitted:
            return (self._svm.predict(x) >= 0.5).astype(int)
        return np.array([], dtype=np.int)

    def predict(self, x):
        if self._is_fitted:
            return (self._svm.predict(self._scaler.transform(x)) >= 0.5).astype(int)
        else:
            return np.full(len(x), 1, dtype=int)


class Node:  # basic class for recursive decomposition
    _next_id, _all_nodes, _all_leaves = count(), {}, set()

    @staticmethod
    def build_tree(root):
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            for child in node.children:
                if child.is_leaf:
                    Node._all_leaves.remove(child._id)
                else:
                    queue.append(child)
                del Node._all_nodes[child._id]
            node.clear_children()
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            Node._all_nodes[node._id] = node
            children = node.split()
            if len(children) == 0:
                Node._all_leaves.add(node._id)
            else:
                for child in children:
                    queue.append(child)
        return Node._all_nodes[root._id]

    @property
    def best(self):
        return self._bag.best

    @property
    def children(self):
        return [Node._all_nodes[n] for n in self._children]

    @property
    def is_leaf(self):
        return len(self._children) == 0

    @property
    def mean(self):
        return self._bag.mean

    def n_d(self):
        c = len(self._children)
        for n in self._children:
            c += Node._all_nodes[n].n_d()
        return c

    @property
    def parent(self):
        return None if self._parent < 0 else Node._all_nodes[self._parent]

    def _update_cb(self):
        self.cb = self._bag.best.y
        if self._parent >= 0:
            parent = Node._all_nodes[self._parent]
            n_p, n_j = len(parent._bag.y), len(self._bag.y)
            self.cb -= 2.0*self.c_e*np.sqrt(2.0*np.power(n_p, 0.5)/n_j)

    def __init__(self, ndim, leaf_size, c_e, bag, label=-1, parent=-1, lb=None, ub=None, rng=None):
        self._ndim, self._leaf_size, self.c_e = ndim, leaf_size, c_e
        self._lb, self._ub = lb, ub
        self._label, self._parent = label, parent
        self._classifier, self.rng = KMSVM(lb, ub, rng), rng
        self._children = []
        self._bag = bag
        self.cb = float('NaN')
        self._update_cb()
        self._id = next(Node._next_id)
        Node._all_nodes[self._id] = self

    def add_bag(self, bag):
        if not self._bag.extend(bag):
            return
        self._update_cb()
        if self._parent >= 0:
            Node._all_nodes[self._parent].add_bag(bag)

    def classify(self):
        s = []
        if len(self._bag) >= self._leaf_size:
            labels = self._classifier.classify(self._bag)
            unique_labels = np.unique(labels)
            if len(unique_labels) > 1:
                for label in unique_labels:
                    choice = label == labels
                    if choice.sum() < 3:
                        s.clear()
                        break
                    s.append((label, choice))
        return s

    def clear_children(self):
        self._children.clear()

    def path_from_root(self):
        nodes, node = [self], self.parent
        while node is not None:
            nodes.append(node)
            node = node.parent
        nodes.reverse()
        return nodes

    def split(self, s=None):
        self._children.clear()
        s = self.classify() if s is None else s
        children = []
        for label, choice in s:
            bag = Bag(self._bag.x[choice], self._bag.y[choice])
            child = Node(self._ndim, self._leaf_size, self.c_e, bag, label, self._id,
                         self._lb, self._ub, self.rng)
            children.append(child)
            self._children.append(child._id)
        return children

    def sort_leaves(self, nodes):
        if self.is_leaf:
            nodes.append(self)
        else:
            s = sorted(self.children, key=lambda c: (c.cb, c.mean, c.best.y), reverse=False)
            for node in s:
                node.sort_leaves(nodes)


class Path:  # basic class for recursive decomposition
    def __init__(self, nodes):
        self._path = nodes

    def __len__(self):
        return len(self._path)

    def __getitem__(self, i):
        return self._path[i]

    def expand(self):
        last = self._path[-1]
        while not last.is_leaf:
            last = sorted(last.children, key=lambda c: (c.cb, c.mean, c.best.y), reverse=False)[0]
            self._path.append(last)


class Sampler(object):  # for sampling in nodes
    def __init__(self, problem, func, rng, ev):
        self.problem, self._ndim = problem, problem['ndim_problem']
        self.problem['fitness_function'] = func
        self.lb, self.ub = problem['lower_boundary'], problem['upper_boundary']
        self.cmaes, self.rng, self.fitness = None, rng, []
        self.ev = ev

    def sample(self, n_samples, path=None):
        if path is None or len(path) < 2:
            x = (self.ub + self.lb)/2.0
            sigma = np.max(self.ub - self.lb)/6.0
        else:
            bag = path[-1]._bag
            x, x_std = np.mean(bag.x, axis=0), np.std(bag.x, axis=0) 
            sigma = (np.mean(x_std) + 3.0*np.std(x_std))/3.0
            sigma = np.max(self.ub - self.lb)/6.0 if sigma == 0.0 else sigma
        bags = Bag(self._ndim)
        options = {'mean': x, 'sigma': sigma, 'n_individuals': 4,
                   'seed_rng': self.rng.integers(np.iinfo(np.int64).max),
                   'saving_fitness': 1, 'verbose': False, 'max_function_evaluations':
                       self.ev.max_function_evaluations - self.ev.n_function_evaluations}
        self.cmaes = CMAES(self.problem, options)
        self.cmaes.start_time = time.time()
        x, mean, p_s, p_c, cm, e_ve, e_va, y, d = self.cmaes.initialize()
        while len(bags) < n_samples:
            x, y, d = self.cmaes.iterate(x, mean, e_ve, e_va, y, d)
            self.fitness.extend(y)
            if self.ev._check_terminations():
                return bags
            self.cmaes._n_generations += 1
            mean, p_s, p_c, cm, e_ve, e_va = self.cmaes.update_distribution(
                x, p_s, p_c, cm, e_ve, e_va, y, d)
            bags.extend(Bag(np.copy(x), np.copy(y)))
        return bags


class LAMCTS(BO):
    """Latent Action Monte Carlo Tree Search (LAMCTS).

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
                * 'n_individuals' - number of individuals/samples (`int`, default: `100`),
                * 'c_e'           - factor to control exploration (`float`, default: `0.01`),
                * 'leaf_size'     - leaf size (`int`, default: 40).

    Examples
    --------
    Use the black-box optimizer `LAMCTS` to minimize the well-known test function
    `Rosenbrock <http://en.wikipedia.org/wiki/Rosenbrock_function>`_:

    .. code-block:: python
       :linenos:

       >>> import numpy
       >>> from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
       >>> from pypop7.optimizers.bo.lamcts import LAMCTS
       >>> problem = {'fitness_function': rosenbrock,  # to define problem arguments
       ...            'ndim_problem': 2,
       ...            'lower_boundary': -5.0*numpy.ones((2,)),
       ...            'upper_boundary': 5.0*numpy.ones((2,))}
       >>> options = {'max_function_evaluations': 5000,  # to set optimizer options
       ...            'seed_rng': 1}
       >>> lamcts = LAMCTS(problem, options)  # to initialize the optimizer class
       >>> results = lamcts.optimize()  # to run the optimization process
       >>> print(f"LAMCTS: {results['n_function_evaluations']}, {results['best_so_far_y']}")
       LAMCTS: 5000, 0.0001

    For its correctness checking of coding, refer to `this code-based repeatability report
    <https://tinyurl.com/5f827dwh>`_ for more details.

    Attributes
    ----------
    c_e              : float
                       factor to control exploration.
    init_individuals : int
                       number of initial individuals.
    leaf_size        : int
                       leaf size.
    n_individuals    : int
                       number of individuals/samples.

    References
    ----------
    Wang, L., Fonseca, R. and Tian, Y., 2020.
    Learning search space partition for black-box optimization using monte carlo tree search.
    Advances in Neural Information Processing Systems, 33, pp.19511-19522.
    https://arxiv.org/abs/2007.00708 (an updated version)
    https://proceedings.neurips.cc/paper/2020/hash/e2ce14e81dba66dbff9cbc35ecfdb704-Abstract.html
    (the original version)

    https://github.com/facebookresearch/LA-MCTS (an updated version)
    https://github.com/facebookresearch/LaMCTS (the original version)
    """
    def __init__(self, problem, options):
        BO.__init__(self, problem, options)
        self.n_individuals = options.get('n_individuals', 100)  # number of individuals/samples
        self.c_e = options.get('c_e', 0.01)  # factor to control exploration
        self.leaf_size = options.get('leaf_size', 40)  # leaf size
        self.init_individuals = options.get('init_individuals', 100)  # number of initial individuals
        self._sampler, self._root, self._mcts = None, None, None
        self._n_generations = 0
        self.problem = problem

    @property
    def stats(self):
        if self._mcts is not None:
            return self._mcts
        return self._stats()

    def _stats(self):
        if self._root is not None:
            leaves, sizes = [], []
            self._root.sort_leaves(leaves)
            for leaf in leaves:
                sizes.append(len(leaf._bag))
            sizes = np.array(sizes)
            return self._root.n_d() + 1, len(sizes), np.mean(sizes), np.median(sizes)
        else:
            return 0, 0, 0.0, 0.0

    def initialize(self, args=None):
        def _func(x):
            return self._evaluate_fitness(x, args)
        self._sampler = Sampler(self.problem, _func, self.rng_initialization, self)
        samples = self._sampler.sample(self.init_individuals)
        self._root = Node(self.ndim_problem, self.leaf_size, self.c_e*samples.best.y, samples,
                          lb=self.lower_boundary, ub=self.upper_boundary, rng=self.rng_initialization)
        self._root = Node.build_tree(self._root)
        self._mcts = self._stats()

    def iterate(self):
        all_leaves = []
        self._root.sort_leaves(all_leaves)
        bags = None
        for sample_node in all_leaves:
            if self._check_terminations():
                return
            path = Path(sample_node.path_from_root())
            if bags is None:
                bags = self._sampler.sample(self.n_individuals, path)
            else:
                bags.extend(self._sampler.sample(self.n_individuals, path))
            if len(bags) >= self.n_individuals:
                break
        if bags is None or len(bags) == 0:
            bags = self._sampler.sample(self.n_individuals)
        self._root.add_bag(bags)
        self._root.c_e = self.c_e*self._root._bag.best.y
        self._root = Node.build_tree(self._root)
        self._mcts = self._stats()
        self._n_generations += 1

    def _collect(self, fitness, y=None):
        fitness.extend(y)
        results = BO._collect(self, fitness)
        results['_n_generations'] = self._n_generations
        return results

    def optimize(self, fitness_function=None, args=None):
        fitness = BO.optimize(self, fitness_function)
        self.initialize(args)
        while not self._check_terminations():
            self.iterate()
            if self.verbose:
                print(f'n_function_evaluations {self.n_function_evaluations}: ' +
                      f'best_so_far_y {self.best_so_far_y:.5}')
        return self._collect(fitness, self._sampler.fitness)
