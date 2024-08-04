`dspace`: Your **D**efault Name**Space**

# Install
```bash
pip install dspace
```

# Quick Start

## For jupyter notebooks
Import `dspace` when you create a new notebook.
```python
import dspace
```

It will print the default library imports (and any custom lines you want). For now, it prints the following:

```python
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
```

Copy-paste the printed lines in your notebook and remove the `import dspace` line. That's it!

> Well, that's my **D**efault Name**Space**, what's yours?

## Modify the default imports

When you `import dspace` for the first time after installation, it creates `~/.dspace` directory and saves the default imports in the `~/.dspace/.default` file. You can simply modify `~/.dspace/.default` file to change your default imports as per your needs!