"""test_ex_5_4.py
Tests for ex_5_4
"""
from os import path, system
import numpy as np

DIR = path.dirname(__file__)
INFILE = path.join(DIR, "../data/ex_5_4-data.csv")
OUTFILE = path.join(DIR, "../outputs/ex_5_4-processed.csv")
MODULE_PATH = path.join(DIR, "../src/ex_5_4.py")


def test_ex_5_4_creates_correct_output_file():
    system(f'python3 "{MODULE_PATH}"')
    assert path.exists(OUTFILE)


def test_ex_5_4_data_mean_removed():
    data = np.loadtxt(INFILE)
    if not path.exists(OUTFILE):
        system(f'python3 "{MODULE_PATH}"')
    proc = np.loadtxt(OUTFILE)
    assert all(proc[data < 0] == 0)
