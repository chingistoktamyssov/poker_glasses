import os
import shutil
import random

# Define your paths
data_dir = 'processed_data'  # This is the folder with all the card class subfolders
train_dir = 'train'
valid_dir = 'validate'

# Ensure train and valid directories exist
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
if not os.path.exists(valid_dir):
    os.makedirs(valid_dir)

# Get class subfolders (card names)
classes = os.listdir(data_dir)

# Split images into train and valid sets for each class
for card_class in classes:
    class_dir = os.path.join(data_dir, card_class)
    
    if os.path.isdir(class_dir):
        images = os.listdir(class_dir)
        random.shuffle(images)
        
        # Split the images (80% for training, 20% for validation)
        train_images = images[:int(0.8 * len(images))]
        valid_images = images[int(0.8 * len(images)):]

        # Create subfolders for train/valid
        os.makedirs(os.path.join(train_dir, card_class), exist_ok=True)
        os.makedirs(os.path.join(valid_dir, card_class), exist_ok=True)

        # Move images to train/valid folders
        for img in train_images:
            shutil.move(os.path.join(class_dir, img), os.path.join(train_dir, card_class, img))
        for img in valid_images:
            shutil.move(os.path.join(class_dir, img), os.path.join(valid_dir, card_class, img))
