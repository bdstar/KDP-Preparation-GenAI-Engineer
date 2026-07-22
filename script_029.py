class MLP(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.c_fc   = nn.Linear(cfg.n_embd, 4 * cfg.n_embd)
        self.c_proj = nn.Linear(4 * cfg.n_embd, cfg.n_embd)
        self.act    = nn.GELU()
 
    def forward(self, x):
        return self.c_proj(self.act(self.c_fc(x)))
 
class Block(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.ln1, self.ln2 = nn.LayerNorm(cfg.n_embd), nn.LayerNorm(cfg.n_embd)
        self.attn, self.mlp = CausalSelfAttention(cfg), MLP(cfg)
 
    def forward(self, x):
        x = x + self.attn(self.ln1(x))   # pre-norm + residual
        x = x + self.mlp(self.ln2(x))
        return x
