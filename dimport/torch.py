from dimport import base_libraries

torch_libraries = f"""{base_libraries}
# torch
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, TensorDataset, random_split
"""