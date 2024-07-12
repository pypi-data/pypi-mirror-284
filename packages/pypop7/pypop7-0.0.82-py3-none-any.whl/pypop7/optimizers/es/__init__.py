"""This open-source Python module provides a set of Evolution Strategies (ES) classes:
    https://pypop.readthedocs.io/en/latest/es/es.html

   For Natural Evolution Strategies (NES), please refer to:
    https://pypop.readthedocs.io/en/latest/nes/nes.html
"""
from pypop7.optimizers.es.es import ES  # abstract class of all evolution strategies (ES)
from pypop7.optimizers.es.res import RES  # Rechenberg’s (1+1)-Evolution Strategy with 1/5th success rule [1973]
from pypop7.optimizers.es.ssaes import SSAES
from pypop7.optimizers.es.dsaes import DSAES
from pypop7.optimizers.es.csaes import CSAES
from pypop7.optimizers.es.saes import SAES
from pypop7.optimizers.es.samaes import SAMAES
from pypop7.optimizers.es.cmaes import CMAES
from pypop7.optimizers.es.maes import MAES
from pypop7.optimizers.es.fmaes import FMAES
from pypop7.optimizers.es.ddcma import DDCMA
from pypop7.optimizers.es.opoc2006 import OPOC2006  # (1+1)-Cholesky-CMA-ES [2006]
from pypop7.optimizers.es.sepcmaes import SEPCMAES  # Separable Covariance Matrix Adaptation Evolution Strategy [2008]
from pypop7.optimizers.es.opoc2009 import OPOC2009  # (1+1)-Cholesky-CMA-ES [2009]
from pypop7.optimizers.es.ccmaes2009 import CCMAES2009  # Cholesky-CMA-ES [2009]
from pypop7.optimizers.es.opoa2010 import OPOA2010  # (1+1)-Active-CMA-ES [2010]
from pypop7.optimizers.es.lmcmaes import LMCMAES  # Limited-Memory CMA-ES [2014]
from pypop7.optimizers.es.opoa2015 import OPOA2015  # (1+1)-Active-CMA-ES [2015]
from pypop7.optimizers.es.ccmaes2016 import CCMAES2016  # Cholesky-CMA-ES [2016]
from pypop7.optimizers.es.lmcma import LMCMA  # Limited-Memory Covariance Matrix Adaptation [2017]
from pypop7.optimizers.es.r1es import R1ES  # Rank-One Evolution Strategy [2018]
from pypop7.optimizers.es.rmes import RMES  # Rank-M Evolution Strategy [2018]
from pypop7.optimizers.es.lmmaes import LMMAES  # Limited-Memory Matrix Adaptation Evolution Strategy [2019]
from pypop7.optimizers.es.mmes import MMES  # Mixture Model-based Evolution Strategy [2021]


__all__ = [ES,  # Evolution Strategies [1964-1965]
           RES,  # Rechenberg’s (1+1)-Evolution Strategy with 1/5th success rule [1973]
           SSAES,  # Schwefel's Self-Adaptation Evolution Strategy
           DSAES,  # Derandomized Self-Adaptation Evolution Strategy
           CSAES,  # Cumulative Step-size self-Adaptation Evolution Strategy
           SAES,  # Self-Adaptation Evolution Strategy
           SAMAES,  # Self-Adaptation Matrix Adaptation Evolution Strategy
           CMAES,  # Covariance Matrix Adaptation Evolution Strategy
           MAES,  # Matrix Adaptation Evolution Strategy
           FMAES,  # Fast Matrix Adaptation Evolution Strategy
           DDCMA,  # Diagonal Decoding Covariance Matrix Adaptation
           OPOC2006,  # (1+1)-Cholesky-CMA-ES [2006]
           SEPCMAES,  # Separable Covariance Matrix Adaptation Evolution Strategy [2008]
           OPOC2009,  # (1+1)-Cholesky-CMA-ES [2009]
           CCMAES2009,  # Cholesky-CMA-ES [2009]
           OPOA2010,  # (1+1)-Active-CMA-ES [2010]
           LMCMAES,  # Limited-Memory CMA-ES [2014]
           OPOA2015,  # (1+1)-Active-CMA-ES [2015]
           CCMAES2016,  # Cholesky-CMA-ES [2016]
           LMCMA,  # Limited-Memory Covariance Matrix Adaptation [2017]
           R1ES,  # Rank-One Evolution Strategy [2018]
           RMES,  # Rank-M Evolution Strategy [2018]
           LMMAES,  # Limited-Memory Matrix Adaptation Evolution Strategy [2019]
           MMES]  # Mixture Model-based Evolution Strategy [2021]
