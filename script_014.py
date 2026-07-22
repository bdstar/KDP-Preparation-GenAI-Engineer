import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
 
tfm = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda x: x.view(-1))])
train_ds = datasets.MNIST(root="data", train=True, download=True, transform=tfm)
test_ds = datasets.MNIST(root="data", train=False, download=True, transform=tfm)
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=256)
