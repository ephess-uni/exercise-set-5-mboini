"""
install_requirements.py

This module will install pytest and any other requirements.

Intended for use in ECIS 639 source repositories.

To use this file:

1. save a copy to the root of your project directory
   (at the same folder depth as requirements.txt)

2. Run the copy in your root directory using IDLE

3. You only need to run this once.

4. Once the script is run, you can run tests using:

   a. the run_pytest.py script provided. or...

   b. issue the pytest command from a terminal/cmd.exe window
      from the root of your repository.
"""
import pip

# Install pytest using the pip script wrapper "main"
pip.main(["install", "-r", "requirements.txt"])
