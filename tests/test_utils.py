import unittest

import numpy as np

from cyclic_boosting import utils


class TestLinearRegressionWithXError(unittest.TestCase):
    def test_lin_reg_weight_one(self):
        alpha = 3.0
        beta = 0.5
        n = 100
        x = np.linspace(0, 10.0, n)
        y = alpha + beta * x
        w = np.ones(n)
        a, b = utils.linear_regression(x, y, w)
        self.assertAlmostEqual(alpha, a)
        self.assertAlmostEqual(beta, b)

    def test_lin_reg_weighted_events(self):
        np.random.seed(456)
        alpha = 3.0
        beta = 0.5
        n = 100
        x = np.linspace(0, 10.0, n)
        y = alpha + beta * x
        err = np.array([np.mean(np.random.randn(n)) for i in range(n)])
        w = 1.0 / err ** 2
        a, b = utils.linear_regression(x, y + err, w)
        assert abs(alpha - a) < 0.01
        assert abs(beta - b) < 0.01