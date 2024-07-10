import math
import warnings

import torch
import torch.distributions as D
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from torch.overrides import handle_torch_function, has_torch_function_variadic

from .functions import tanh_exp


class TanhExp(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, threshold=3.0):
        return tanh_exp(x, threshold)
