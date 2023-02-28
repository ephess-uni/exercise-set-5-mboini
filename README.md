# ex_5_0.py
In a module named ex_5_0.py, implement a function `line_count(infile)` that meets the following requirements:

- takes an input filename `infile`
- opens the file
- counts the number of lines present in the file. *Hint: use readlines()*
- prints the number of lines in the file to standard output (the console/screen)

This module will be used in the next exercise. Note that for this exercise, `infile` is guaranteed to exist.

*Optional but helpful: Test your function with simple files of your creation.  You might also consider adding an entry point for your function*

# ex_5_1.py
In this exercise you will implement a command-line interface for the `line_count` function that you implemented in `ex_5_0.py`. Your module named `ex_5_1.py` will consist only of an entry point that meets the following requirements:

- use the appropriate `if` statement and conditional expression to assure that module code is only executed if the module is run from the command line. Note that it would technically execute if `Run -> Run Module` is selected in IDLE but this exercise is command-line focused.

- instantiate an `argparse.ArgumentParser` object
- configure the ArgumentParser object with the following:
    - a description for the program which includes the text `"This program prints the number of lines in infile."`
    - a positional argument `infile`
- parse the arguments
- call `ex_5_0.line_count` with the infile argument.

To keep the problem simple, the filename that is passed to your program is guaranteed to exist. Your entry point only needs to parse arguments, import and call `line_count` with the appropriate argument.

# ex_5_2.py
This exercise introduces two numpy functions: `numpy.savetxt` and `numpy.loadtxt`.  In this exercise you will begin with a starter module entitled `ex_5_2.py` which includes code to read and write NumPy array data to a file.

Complete `ex_5_2.py` by finishing the `TODO` items included in the comments.  These include:

- modify the input data so that it has a mean of 0.
- modify the zero mean data so that it has a standard deviation of 1.
- make sure to save the processed data to a variable called `processed` so that the `np.savetxt` call succeeds.

For more information about loading and saving data with NumPy, see the official documentation notes on [savetxt](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt) and [loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html?highlight=loadtxt#numpy.loadtxt).

# ex_5_3.py
In `ex_5_3.py` re-create the code from `ex_5_2.py` and implement a command-line interace for it by:

- creating an `argparse.ArgumentParser` object
- configure the ArgumentParser object with the following:
    - a description that includes the text `This program applies a standard scale transform to the data in infile and writes it to outfile.`
    - a positional argument `infile` which should be the input filename for the data file that needs to be processed.
    - a positional argument `outfile` which accepts the output filename.

Test your program with the input data from `data/ex_5_2-data.csv`.


# ex_5_4.py
Use `numpy.loadtxt` to load an array from the file `data/ex_5_4-data.csv`. Your program 
should implement the following:

- load the 1000 element `ndarray` from `data/ex_5_4-data.csv`
- set any negative elements of the array to 0
- write the processed array to a file named `outputs/ex_5_4-processed.csv` using `numpy.savetxt`.

To keep this simple, you may assume that the file `ex_5_4-data.csv` will be available 
to your program. Use `src.util.get_project_root()` to get the root directory of your 
repository. This returns a `pathlib.Path` object which will allow you to refer to the 
input and output files in the following way:

```python
root_directory = get_project_root()
infile = root_directory / 'date' / 'ex_5_4-data.csv'
outfile = root_directory / 'outputs' / 'ex_5_4-processed.csv'
```

NOTE: no command-line interface is required for this exercise.

# Running Python Scripts with Arguments
Running a Python script without arguments is as simple as double-clicking the script 
from a file explorer.  In order to pass arguments to a script, we must run the script 
from the command line.  

## Opening a Command Line Interface on Windows
1. Using File Explorer, navigate to your project `src` directory.
2. Click in the File Explorer address bar
3. Type `cmd` in the address bar and press enter.  A command prompt should open.
4. Run your script with: `python path\to\script arg1 arg2` (for example)

## Opening a Command Line Interface in macOS
1. Use [these instructions](https://support.apple.com/guide/terminal/open-new-terminal-windows-and-tabs-trmlb20c7888/mac) for 
   for information on opening a terminal window from Finder (file explorer)
2. Run your script with: `python3 path/to/script arg1 arg1`

