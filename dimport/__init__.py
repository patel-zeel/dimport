import os
from os.path import join, exists, basename, dirname
from ._version import version as __version__  # noqa

base_libraries = """
# Config
import os

# Basic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Monitoring
from tqdm.notebook import tqdm

# IO
from os.path import join, exists, basename, dirname
from glob import glob

# Parallel processing
from joblib import Parallel, delayed
"""

# get user home directory
home = os.path.expanduser("~")

# load or write and load default libraries
if not exists(join(home, ".dimport", ".default")):
    print("Default libraries not found. Writing default libraries to ~/.dimport/.default")
    os.makedirs(join(home, ".dimport"), exist_ok=True)
    with open(join(home, ".dimport", ".default"), "w") as f:
        f.write(base_libraries)

with open(join(home, ".dimport", ".default"), "r") as f:
    default = f.read().strip()

print(default)