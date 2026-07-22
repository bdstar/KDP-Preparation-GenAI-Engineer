model = GPT(GPTConfig()).to("cuda")
opt = torch.optim.AdamW(model.parameters(), lr=3e-4)
 
for step in range(5000):
    xb, yb = get_batch("train")        # (B, block_size) context and targets
    _, loss = model(xb, yb)
    opt.zero_grad(set_to_none=True)
    loss.backward()
    opt.step()
