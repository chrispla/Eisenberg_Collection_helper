# Eisenberg Collection Helper
Helper scripts for audio and metadata management for the Eisenberg Collection

## Tools

* `metadata.py`

   **Description** : get a pandas DataFrame saved in PyTables structure in an HDF5 (.h5) file from a semicolon-separated .csv file with table of metadata <br>

   **Instructions** : run with python3 using the arguments `--input_path` for the path of the .csv file and `--output_dir` for the desired directory of the .h5 file output. If no output directory is specified, output is defaulted to current working directory. Example: <br> 
   ```python
   python3 metadata.py --input_path=/Users/MaSC/Eisenberg_Collection/metadata.csv --ouput_path=/Users/MaSC/Eisenberg_Collection
   ```
* `features.py`

    **Description** : read metadata and find the associated audio files to compute features and store them in an .h5 file as a python dictionary <br>

    **Instructions** : run with python3 using the arguments `--metadata_path` for the path of the .h5 metadata file, `--audio_dir` for the parent directory of the audio files, and `output_dir` for the desired directory of the output. Both audio_dir and output_dir default to current working directory if not specified. Example: <br> 
   ```python
   python3 features.py --metadata_path=/Users/MaSC/Eisenberg_Collection/metadata.h5 --audio_dir=/Users/MaSC/Eisenberg_Collection --output_dir=/Users/MaSC/Eisenberg_Collection
   ```