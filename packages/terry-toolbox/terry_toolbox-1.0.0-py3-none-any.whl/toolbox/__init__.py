from pathlib import Path
import numpy as np

def get_directory(filename):
    path = Path(filename)
    while path.is_file():
        path = path.parent
    return path

PI = np.pi
