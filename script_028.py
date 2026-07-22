import torch
import torch.nn as nn
from torch.nn import functional as F
from dataclasses import dataclass
 
@dataclass
class GPTConfig:
    vocab_size: int = 65      # char-level Shakespeare
    block_size: int = 256     # context length
    n_layer: int = 6
    n_head: int = 6
    n_embd: int = 384
    dropout: float = 0.2
scaled_dot_product_attention
class CausalSelfAttention(nn.Module):
    def __init__(self, cfg: GPTConfig):
        super().__init__()
        assert cfg.n_embd % cfg.n_head == 0
        self.c_attn = nn.Linear(cfg.n_embd, 3 * cfg.n_embd)  # Q, K, V
        self.c_proj = nn.Linear(cfg.n_embd, cfg.n_embd)      # output W_O
        self.n_head, self.n_embd = cfg.n_head, cfg.n_embd
 
    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
        # reshape into heads: (B, n_head, T, head_dim)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.c_proj(y)
