import math
import warnings
from typing import Literal

import torch
from torchtyping import TensorType

Reduction = Literal["none", "mean", "sum"]


def tanh_exp(x, threshold=3.0):
    """
    TanhExp(x) = x * tanh(exp(x))

    - Clamp is necessary to prevent overflow. Using torch.where alone is insufficient;
        there might be issues when x is small.

    - TanhExp converges to 1 when x is large;  x*tanh(exp(x)) - x < 0f64 if x > 3
    """
    return torch.where(
        x > threshold, x, x * torch.tanh(torch.exp(torch.clamp(x, max=threshold)))
    )


def return_to_go(rewards: TensorType[..., "T"], gamma: float) -> TensorType[..., "T"]:
    if gamma == 1.0:
        return rewards.flip(-1).cumsum(-1).flip(-1)

    seq_len = rewards.shape[-1]
    rtgs = torch.zeros_like(rewards)
    rtg = torch.zeros_like(rewards[..., 0])

    for i in range(seq_len - 1, -1, -1):
        rtg = rewards[..., i] + gamma * rtg
        rtgs[..., i] = rtg

    return rtgs


def quantile_loss(y_pred, y_true, tau, reduction: Reduction = "mean"):
    errors = y_true - y_pred
    loss = torch.max(tau * errors, (tau - 1) * errors)

    match reduction:
        case "none":
            return loss
        case "mean":
            return torch.mean(loss)
        case "sum":
            return torch.sum(loss)
        case _:
            raise ValueError(f"Invalid reduction mode: {reduction}")


def expectile_loss(y_pred, y_true, tau, reduction: Reduction = "mean"):
    errors = y_true - y_pred
    weight = torch.where(errors > 0, tau, 1 - tau)
    loss = weight * errors**2

    match reduction:
        case "none":
            return loss
        case "mean":
            return torch.mean(loss)
        case "sum":
            return torch.sum(loss)
        case _:
            raise ValueError(f"Invalid reduction mode: {reduction}")
