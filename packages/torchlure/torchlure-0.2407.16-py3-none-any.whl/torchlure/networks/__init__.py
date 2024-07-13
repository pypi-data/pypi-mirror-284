import einops as ein
import torch
import torch.nn as nn
from torchtyping import TensorType


class ReLUKANLayer(nn.Module):
    def __init__(
        self,
        input_size: int,
        grid: int,
        k: int,
        output_size: int,
        train_bounds: bool = True,
    ):
        super().__init__()
        self.grid = grid
        self.k = k
        self.r = 4 * grid * grid / ((k + 1) * (k + 1))
        self.input_size, self.output_size = input_size, output_size

        phase_low = torch.arange(-k, grid, dtype=torch.float32) / grid
        phase_high = phase_low + (k + 1) / grid
        self.phase_low = nn.Parameter(
            phase_low.repeat(input_size, 1), requires_grad=train_bounds
        )
        self.phase_high = nn.Parameter(
            phase_high.repeat(input_size, 1), requires_grad=train_bounds
        )

        self.conv = nn.Conv2d(1, output_size, (grid + k, input_size))

    def forward(
        self, x: TensorType[..., "input_size"]
    ) -> TensorType[..., "output_size"]:
        *batch_dims, input_size = x.shape
        assert (
            input_size == self.input_size
        ), f"Input size mismatch: expected {self.input_size}, got {input_size}"

        x = ein.rearrange(x, "... d -> ... d 1")
        x1 = torch.relu(x - self.phase_low.unsqueeze(0))
        x2 = torch.relu(self.phase_high.unsqueeze(0) - x)
        x = (x1 * x2 * self.r).pow(2)

        x = ein.rearrange(x, "... d gk -> ... 1 (gk d)", gk=self.grid + self.k)
        x = self.conv(x)
        x = ein.rearrange(x, "... c 1 1 -> ... c")

        return x


class ReLUKAN(nn.Module):
    def __init__(self, width: list[int], grid: int, k: int):
        super().__init__()
        self.layers = nn.ModuleList(
            [
                ReLUKANLayer(width[i], grid, k, width[i + 1])
                for i in range(len(width) - 1)
            ]
        )

    def forward(self, x: TensorType[..., "input_dim"]) -> TensorType[..., "output_dim"]:
        for layer in self.layers:
            x = layer(x)
        return x


def create_relukan_network(
    input_dim: int,
    output_dim: int,
    hidden_dim: int,
    num_layers: int,
    grid: int,
    k: int,
) -> ReLUKAN:
    width = [input_dim] + [hidden_dim] * (num_layers - 1) + [output_dim]
    return ReLUKAN(width, grid, k)
