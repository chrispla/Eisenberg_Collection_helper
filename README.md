# Eisenberg_Collection_helper
Helper scripts for audio and metadata management for the Eisenberg Collection

### Tools

* `metadata.py` : get a pandas DataFrame saved in PyTables structure in an HDF5 (.h5) file from a semicolon-separated .csv file with table of metadata <br>

    **instructions** : run with python3 using the arguments `--input_path` for the path of the .csv file and `--output_dir` for the desired directory of the .h5 file output. If no output directory is specified, output is defaulted to current working directory. Example: `python3 metadata.py --input_path=/Users/MaSC/Eisenberg_Collection/metadata.csv --ouput_path=/Users/MaSC/Eisenberg_Collection`
  

