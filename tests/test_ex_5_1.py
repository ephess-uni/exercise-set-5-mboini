"""test_ex_5_1.py"""
from os import path, system

MODULE_PATH = path.join(path.dirname(__file__), "../src/ex_5_1.py")


def test_ex_5_1_has_description(capfd):
    system(f'python "{MODULE_PATH}" -h')
    out_fd, _ = capfd.readouterr()

    assert "prints" in out_fd


def test_ex_5_1_prints_correct_line_count(capfd):
    infile_fixture = path.join(
        path.dirname(__file__),
        "fixtures",
        "ex_5_0_fixture.txt",
    )
    system(f'python "{MODULE_PATH}" "{infile_fixture}"')

    out, _ = capfd.readouterr()

    assert out == "4\n"
