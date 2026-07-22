requires_gradTrue.backward().grad
import torch
 
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1     # forward pass builds the graph
y.backward()               # backward pass computes dy/dx
print(x.grad)              # tensor(7.) — because dy/dx = 2x + 3 = 7 at x=2
torch.no_grad()
