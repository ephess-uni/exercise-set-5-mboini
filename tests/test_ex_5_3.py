"""test_ex_5_3.py"""
from os import path, system
from tempfile import TemporaryFile

MODULE_PATH = path.join(path.dirname(__file__), "../src/ex_5_3.py")
INFILE = path.join(path.dirname(__file__), "../data/ex_5_2-data.csv")
OUTFILE = path.join(path.dirname(__file__), "../outputs/test_ex_5_3.csv")


def test_ex_5_3_has_description(capfd):
    system(f'python "{MODULE_PATH}" -h')
    out_fd, _ = capfd.readouterr()

    assert "transform" in out_fd


def test_ex_5_3_writes_correct_file():
    system(f'python "{MODULE_PATH}" "{INFILE}" "{OUTFILE}"')
    assert path.exists(OUTFILE)
