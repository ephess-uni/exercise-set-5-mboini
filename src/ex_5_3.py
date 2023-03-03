import numpy as np
import os
from argparse import ArgumentParser

# Import the get_repository_root function from src.util or util
try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

if __name__ == "__main__":
    # Create the argument parser object
    parser = ArgumentParser(description='Process input file of data, scale and shift to mean 0 and standard deviation 1, and save to output file')
    parser.add_argument('input_file', help='path to input file of data')
    parser.add_argument('output_file', help='path to output file')

    # Parse the input and output file arguments from the command line
    args = parser.parse_args()

    # Load the input data from the input file
    input_data = np.loadtxt(args.input_file)

    # Scale and shift the data to have mean 0 and standard deviation 1
    scaled_data = (input_data - input_data.mean(axis=0)) / input_data.std(axis=0)

    # Create the output directory if it does not already exist
    root_dir = get_repository_root()
    os.makedirs(root_dir / "outputs", exist_ok=True)

    # Save the processed data to the output file
    np.savetxt(args.output_file, scaled_data, fmt='%.2e')
