import os
import shutil


# Paths to the image and label directories
image_dir = 'Images/Images'
label_dir = 'YOLO_Annotations/YOLO_Annotations'
output_dir = 'output'


# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Get a mapping of class IDs to class names (modify as per your dataset)
class_names = [
    "ace_of_spades", "ace_of_clubs", "ace_of_diamonds", "ace_of_hearts",
    "2_of_spades", "2_of_clubs", "2_of_diamonds", "2_of_hearts",
    "3_of_spades", "3_of_clubs", "3_of_diamonds", "3_of_hearts",
    "4_of_spades", "4_of_clubs", "4_of_diamonds", "4_of_hearts",
    "5_of_spades", "5_of_clubs", "5_of_diamonds", "5_of_hearts",
    "6_of_spades", "6_of_clubs", "6_of_diamonds", "6_of_hearts",
    "7_of_spades", "7_of_clubs", "7_of_diamonds", "7_of_hearts",
    "8_of_spades", "8_of_clubs", "8_of_diamonds", "8_of_hearts",
    "9_of_spades", "9_of_clubs", "9_of_diamonds", "9_of_hearts",
    "10_of_spades", "10_of_clubs", "10_of_diamonds", "10_of_hearts",
    "jack_of_spades", "jack_of_clubs", "jack_of_diamonds", "jack_of_hearts",
    "queen_of_spades", "queen_of_clubs", "queen_of_diamonds", "queen_of_hearts",
    "king_of_spades", "king_of_clubs", "king_of_diamonds", "king_of_hearts",
    "joker"
]


# Loop over each label file
for label_file in os.listdir(label_dir):
    if label_file.endswith('.txt'):
        # Read the label file
        with open(os.path.join(label_dir, label_file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                class_id = int(line.split()[0])  # Extract class ID
                if class_id < 0 or class_id >= len(class_names):
                    print(f"Invalid class_id {class_id} in file {label_file}")
                    continue  # Skip invalid class_id
                class_name = class_names[class_id]  # Map class ID to class name

                # Get the corresponding image file
                image_file = label_file.replace('.txt', '.jpg')  # or .png, depending on your dataset

                # Create the class folder if it doesn't exist
                class_dir = os.path.join(output_dir, class_name)
                if not os.path.exists(class_dir):
                    os.makedirs(class_dir)

                # Move the image to the correct class folder
                src_image_path = os.path.join(image_dir, image_file)
                dst_image_path = os.path.join(class_dir, image_file)
                if os.path.exists(src_image_path):
                    shutil.copy(src_image_path, dst_image_path)
                else:
                    print(f"Image file {src_image_path} does not exist")