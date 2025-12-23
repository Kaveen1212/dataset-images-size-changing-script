from PIL import Image
import os
from pathlib import Path

# Define source and destination folders
source_folders = ['betel_diseased', 'betel_healthy']
destination_folders = ['betel_diseased_resized', 'betel_healthy_resized']

# Target size
target_size = (512, 512)

# Process each folder
for source_folder, dest_folder in zip(source_folders, destination_folders):
    # Create destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    # Get all image files from source folder
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')

    if os.path.exists(source_folder):
        image_files = [f for f in os.listdir(source_folder) if f.endswith(image_extensions)]

        print(f"\nProcessing {len(image_files)} images from '{source_folder}' to '{dest_folder}'...")

        for idx, image_file in enumerate(image_files, 1):
            try:
                # Open image
                img_path = os.path.join(source_folder, image_file)
                img = Image.open(img_path)

                # Resize image to 250x250
                img_resized = img.resize(target_size, Image.LANCZOS)

                # Save to destination folder
                dest_path = os.path.join(dest_folder, image_file)
                img_resized.save(dest_path)

                print(f"  [{idx}/{len(image_files)}] Resized: {image_file}")

            except Exception as e:
                print(f"  Error processing {image_file}: {str(e)}")

        print(f"✓ Completed '{source_folder}' - {len(image_files)} images resized to 250x250")
    else:
        print(f"Warning: Source folder '{source_folder}' not found!")

print("\n✓ All images have been resized and saved to the new folders!")
