import torch.nn as nn
 
class MLP(nn.Module):
    def __init__(self, in_dim=784, hidden=256, out_dim=10, p=0.2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.GELU(), nn.Dropout(p),
            nn.Linear(hidden, hidden), nn.GELU(), nn.Dropout(p),
            nn.Linear(hidden, out_dim),
        )
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
                nn.init.zeros_(m.bias)
 
    def forward(self, x):
        return self.net(x)
