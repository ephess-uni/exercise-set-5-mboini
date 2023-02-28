"""test_ex_5_0.py"""
from os import path, system
from src.ex_5_0 import line_count

SRC_PATH = path.join(path.dirname(__file__), "../src")


def test_ex_5_0_writes_to_correct_value_to_stdout(capsys):
    infile_fixture = path.join(
        path.dirname(__file__),
        "fixtures",
        "ex_5_0_fixture.txt",
    )
    line_count(infile_fixture)
    captured = capsys.readouterr()
    assert captured.out == "4\n"
