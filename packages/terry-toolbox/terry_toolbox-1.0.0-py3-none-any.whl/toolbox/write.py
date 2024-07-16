import json
import numpy as np
from pathlib import Path

# def read_txt(file):
#     with open(file) as f:
#         return f.read().splitlines()

# def read_json(file):
#     with open(file) as f:
#         return json.load(f)
    
# def read_npy(file):
#     return np.load(file)

# def read_npz(file):
#     return dict(np.load(file))

def write_json(filename, dict_):
    filepath = Path(filename)
    if filepath.suffix != '.json':
        filepath = filepath.with_suffix('.json')
    
    filepath.parent.mkdir(parents=True, exist_ok=True)
    # assert filepath.exists(), f"{filepath} does not exist"
    
    with open(filepath, 'w') as f:
        json.dump(dict_, f, indent=4)