import torch
from torch import nn

# Dane treningowe: y = 2x + 1 + szum
x = torch.linspace(-1, 1, 100).unsqueeze(1)
y = 2 * x + 1 + 0.1 * torch.randn_like(x)

model = nn.Sequential(
    nn.Linear(1, 1)
)

loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(101):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        print(f"Epoch {epoch:03d}: loss = {loss.item():.6f}")

w = model[0].weight.item()
b = model[0].bias.item()
print(f"Final model: y = {w:.4f}x + {b:.4f}")
