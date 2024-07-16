import json
import numpy as np
def read_txt(file):
    with open(file) as f:
        return f.read().splitlines()

def read_json(file):
    with open(file) as f:
        return json.load(f)
    
def read_npy(file):
    return np.load(file)

def read_npz(file):
    return dict(np.load(file))