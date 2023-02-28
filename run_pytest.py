"""
run_pytest.py

This module will run pytest on your repo.

Intended for use in ECIS 639 source repositories.

To use this file:

1. save a copy to the root of your project directory
   (at the same folder depth as requirements.txt)

2. Run the copy in your root directory using IDLE

You will see test output printed in the Python shell.

"""
import pytest
import os

os.environ["NO_COLOR"] = "1"
pytest.main()
