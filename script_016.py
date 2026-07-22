import math
 
device = "cuda" if torch.cuda.is_available() else "cpu"
model = MLP().to(device)
opt = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.01)
epochs, warmup = 5, 100
steps = epochs * len(train_loader)
 
def lr_at(step):                          # linear warmup then cosine decay
    if step < warmup:
        return step / warmup
    progress = (step - warmup) / (steps - warmup)
    return 0.5 * (1 + math.cos(math.pi * progress))
 
sched = torch.optim.lr_scheduler.LambdaLR(opt, lr_lambda=lr_at)
