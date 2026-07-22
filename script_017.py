loss_fn = nn.CrossEntropyLoss()
model = torch.compile(model)              # JIT-compile for speed
 
for epoch in range(epochs):
    model.train()
    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device)
        opt.zero_grad()
        with torch.autocast(device_type=device, dtype=torch.bfloat16):
            loss = loss_fn(model(xb), yb)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        opt.step(); sched.step()
    print(f"epoch {epoch+1}: last batch loss {loss.item():.3f}")
torch.no_grad()
model.eval()
correct = total = 0
with torch.no_grad():
    for xb, yb in test_loader:
        xb, yb = xb.to(device), yb.to(device)
        preds = model(xb).argmax(dim=1)
        correct += (preds == yb).sum().item(); total += yb.size(0)
print(f"test accuracy: {correct / total:.3f}")
