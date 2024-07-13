import torch
from .utils import init_parameter

class Triangular(torch.nn.Module):
    """
    Applies a sigmoid transformation to the incoming data.

    Attributes
    ----------
    left_foot : float
        left foot of the triangular function
    peak : float
        peak of the triangular function
    right_foot : float
        right foot of the triangular function

    Returns
    -------
    torch.tensor
        a tensor of equal size to the input tensor
    """
    def __init__(self, left_foot:float = None, peak:float = None, right_foot:float = None) -> None:
        super().__init__()
        self.left_foot = init_parameter(left_foot)
        self.peak = init_parameter(peak)
        self.right_foot = init_parameter(right_foot)
    
    def get_center(self) -> torch.Tensor:
        return self.center
    
    def forward(self, x) -> torch.Tensor:

        term1 = (x - self.left_foot) / (self.peak - self.left_foot)
        term2 = (self.right_foot - x) / (self.right_foot - self.peak)
        
        min_term = torch.min(term1, term2)
        
        return torch.max(min_term, torch.tensor(0.0))