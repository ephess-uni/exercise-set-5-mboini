""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
import os
from argparse import ArgumentParser

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)

    par = ArgumentParser(description='prints the data from the inputfile to the outputfile applying standard scale transform')
    par.add_argument('infile',help='input file path',nargs='?')
    par.add_argument('outfile',help='output file path',nargs='?')
    arg_parse = par.parse_args()
    input_data = np.loadtxt(arg_parse.infile)
    scaled_data1 = (input_data - input_data.mean(axis=0)) 
    scaled_data2 = input_data.std(axis=0)
    processed = scaled_data1/scaled_data2
    root_dir = get_repository_root()
    os.makedirs(root_dir / "outputs", exist_ok=True)
    np.savetxt(arg_parse.outfile, processed, fmt='%.2e')
