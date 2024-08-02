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

print(base_libraries)