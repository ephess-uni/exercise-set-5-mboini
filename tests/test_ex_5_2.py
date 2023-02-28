from os import path, system
import numpy as np
import pytest

CURDIR = path.dirname(__file__)
INFILE = path.join(CURDIR, "../data/ex_5_2-data.csv")
OUTFILE = path.join(CURDIR, "../outputs/ex_5_2-processed.csv")
MODULE_DIR = path.join(CURDIR, "../src")


@pytest.fixture
def processed():
    system(f'cd "{MODULE_DIR}" && python ex_5_2.py')
    return np.loadtxt(OUTFILE)


def test_ex_5_2_removes_mean(processed):
    mu = processed.mean()

    # Assert that error is less than 1%
    assert np.abs(mu) < 0.01


def test_ex_5_2_scales_unit_std(processed):
    sigma = processed.std()

    # Assert that error is less than 1%
    assert np.abs(1 - sigma) < 0.01
