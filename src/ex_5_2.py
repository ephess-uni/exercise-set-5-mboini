""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np
import os

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":
    
    # Use these predefined input / output files

    root_dir = get_repository_root()

    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    data = np.loadtxt(INFILE)
    pre = (data - data.mean(axis=0)) / data.std(axis=0)
    processed = pre
    
    

    # Complete the data processing steps using numpy here.

    os.makedirs(root_dir / "outputs", exist_ok=True)

    # Save the output to OUTFILE using numpy routines.

    np.savetxt(OUTFILE, processed, fmt='%.2e')
