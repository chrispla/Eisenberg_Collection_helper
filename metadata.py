import pandas as pd
import os

# Path of .csv file
input_path = input("Enter path of .csv metadata file: ")
output_dir = input("Enter directory for output (leave blank for current directory): ")

# Exit if path doesn't exist
if not os.path.exists(input_path):
    print("Invalid input path, exiting...")
    exit()

# Check if valid output dir
if not output_dir: #if empty string
    output_path = os.path.join('.', 'metadata.h5')
elif os.path.isdir(output_dir): #existing directory
    output_path = os.path.join(output_dir, 'metadata.h5')
else: #non existant directory
    print("Invalid output directory, exiting...")
    exit()

# Read .csv
try:
    metadata = pd.read_csv(input_path, sep=';')
except:
    print("Incorrect format, exiting...")
    exit()

# Output to HDF5
metadata.to_hdf(output_path, key='df', format='table')
print("Output completed.")