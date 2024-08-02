from box import base_libraries

vision_libraries = f"""{base_libraries}
# PIL
from PIL import Image

# torch
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import torchvision.models as models
"""

print(vision_libraries)