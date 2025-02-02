import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# Define image transformations (resize, normalize, convert to tensor)
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to match input size for models like ResNet
    transforms.ToTensor(),  # Convert to tensor
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # Normalize
])

# Load the training and validation datasets
train_dataset = datasets.ImageFolder(root=train_dir, transform=transform)
valid_dataset = datasets.ImageFolder(root=valid_dir, transform=transform)

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=32, shuffle=False)