import pandas as pd
from pathlib import Path
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="input and output path")
parser.add_argument("--input_path", required=True) #path of .csv metadata file
parser.add_argument("--output_dir", default=".") #directory of output
args = parser.parse_args()

input_path = args.input_path
output_dir = args.output_dir

# Compose output path and check validity
if Path(output_dir).is_dir():
    output_path = Path(output_dir) / 'metadata.h5'
else:
    raise FileNotFoundError("Invalid output directory: %s, exiting...", output_dir)

# Read .csv
metadata = pd.read_csv(input_path, sep=';')

# Output to HDF5
metadata.to_hdf(output_path, key='df', format='table')
print("Output completed.")
