"""
Script to compute audio features for the audio recordings in the Eisenberg Collection.
The script goes through the song titles in the metadata file and checks if there are
audio file paths that contain the title. If there is a match, the features are computed
and added to a dictionary with the NYUAD Archive reference as a key. Audio file paths
that have been matched are removed from the list of paths, so that the audio recordings
that haven't been matched are provided to the user at the end.
"""

import librosa #feature computation
from pathlib import Path #directory traversal
import pandas as pd #read metadata DataFrame
import argparse #parse command line arguments
import deepdish as dd #save python dictionary to HDF5
import sys #display computation progress
import warnings #to filter warnings
from tables import NaturalNameWarning #to filter naming warning from PyTables

# Argument parser
parser = argparse.ArgumentParser(description="audio and metadata directories")
parser.add_argument("--metadata_path", required=True)
parser.add_argument("--audio_dir", default='.')
parser.add_argument("--output_dir", default='.')
args = parser.parse_args()
metadata_path = args.metadata_path
audio_dir = args.audio_dir
output_dir = args.output_dir

# filter naming warnings from PyTables
warnings.filterwarnings('ignore', category=NaturalNameWarning)

# Check if audio directory exists
if not Path(audio_dir).is_dir():
    raise FileNotFoundError("Invalid audio directory: %s, exiting...", audio_dir)

# Check if output directory exists
if not Path(output_dir).is_dir():
    raise FileNotFoundError("Invalid output directory: %s, exiting...", output_dir)

# Read all paths of audio in directory
audio_paths = []
def files_of(root):
    for p in Path(root).iterdir():
        if p.is_dir():
            files_of(p)
        elif p.is_file() and ('.wav' in str(p) or '.mp3' in str(p) or '.aif' in str(p)):  
            # only get paths of audio files
            audio_paths.append(str(p))
files_of(audio_dir)
print("Found", len(audio_paths), "audio files.")

# Read metadata
metadata = pd.read_hdf(metadata_path)

# Dictionary for audio features
# key : NYUAD Archives Reference
# value : {'mfcc' : np.array, 'chromagram' : np.array, 'tempogram' : np.array}
features = {}

# Associate title from metadata with audio path
file_count = 0
for i, row in metadata.iterrows(): 
    title = row['Song Title']
    for path in audio_paths:  
        if title in path:
            file_count += 1

            # Create feature dictionary
            d = {}

            # Compute features
            y, sr = librosa.load(path)
            d['mfcc'] = librosa.feature.mfcc(y, sr)
            d['chromagram'] = librosa.feature.chroma_stft(y, sr)
            d['tempogram'] = librosa.feature.mfcc(y, sr)

            # add features to dictionary, with the archive reference as key
            key = row['NYUAD Archives Reference']
            features[key] = d

            # remove path from list so that it isn't checked in the future
            audio_paths.remove(path)

            break # stop checking paths if there has been a match

    # Progress
    sys.stdout.write("\rComputed features for %i audio files." % file_count)
    sys.stdout.flush()
print('\n' + "Found " + str(file_count-len(audio_paths)) + " unmatched audio files.")

# Save to HDF5
features_path = Path(output_dir) / 'features.h5'
dd.io.save(features_path, features)
print("Saved features.")

# Save unmatched entries
unmatched_path = Path(output_dir) / 'unmatched.txt'
with open(unmatched_path, 'w') as f:
    for item in audio_paths:
        f.write("%s\n" % item)
print("Saved list of unmatched audio files.")
